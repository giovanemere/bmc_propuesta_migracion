# Guía de Implementación Técnica - BMC AWS Migration

## Configuración de Infraestructura AWS

### 1. Setup Inicial del Ambiente

#### AWS Account Configuration
```bash
# Configure AWS CLI
aws configure set region us-east-1
aws configure set output json

# Create VPC for BMC
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=BMC-VPC}]'

# Create subnets
aws ec2 create-subnet --vpc-id vpc-xxx --cidr-block 10.0.1.0/24 --availability-zone us-east-1a
aws ec2 create-subnet --vpc-id vpc-xxx --cidr-block 10.0.2.0/24 --availability-zone us-east-1b
```

#### RDS PostgreSQL Setup
```bash
# Create DB subnet group
aws rds create-db-subnet-group \
    --db-subnet-group-name bmc-db-subnet-group \
    --db-subnet-group-description "BMC Database Subnet Group" \
    --subnet-ids subnet-xxx subnet-yyy

# Create RDS instance for 60M products
aws rds create-db-instance \
    --db-instance-identifier bmc-products-db \
    --db-instance-class db.r5.2xlarge \
    --engine postgres \
    --engine-version 14.9 \
    --allocated-storage 1000 \
    --storage-type gp3 \
    --storage-encrypted \
    --db-name bmcproducts \
    --master-username bmcadmin \
    --manage-master-user-password \
    --db-subnet-group-name bmc-db-subnet-group \
    --vpc-security-group-ids sg-xxx
```

### 2. Microservices Deployment

#### Product Service (60M Records Handler)
```python
# product_service/main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from redis import Redis
import asyncio
from typing import List, Optional

app = FastAPI(title="BMC Product Service", version="1.0.0")

# Database connection for 60M products
DATABASE_URL = "postgresql://bmcadmin:password@bmc-products-db.xxx.rds.amazonaws.com/bmcproducts"

# Redis cache for product lookups
redis_client = Redis(host='bmc-cache.xxx.cache.amazonaws.com', port=6379, db=0)

@app.get("/products/search")
async def search_products(
    query: str,
    dian_classification: Optional[str] = None,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Search products in 60M records with caching"""
    cache_key = f"product_search:{query}:{dian_classification}:{limit}"
    
    # Check cache first
    cached_result = redis_client.get(cache_key)
    if cached_result:
        return json.loads(cached_result)
    
    # Database query with optimized indexes
    query_builder = db.query(Product)
    if dian_classification:
        query_builder = query_builder.filter(Product.dian_classification == dian_classification)
    
    products = query_builder.filter(
        Product.product_name.ilike(f"%{query}%")
    ).limit(limit).all()
    
    result = [product.to_dict() for product in products]
    
    # Cache for 24 hours
    redis_client.setex(cache_key, 86400, json.dumps(result))
    
    return result

@app.post("/products/match-invoice")
async def match_invoice_products(invoice_data: dict):
    """Match invoice items with 60M product database"""
    matched_products = []
    
    for item in invoice_data.get('items', []):
        # Use fuzzy matching for product names
        matches = await fuzzy_match_product(
            item['product_name'],
            item.get('quantity_unit'),
            item.get('category_hint')
        )
        matched_products.append({
            'original_item': item,
            'matches': matches,
            'confidence': calculate_match_confidence(matches)
        })
    
    return {
        'invoice_id': invoice_data['invoice_id'],
        'matched_products': matched_products,
        'total_matches': len(matched_products)
    }
```

#### OCR Processing Service
```python
# ocr_service/main.py
import boto3
from fastapi import FastAPI, UploadFile, File
import asyncio
from PIL import Image
import io

app = FastAPI(title="BMC OCR Service", version="1.0.0")

textract = boto3.client('textract')
s3 = boto3.client('s3')

@app.post("/ocr/process-image")
async def process_invoice_image(file: UploadFile = File(...)):
    """Process invoice image with >95% accuracy requirement"""
    
    # Upload to S3 for Textract processing
    s3_key = f"invoices/images/{file.filename}"
    s3.upload_fileobj(file.file, 'bmc-documents-raw', s3_key)
    
    # Start Textract analysis
    response = textract.start_document_analysis(
        DocumentLocation={
            'S3Object': {
                'Bucket': 'bmc-documents-raw',
                'Name': s3_key
            }
        },
        FeatureTypes=['TABLES', 'FORMS']
    )
    
    job_id = response['JobId']
    
    # Poll for completion
    while True:
        result = textract.get_document_analysis(JobId=job_id)
        status = result['JobStatus']
        
        if status == 'SUCCEEDED':
            break
        elif status == 'FAILED':
            raise HTTPException(status_code=500, detail="OCR processing failed")
        
        await asyncio.sleep(2)
    
    # Extract structured data
    extracted_data = extract_invoice_structure(result['Blocks'])
    
    # Validate accuracy (must be >95%)
    confidence_score = calculate_confidence(result['Blocks'])
    if confidence_score < 95.0:
        return {
            'status': 'low_confidence',
            'confidence': confidence_score,
            'requires_manual_review': True,
            'extracted_data': extracted_data
        }
    
    return {
        'status': 'success',
        'confidence': confidence_score,
        'extracted_data': extracted_data,
        'processing_time': result.get('ProcessingTime', 0)
    }

def extract_invoice_structure(blocks):
    """Extract invoice structure from Textract blocks"""
    invoice_data = {
        'invoice_number': None,
        'invoice_date': None,
        'items': [],
        'total_amount': None
    }
    
    # Process blocks to extract structured data
    for block in blocks:
        if block['BlockType'] == 'KEY_VALUE_SET':
            # Extract key-value pairs
            if 'invoice' in block.get('Text', '').lower():
                invoice_data['invoice_number'] = extract_value(block)
        elif block['BlockType'] == 'TABLE':
            # Extract table data (invoice items)
            items = extract_table_items(block)
            invoice_data['items'].extend(items)
    
    return invoice_data
```

#### Invoice Processing Service
```python
# invoice_service/main.py
from fastapi import FastAPI, BackgroundTasks
import boto3
from sqlalchemy.orm import Session

app = FastAPI(title="BMC Invoice Service", version="1.0.0")

sqs = boto3.client('sqs')
eventbridge = boto3.client('events')

@app.post("/invoices/upload")
async def upload_invoice(
    file_type: str,  # 'image', 'pdf', 'xml'
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """Handle invoice upload and trigger processing pipeline"""
    
    # Create invoice record
    invoice = Invoice(
        invoice_number=generate_invoice_number(),
        document_type=file_type,
        processing_status='UPLOADED',
        created_at=datetime.utcnow()
    )
    db.add(invoice)
    db.commit()
    
    # Trigger appropriate processing based on file type
    if file_type in ['image', 'pdf']:
        # Send to OCR processing queue
        background_tasks.add_task(
            trigger_ocr_processing,
            invoice.invoice_id,
            file_type
        )
    else:
        # Direct processing for structured data
        background_tasks.add_task(
            trigger_direct_processing,
            invoice.invoice_id
        )
    
    return {
        'invoice_id': invoice.invoice_id,
        'status': 'uploaded',
        'processing_queue': 'ocr' if file_type in ['image', 'pdf'] else 'direct'
    }

@app.post("/invoices/{invoice_id}/calculate-commission")
async def calculate_commission(invoice_id: int, db: Session = Depends(get_db)):
    """Calculate commission based on business rules"""
    
    invoice = db.query(Invoice).filter(Invoice.invoice_id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    # Get invoice items with product matches
    items = db.query(InvoiceItem).filter(InvoiceItem.invoice_id == invoice_id).all()
    
    total_commission = 0
    commission_details = []
    
    for item in items:
        # Apply business rules based on DIAN classification
        product = db.query(Product).filter(Product.product_id == item.product_id).first()
        
        commission_rate = get_commission_rate(
            product.dian_classification,
            item.total_amount,
            invoice.invoice_date
        )
        
        item_commission = item.total_amount * commission_rate
        total_commission += item_commission
        
        commission_details.append({
            'item_id': item.item_id,
            'product_code': product.product_code,
            'amount': item.total_amount,
            'rate': commission_rate,
            'commission': item_commission
        })
    
    # Save commission record
    commission = Commission(
        invoice_id=invoice_id,
        commission_rate=total_commission / sum(item.total_amount for item in items),
        commission_amount=total_commission,
        calculation_date=datetime.utcnow(),
        business_rule_version='v2.1'
    )
    db.add(commission)
    db.commit()
    
    # Trigger certificate generation
    await trigger_certificate_generation(invoice_id, commission.commission_id)
    
    return {
        'invoice_id': invoice_id,
        'total_commission': total_commission,
        'commission_details': commission_details,
        'commission_id': commission.commission_id
    }
```

### 3. Database Migration Scripts

#### Product Migration (60M Records)
```python
# migration/migrate_products.py
import pandas as pd
from sqlalchemy import create_engine
import boto3
from concurrent.futures import ThreadPoolExecutor
import logging

def migrate_products_batch(batch_data, batch_number):
    """Migrate a batch of products (10K records per batch)"""
    engine = create_engine(DATABASE_URL)
    
    try:
        # Process batch
        batch_data.to_sql(
            'products',
            engine,
            schema='bmc_transactional',
            if_exists='append',
            index=False,
            method='multi',
            chunksize=1000
        )
        
        logging.info(f"Batch {batch_number} completed: {len(batch_data)} records")
        return True
        
    except Exception as e:
        logging.error(f"Batch {batch_number} failed: {str(e)}")
        return False

def main():
    """Main migration function for 60M products"""
    
    # Read from Google Cloud export
    source_file = 'gs://bmc-export/products_export.csv'
    
    # Process in batches of 10K records
    batch_size = 10000
    batch_number = 0
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        for chunk in pd.read_csv(source_file, chunksize=batch_size):
            batch_number += 1
            
            # Clean and validate data
            chunk = clean_product_data(chunk)
            
            # Submit batch for processing
            executor.submit(migrate_products_batch, chunk, batch_number)
            
            if batch_number % 100 == 0:
                logging.info(f"Submitted {batch_number} batches ({batch_number * batch_size} records)")

def clean_product_data(df):
    """Clean and validate product data"""
    # Remove duplicates
    df = df.drop_duplicates(subset=['product_code'])
    
    # Validate DIAN classifications
    valid_classifications = ['1', '2', '3']  # Alimentos, Cantidad, Unidad
    df = df[df['dian_classification'].isin(valid_classifications)]
    
    # Clean product names
    df['product_name'] = df['product_name'].str.strip().str.title()
    
    # Validate required fields
    df = df.dropna(subset=['product_code', 'product_name', 'dian_classification'])
    
    return df

if __name__ == "__main__":
    main()
```

### 4. Performance Optimization

#### Database Indexing for 60M Records
```sql
-- Create optimized indexes for 60M product lookups
CREATE INDEX CONCURRENTLY idx_products_code_hash ON bmc_transactional.products USING hash(product_code);
CREATE INDEX CONCURRENTLY idx_products_name_gin ON bmc_transactional.products USING gin(to_tsvector('spanish', product_name));
CREATE INDEX CONCURRENTLY idx_products_dian_btree ON bmc_transactional.products(dian_classification, category_id);

-- Composite index for common queries
CREATE INDEX CONCURRENTLY idx_products_lookup ON bmc_transactional.products(dian_classification, product_name varchar_pattern_ops);

-- Analyze tables for query optimization
ANALYZE bmc_transactional.products;
```

#### Redis Caching Strategy
```python
# cache/redis_manager.py
import redis
import json
import hashlib
from typing import Optional, List

class BMCCacheManager:
    def __init__(self):
        self.redis_client = redis.Redis(
            host='bmc-cache.xxx.cache.amazonaws.com',
            port=6379,
            db=0,
            decode_responses=True
        )
    
    def cache_product_lookup(self, query: str, results: List[dict], ttl: int = 86400):
        """Cache product lookup results for 24 hours"""
        cache_key = f"product_lookup:{hashlib.md5(query.encode()).hexdigest()}"
        self.redis_client.setex(cache_key, ttl, json.dumps(results))
    
    def get_cached_product_lookup(self, query: str) -> Optional[List[dict]]:
        """Get cached product lookup results"""
        cache_key = f"product_lookup:{hashlib.md5(query.encode()).hexdigest()}"
        cached_data = self.redis_client.get(cache_key)
        
        if cached_data:
            return json.loads(cached_data)
        return None
    
    def cache_dian_classification(self, classification: str, metadata: dict):
        """Cache DIAN classification metadata for 7 days"""
        cache_key = f"dian_classification:{classification}"
        self.redis_client.setex(cache_key, 604800, json.dumps(metadata))  # 7 days
    
    def invalidate_product_cache(self, product_code: str):
        """Invalidate cache when product is updated"""
        pattern = f"product_lookup:*{product_code}*"
        keys = self.redis_client.keys(pattern)
        if keys:
            self.redis_client.delete(*keys)
```

### 5. Monitoring y Alertas

#### CloudWatch Custom Metrics
```python
# monitoring/metrics.py
import boto3
from datetime import datetime

cloudwatch = boto3.client('cloudwatch')

def publish_ocr_metrics(confidence_score: float, processing_time: float):
    """Publish OCR processing metrics"""
    cloudwatch.put_metric_data(
        Namespace='BMC/OCR',
        MetricData=[
            {
                'MetricName': 'ConfidenceScore',
                'Value': confidence_score,
                'Unit': 'Percent',
                'Timestamp': datetime.utcnow()
            },
            {
                'MetricName': 'ProcessingTime',
                'Value': processing_time,
                'Unit': 'Seconds',
                'Timestamp': datetime.utcnow()
            }
        ]
    )

def publish_product_lookup_metrics(query_time: float, cache_hit: bool):
    """Publish product lookup performance metrics"""
    cloudwatch.put_metric_data(
        Namespace='BMC/ProductService',
        MetricData=[
            {
                'MetricName': 'QueryTime',
                'Value': query_time,
                'Unit': 'Milliseconds',
                'Timestamp': datetime.utcnow()
            },
            {
                'MetricName': 'CacheHitRate',
                'Value': 1 if cache_hit else 0,
                'Unit': 'Count',
                'Timestamp': datetime.utcnow()
            }
        ]
    )
```

### 6. Deployment Scripts

#### ECS Fargate Deployment
```yaml
# deployment/docker-compose.yml
version: '3.8'
services:
  product-service:
    build: ./product_service
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - REDIS_URL=${REDIS_URL}
      - AWS_REGION=us-east-1
    deploy:
      replicas: 3
      resources:
        limits:
          memory: 2G
          cpus: '1.0'
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  ocr-service:
    build: ./ocr_service
    environment:
      - AWS_REGION=us-east-1
      - S3_BUCKET=bmc-documents-raw
    deploy:
      replicas: 2
      resources:
        limits:
          memory: 4G
          cpus: '2.0'

  invoice-service:
    build: ./invoice_service
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - SQS_QUEUE_URL=${SQS_QUEUE_URL}
    deploy:
      replicas: 3
      resources:
        limits:
          memory: 1G
          cpus: '0.5'
```

#### Terraform Infrastructure
```hcl
# infrastructure/main.tf
provider "aws" {
  region = "us-east-1"
}

# RDS for 60M products
resource "aws_db_instance" "bmc_products" {
  identifier = "bmc-products-db"
  
  engine         = "postgres"
  engine_version = "14.9"
  instance_class = "db.r5.2xlarge"
  
  allocated_storage     = 1000
  max_allocated_storage = 5000
  storage_type         = "gp3"
  storage_encrypted    = true
  
  db_name  = "bmcproducts"
  username = "bmcadmin"
  manage_master_user_password = true
  
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = aws_db_subnet_group.bmc.name
  
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"
  
  performance_insights_enabled = true
  monitoring_interval         = 60
  
  tags = {
    Name = "BMC Products Database"
    Environment = "production"
  }
}

# ElastiCache Redis for caching
resource "aws_elasticache_replication_group" "bmc_cache" {
  replication_group_id       = "bmc-cache"
  description                = "BMC Redis Cache"
  
  node_type                  = "cache.r6g.large"
  port                       = 6379
  parameter_group_name       = "default.redis7"
  
  num_cache_clusters         = 2
  automatic_failover_enabled = true
  multi_az_enabled          = true
  
  subnet_group_name = aws_elasticache_subnet_group.bmc.name
  security_group_ids = [aws_security_group.redis.id]
  
  at_rest_encryption_enabled = true
  transit_encryption_enabled = true
  
  tags = {
    Name = "BMC Cache Cluster"
    Environment = "production"
  }
}
```

Esta guía técnica proporciona la implementación detallada para migrar el sistema BMC a AWS, incluyendo el manejo de 60M productos, procesamiento OCR, y todas las integraciones necesarias.
