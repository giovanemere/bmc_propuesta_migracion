# MCP Arquitectura BMC - Actualizado con Diagramas como Código

## Infraestructura como Código - Terraform

### Estructura del Proyecto
```
infrastructure/
├── terraform/
│   ├── main.tf                 # Configuración principal
│   ├── variables.tf            # Variables de configuración
│   ├── outputs.tf              # Outputs de recursos
│   └── modules/
│       ├── vpc/                # Módulo VPC
│       ├── ecs/                # Módulo ECS Fargate
│       ├── rds/                # Módulo RDS PostgreSQL
│       ├── elasticache/        # Módulo Redis
│       ├── s3/                 # Módulo S3
│       ├── lambda/             # Módulo Lambda
│       ├── api_gateway/        # Módulo API Gateway
│       └── monitoring/         # Módulo CloudWatch
└── diagrams/
    ├── bmc_architecture.py     # Generador de diagramas
    ├── bmc_process_flows.py    # Flujos de proceso
    ├── generate_all.sh         # Script de generación
    └── requirements.txt        # Dependencias Python
```

### Configuración Principal (main.tf)
```hcl
# BMC AWS Infrastructure - Main Configuration
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Project     = "BMC-Migration"
      Environment = var.environment
      ManagedBy   = "Terraform"
      Owner       = "BMC-Team"
    }
  }
}

# VPC and Networking
module "vpc" {
  source = "./modules/vpc"
  
  name_prefix = local.name_prefix
  cidr_block  = var.vpc_cidr
  azs         = local.azs
  
  tags = local.common_tags
}

# RDS PostgreSQL (60M Products)
module "rds" {
  source = "./modules/rds"
  
  name_prefix           = local.name_prefix
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  security_group_ids   = [module.security_groups.rds_sg_id]
  
  instance_class       = var.rds_instance_class
  allocated_storage    = var.rds_allocated_storage
  max_allocated_storage = var.rds_max_allocated_storage
  
  tags = local.common_tags
}

# ECS Fargate Cluster
module "ecs" {
  source = "./modules/ecs"
  
  name_prefix        = local.name_prefix
  vpc_id            = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_subnet_ids
  public_subnet_ids  = module.vpc.public_subnet_ids
  security_group_ids = [module.security_groups.ecs_sg_id]
  microservices     = var.microservices
  
  tags = local.common_tags
}
```

## Diagramas como Código - Python

### Generador de Arquitectura Principal
```python
#!/usr/bin/env python3
"""
BMC AWS Architecture Diagram Generator
Generates PNG diagrams with AWS icons using diagrams library
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS, Lambda, Fargate
from diagrams.aws.database import RDS, Redshift, ElastiCache
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway, CloudFront, ELB
from diagrams.aws.security import Cognito, IAM, WAF, KMS
from diagrams.aws.integration import EventBridge, SQS, SNS
from diagrams.aws.analytics import Textract, Comprehend
from diagrams.aws.management import CloudWatch, XRay, CloudTrail

def generate_main_architecture():
    """Generate main BMC architecture diagram"""
    
    with Diagram("BMC AWS Architecture - 60M Products Platform", 
                 filename="bmc_main_architecture", 
                 show=False, 
                 direction="TB"):
        
        # Users
        users = OnPremUsers("BMC Users")
        external = OnPremUsers("External Systems")
        
        with Cluster("AWS Cloud"):
            # Edge Layer
            with Cluster("Edge & Security"):
                cloudfront = CloudFront("CloudFront CDN")
                waf = WAF("AWS WAF")
                
            # API Layer
            with Cluster("API Gateway"):
                api_gateway = APIGateway("API Gateway")
                cognito = Cognito("User Auth")
                
            # Compute Layer - Microservices
            with Cluster("Microservices (ECS Fargate)"):
                with Cluster("Invoice Service"):
                    invoice_service = Fargate("Invoice\n2 vCPU, 4GB")
                    
                with Cluster("Product Service (60M)"):
                    product_service = Fargate("Product\n4 vCPU, 8GB")
                    
                with Cluster("OCR Service"):
                    ocr_service = Fargate("OCR\n2 vCPU, 4GB")
                    
                with Cluster("Commission Service"):
                    commission_service = Fargate("Commission\n1 vCPU, 2GB")
                    
                with Cluster("Certificate Service"):
                    certificate_service = Fargate("Certificate\n1 vCPU, 2GB")
            
            # AI/ML Services
            with Cluster("AI/ML Services"):
                textract = Textract("Amazon Textract\nOCR >95%")
                comprehend = Comprehend("Amazon Comprehend\nNLP Analysis")
                
            # Data Layer
            with Cluster("Data Layer"):
                with Cluster("Transactional"):
                    rds_primary = RDS("RDS PostgreSQL\n60M Products\nMulti-AZ")
                    rds_replica = RDS("Read Replica\nQuery Optimization")
                    
                with Cluster("Caching"):
                    redis = ElastiCache("ElastiCache Redis\nProduct Cache\n24h TTL")
                    
                with Cluster("Analytics"):
                    redshift = Redshift("Redshift\nData Warehouse\nOLAP")
                    
                with Cluster("Document Storage"):
                    s3_docs = S3("S3 Documents\nIntelligent Tiering")
                    s3_backup = S3("S3 Backup\nCross-Region")
                    
            # Integration Layer
            with Cluster("Event-Driven Integration"):
                eventbridge = EventBridge("EventBridge\nEvent Bus")
                sqs_fifo = SQS("SQS FIFO\nInvoice Queue")
                sqs_standard = SQS("SQS Standard\nOCR Queue")
                sns = SNS("SNS\nNotifications")
                
            # Monitoring
            with Cluster("Monitoring & Observability"):
                cloudwatch = CloudWatch("CloudWatch\nMetrics & Logs")
                xray = XRay("X-Ray\nDistributed Tracing")
                cloudtrail = CloudTrail("CloudTrail\nAudit Logs")
        
        # Flow connections
        users >> cloudfront >> waf >> api_gateway
        api_gateway >> cognito
        api_gateway >> [invoice_service, product_service, ocr_service]
        
        # Service interactions
        invoice_service >> ocr_service >> textract
        product_service >> redis >> rds_primary
        ocr_service >> s3_docs
        
        # Event flows
        invoice_service >> eventbridge >> [sqs_fifo, sqs_standard, sns]
        
        # Data flows
        rds_primary >> rds_replica
        product_service >> redshift
        s3_docs >> s3_backup
        
        # Monitoring
        [invoice_service, product_service, ocr_service] >> cloudwatch
```

### Microservicios Detallados
```python
def generate_microservices_detail():
    """Generate detailed microservices architecture"""
    
    with Diagram("BMC Microservices Architecture - ECS Fargate", 
                 filename="bmc_microservices_detail", 
                 show=False, 
                 direction="TB"):
        
        with Cluster("API Gateway Layer"):
            api_gateway = APIGateway("API Gateway\nCentral Router")
            
        with Cluster("ECS Fargate Cluster"):
            with Cluster("Invoice Service Pod"):
                invoice_alb = ELB("Invoice ALB")
                invoice_tasks = [
                    Fargate("Invoice Task 1\n2 vCPU, 4GB"),
                    Fargate("Invoice Task 2\n2 vCPU, 4GB"),
                    Fargate("Invoice Task N\nAuto Scaling 2-10")
                ]
                
            with Cluster("Product Service Pod (60M Records)"):
                product_alb = ELB("Product ALB")
                product_tasks = [
                    Fargate("Product Task 1\n4 vCPU, 8GB"),
                    Fargate("Product Task 2\n4 vCPU, 8GB"),
                    Fargate("Product Task N\nAuto Scaling 3-15")
                ]
        
        # API Gateway routing
        api_gateway >> [invoice_alb, product_alb]
        
        # Load balancer to tasks
        invoice_alb >> invoice_tasks
        product_alb >> product_tasks
```

## Configuración de Microservicios

### Variables de Configuración
```hcl
# Microservices Configuration
variable "microservices" {
  description = "Microservices configuration"
  type = map(object({
    cpu    = number
    memory = number
    port   = number
    min_capacity = number
    max_capacity = number
  }))
  
  default = {
    invoice = {
      cpu    = 2048
      memory = 4096
      port   = 8000
      min_capacity = 2
      max_capacity = 10
    }
    product = {
      cpu    = 4096
      memory = 8192
      port   = 8001
      min_capacity = 3
      max_capacity = 15
    }
    ocr = {
      cpu    = 2048
      memory = 4096
      port   = 8002
      min_capacity = 2
      max_capacity = 8
    }
    commission = {
      cpu    = 1024
      memory = 2048
      port   = 8003
      min_capacity = 2
      max_capacity = 6
    }
    certificate = {
      cpu    = 1024
      memory = 2048
      port   = 8004
      min_capacity = 2
      max_capacity = 5
    }
  }
}
```

### ECS Task Definitions
```hcl
# ECS Task Definitions
resource "aws_ecs_task_definition" "microservices" {
  for_each = var.microservices

  family                   = "${var.name_prefix}-${each.key}"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = each.value.cpu
  memory                   = each.value.memory
  execution_role_arn       = aws_iam_role.ecs_execution.arn
  task_role_arn           = aws_iam_role.ecs_task.arn

  container_definitions = jsonencode([
    {
      name  = each.key
      image = "${var.ecr_repository_url}/${each.key}:latest"
      
      portMappings = [
        {
          containerPort = each.value.port
          protocol      = "tcp"
        }
      ]

      environment = [
        {
          name  = "SERVICE_NAME"
          value = each.key
        },
        {
          name  = "ENVIRONMENT"
          value = var.environment
        }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = aws_cloudwatch_log_group.microservices[each.key].name
          awslogs-region        = data.aws_region.current.name
          awslogs-stream-prefix = "ecs"
        }
      }

      healthCheck = {
        command     = ["CMD-SHELL", "curl -f http://localhost:${each.value.port}/health || exit 1"]
        interval    = 30
        timeout     = 5
        retries     = 3
        startPeriod = 60
      }
    }
  ])

  tags = var.tags
}
```

## Base de Datos - RDS PostgreSQL (60M Productos)

### Configuración Optimizada
```hcl
# RDS Instance - Optimized for 60M products
resource "aws_db_instance" "main" {
  identifier = "${var.name_prefix}-postgres"

  # Engine configuration
  engine         = "postgres"
  engine_version = "14.9"
  instance_class = var.instance_class

  # Storage configuration for 60M products
  allocated_storage     = var.allocated_storage
  max_allocated_storage = var.max_allocated_storage
  storage_type         = "gp3"
  storage_encrypted    = true
  kms_key_id          = aws_kms_key.rds.arn

  # Database configuration
  db_name  = "bmc_production"
  username = "bmc_admin"
  password = random_password.db_password.result

  # Performance configuration
  parameter_group_name = aws_db_parameter_group.main.name
  monitoring_interval  = 60
  monitoring_role_arn  = aws_iam_role.rds_monitoring.arn

  # High availability
  multi_az = true

  # Performance Insights
  performance_insights_enabled = true
  performance_insights_kms_key_id = aws_kms_key.rds.arn
  performance_insights_retention_period = 7

  tags = merge(var.tags, {
    Name = "${var.name_prefix}-postgres"
    Purpose = "60M-Products-Database"
  })
}
```

### Parámetros Optimizados
```hcl
# DB Parameter Group for PostgreSQL optimization
resource "aws_db_parameter_group" "main" {
  family = "postgres14"
  name   = "${var.name_prefix}-db-params"

  # Optimizations for 60M products
  parameter {
    name  = "shared_preload_libraries"
    value = "pg_stat_statements"
  }

  parameter {
    name  = "work_mem"
    value = "256MB"
  }

  parameter {
    name  = "maintenance_work_mem"
    value = "2GB"
  }

  parameter {
    name  = "effective_cache_size"
    value = "24GB"
  }

  parameter {
    name  = "random_page_cost"
    value = "1.1"
  }

  parameter {
    name  = "checkpoint_completion_target"
    value = "0.9"
  }

  parameter {
    name  = "wal_buffers"
    value = "16MB"
  }

  parameter {
    name  = "default_statistics_target"
    value = "100"
  }

  tags = var.tags
}
```

## Generación de Diagramas

### Script de Generación Automática
```bash
#!/bin/bash

# BMC AWS Architecture Diagram Generator Script
echo "🚀 BMC AWS Architecture Diagram Generator"
echo "=========================================="

# Install system dependencies for graphviz
echo "📦 Installing system dependencies..."
if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y graphviz
elif command -v yum &> /dev/null; then
    sudo yum install -y graphviz
elif command -v brew &> /dev/null; then
    brew install graphviz
fi

# Create virtual environment
echo "🐍 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Generate diagrams
echo "🎨 Generating BMC AWS Architecture Diagrams..."
python3 bmc_architecture.py
python3 bmc_process_flows.py

echo "✅ Diagrams generated successfully!"
echo "📁 Generated files:"
ls -la *.png
```

### Dependencias Python
```txt
# Requirements for BMC AWS Diagram Generation
diagrams==0.23.4
graphviz==0.20.1
Pillow==10.0.1
```

## Comandos de Despliegue

### Terraform
```bash
# Inicializar Terraform
terraform init

# Planificar despliegue
terraform plan -var-file="prod.tfvars"

# Aplicar infraestructura
terraform apply -var-file="prod.tfvars"

# Destruir infraestructura (si necesario)
terraform destroy -var-file="prod.tfvars"
```

### Generación de Diagramas
```bash
# Generar todos los diagramas
cd infrastructure/diagrams
./generate_all.sh

# Generar diagramas específicos
python3 bmc_architecture.py
python3 bmc_process_flows.py
```

## Archivos Generados

### Diagramas PNG
- `bmc_main_architecture.png` - Arquitectura principal
- `bmc_microservices_detail.png` - Detalle microservicios
- `bmc_data_architecture.png` - Arquitectura de datos
- `bmc_security_architecture.png` - Seguridad y compliance
- `bmc_monitoring_architecture.png` - Monitoreo
- `bmc_invoice_processing_flow.png` - Flujo facturas
- `bmc_product_lookup_flow.png` - Búsqueda productos
- `bmc_ocr_processing_flow.png` - Procesamiento OCR
- `bmc_error_handling_flow.png` - Manejo errores
- `bmc_monitoring_flow.png` - Flujo monitoreo

### Infraestructura Terraform
- Recursos AWS completamente definidos
- Módulos reutilizables
- Variables configurables
- Outputs para integración
- Tags consistentes
- Seguridad por defecto
