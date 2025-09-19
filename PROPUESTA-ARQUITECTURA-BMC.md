# Propuesta de Arquitectura BMC - AWS Migration

## Modelo C4 - Context, Containers, Components, Code

### Nivel 1: Context Diagram

```
[Usuarios BMC] --> [Sistema BMC] --> [DIAN]
[Sistemas Externos] --> [Sistema BMC] --> [Entidades Regulatorias]
[Operadores] --> [Sistema BMC] --> [Reportes Regulatorios]
```

**Actores Principales:**
- **Usuarios BMC:** Operadores de la bolsa comisionista
- **Sistemas Externos:** Integración SFTP con entidades regulatorias
- **DIAN:** Validación de clasificaciones y cumplimiento
- **Entidades Regulatorias:** Intercambio de información financiera

### Nivel 2: Container Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Sistema BMC AWS                          │
├─────────────────────────────────────────────────────────────┤
│  [Web Frontend]     [Mobile App]     [Admin Portal]        │
│       │                  │                 │               │
│       └──────────────────┼─────────────────┘               │
│                          │                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              API Gateway                             │  │
│  └──────────────────────────────────────────────────────┘  │
│                          │                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                Microservices                         │  │
│  │  [Invoice Service] [Product Service] [OCR Service]   │  │
│  │  [Commission Service] [Certificate Service]          │  │
│  │  [Validation Service] [Notification Service]         │  │
│  └──────────────────────────────────────────────────────┘  │
│                          │                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Data Layer                              │  │
│  │  [RDS PostgreSQL] [Redshift] [ElastiCache] [S3]     │  │
│  └──────────────────────────────────────────────────────┘  │
│                          │                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │            External Integrations                     │  │
│  │  [SFTP Gateway] [Email Service] [DIAN API]          │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Nivel 3: Component Diagram - Microservices Detail

#### Invoice Service Components
```
┌─────────────────────────────────────────┐
│           Invoice Service               │
├─────────────────────────────────────────┤
│ • File Upload Handler                   │
│ • OCR Document Processor                │
│ • Batch Processing Engine               │
│ • Invoice Validator                     │
│ • Business Rules Engine                 │
│ • Status Tracker                       │
└─────────────────────────────────────────┘
```

#### Product Service Components
```
┌─────────────────────────────────────────┐
│           Product Service               │
├─────────────────────────────────────────┤
│ • Product Lookup Engine (60M records)  │
│ • DIAN Classification Matcher           │
│ • Cache Manager                         │
│ • Product List API                      │
│ • Search & Filter Engine                │
│ • Data Synchronizer                     │
└─────────────────────────────────────────┘
```

#### OCR Processing Service Components
```
┌─────────────────────────────────────────┐
│        OCR Processing Service           │
├─────────────────────────────────────────┤
│ • Image Preprocessor                    │
│ • PDF Text Extractor                   │
│ • Textract Integration                  │
│ • Accuracy Validator (>95%)            │
│ • Format Converter                      │
│ • Quality Assurance Engine             │
└─────────────────────────────────────────┘
```

## Definiciones de Desarrollo

### Stack Tecnológico

#### Backend Services
```yaml
Language: Python 3.9+
Framework: FastAPI
Architecture: Event-Driven Microservices
Containerization: Docker + ECS Fargate
Orchestration: AWS Step Functions
API Documentation: OpenAPI/Swagger
Testing: pytest + coverage >90%
```

#### Frontend Applications
```yaml
Framework: React 18+ with TypeScript
State Management: Redux Toolkit + RTK Query
UI Library: Material-UI v5
Build Tool: Vite
Testing: Jest + React Testing Library
E2E Testing: Playwright
```

#### Development Standards
```yaml
Code Style: 
  - Python: PEP 8 + Black formatter
  - TypeScript: ESLint + Prettier
  - SQL: snake_case naming

Git Workflow: GitFlow
Branch Protection: Required PR reviews
CI/CD: GitHub Actions + AWS CodePipeline
Code Quality: SonarQube integration
```

### Microservices Architecture

#### Service Communication
```yaml
Synchronous: REST APIs via API Gateway
Asynchronous: EventBridge + SQS
Service Mesh: AWS App Mesh (optional)
Circuit Breaker: AWS Lambda built-in retry
Load Balancing: Application Load Balancer
```

#### Error Handling & Resilience
```yaml
Retry Strategy: Exponential backoff
Dead Letter Queues: SQS DLQ for failed messages
Health Checks: /health endpoints
Monitoring: CloudWatch + X-Ray tracing
Alerting: SNS + CloudWatch Alarms
```

## Definiciones de Base de Datos

### Arquitectura de Datos Multi-Tier

#### Transactional Layer - RDS PostgreSQL
```sql
-- Core Tables Structure
CREATE SCHEMA bmc_transactional;

-- Products table (60M records)
CREATE TABLE bmc_transactional.products (
    product_id BIGSERIAL PRIMARY KEY,
    product_code VARCHAR(50) UNIQUE NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    dian_classification VARCHAR(20) NOT NULL,
    category_id INTEGER NOT NULL,
    unit_type VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Invoices table (partitioned by month)
CREATE TABLE bmc_transactional.invoices (
    invoice_id BIGSERIAL PRIMARY KEY,
    invoice_number VARCHAR(100) NOT NULL,
    invoice_date DATE NOT NULL,
    document_type VARCHAR(20) NOT NULL, -- 'PDF', 'IMAGE', 'XML'
    document_path VARCHAR(500),
    ocr_confidence DECIMAL(5,2), -- OCR accuracy percentage
    processing_status VARCHAR(20) DEFAULT 'PENDING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) PARTITION BY RANGE (invoice_date);

-- Invoice items
CREATE TABLE bmc_transactional.invoice_items (
    item_id BIGSERIAL PRIMARY KEY,
    invoice_id BIGINT REFERENCES bmc_transactional.invoices(invoice_id),
    product_id BIGINT REFERENCES bmc_transactional.products(product_id),
    quantity DECIMAL(15,4) NOT NULL,
    unit_price DECIMAL(15,4) NOT NULL,
    total_amount DECIMAL(15,4) NOT NULL,
    validation_status VARCHAR(20) DEFAULT 'PENDING'
);

-- Commissions
CREATE TABLE bmc_transactional.commissions (
    commission_id BIGSERIAL PRIMARY KEY,
    invoice_id BIGINT REFERENCES bmc_transactional.invoices(invoice_id),
    commission_rate DECIMAL(8,6) NOT NULL,
    commission_amount DECIMAL(15,4) NOT NULL,
    calculation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    business_rule_version VARCHAR(20) NOT NULL
);
```

#### Analytical Layer - Redshift
```sql
-- Data Warehouse Schema
CREATE SCHEMA bmc_analytics;

-- Fact table for commissions
CREATE TABLE bmc_analytics.fact_commissions (
    commission_key BIGINT IDENTITY(1,1) PRIMARY KEY,
    invoice_key BIGINT NOT NULL,
    product_key BIGINT NOT NULL,
    date_key INTEGER NOT NULL,
    commission_amount DECIMAL(15,4) NOT NULL,
    commission_rate DECIMAL(8,6) NOT NULL,
    quantity DECIMAL(15,4) NOT NULL,
    total_invoice_amount DECIMAL(15,4) NOT NULL
) DISTKEY(date_key) SORTKEY(date_key);

-- Dimension tables
CREATE TABLE bmc_analytics.dim_products (
    product_key BIGINT IDENTITY(1,1) PRIMARY KEY,
    product_code VARCHAR(50) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    dian_classification VARCHAR(20) NOT NULL,
    category_name VARCHAR(100) NOT NULL
) DISTSTYLE ALL;

CREATE TABLE bmc_analytics.dim_time (
    date_key INTEGER PRIMARY KEY,
    full_date DATE NOT NULL,
    year INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    week_of_year INTEGER NOT NULL
) DISTSTYLE ALL;
```

#### Caching Layer - ElastiCache Redis
```yaml
Cache Strategy:
  Product Lookups:
    TTL: 24 hours
    Pattern: "product:{product_code}"
    Size: ~2GB for 60M products metadata
  
  DIAN Classifications:
    TTL: 7 days
    Pattern: "dian:{classification_code}"
    Size: ~100MB
  
  User Sessions:
    TTL: 30 minutes
    Pattern: "session:{user_id}"
    Size: ~10MB total
```

### Database Performance Optimization

#### Indexing Strategy
```sql
-- Products table indexes
CREATE INDEX idx_products_code ON bmc_transactional.products(product_code);
CREATE INDEX idx_products_dian ON bmc_transactional.products(dian_classification);
CREATE INDEX idx_products_category ON bmc_transactional.products(category_id);

-- Invoices table indexes
CREATE INDEX idx_invoices_date ON bmc_transactional.invoices(invoice_date);
CREATE INDEX idx_invoices_status ON bmc_transactional.invoices(processing_status);
CREATE INDEX idx_invoices_number ON bmc_transactional.invoices(invoice_number);

-- Composite indexes for common queries
CREATE INDEX idx_invoice_items_lookup ON bmc_transactional.invoice_items(invoice_id, product_id);
```

#### Partitioning Strategy
```sql
-- Monthly partitions for invoices (last 24 months + future 12 months)
CREATE TABLE bmc_transactional.invoices_2024_01 PARTITION OF bmc_transactional.invoices
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE bmc_transactional.invoices_2024_02 PARTITION OF bmc_transactional.invoices
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
-- ... continue for all months
```

## Integraciones con Plataformas

### AWS Services Integration

#### Document Processing Pipeline
```yaml
S3 Bucket Structure:
  - bmc-documents-raw/
    - invoices/images/
    - invoices/pdfs/
    - certificates/generated/
  
  - bmc-documents-processed/
    - ocr-results/
    - validated-documents/
    - archived/

Textract Integration:
  - Async processing for large documents
  - Confidence threshold: 95%
  - Custom forms analysis for invoice structure
  - Multi-language support (Spanish)

Lambda Functions:
  - document-preprocessor
  - ocr-processor
  - validation-engine
  - format-converter
```

#### Event-Driven Architecture
```yaml
EventBridge Rules:
  - invoice.uploaded → trigger OCR processing
  - invoice.processed → trigger validation
  - validation.completed → trigger commission calculation
  - commission.calculated → trigger certificate generation

SQS Queues:
  - invoice-processing-queue (FIFO)
  - ocr-processing-queue (Standard)
  - notification-queue (Standard)
  - dead-letter-queue (Error handling)

SNS Topics:
  - invoice-events
  - system-alerts
  - user-notifications
```

### External System Integrations

#### SFTP Integration - AWS Transfer Family
```yaml
Configuration:
  Protocol: SFTP
  Identity Provider: Service Managed
  Endpoint Type: VPC
  Security: VPC Security Groups + NACLs

Directory Structure:
  /incoming/
    - daily-reports/
    - regulatory-filings/
  /outgoing/
    - commission-reports/
    - compliance-documents/
  /archive/
    - processed-files/

Automation:
  - Lambda trigger on file upload
  - Automatic file validation
  - Processing status notifications
  - Archive after 30 days
```

#### DIAN API Integration
```yaml
Authentication: OAuth 2.0 + Client Credentials
Rate Limiting: 1000 requests/hour
Retry Strategy: Exponential backoff
Endpoints:
  - /classification/validate
  - /products/lookup
  - /compliance/check

Error Handling:
  - Circuit breaker pattern
  - Fallback to cached data
  - Manual review queue for failures
```

#### Email Service - Amazon SES
```yaml
Configuration:
  Domain: bmc.gov.co (verified)
  DKIM: Enabled
  Bounce/Complaint Handling: Configured

Templates:
  - certificate-delivery
  - processing-notification
  - error-alert
  - compliance-report

Delivery:
  - Immediate: Critical alerts
  - Batched: Daily reports
  - Scheduled: Weekly summaries
```

### Security & Compliance Integration

#### IAM Roles & Policies
```yaml
Service Roles:
  - BMC-InvoiceService-Role
  - BMC-ProductService-Role
  - BMC-OCRService-Role
  - BMC-DataAccess-Role

User Roles:
  - BMC-Admin (full access)
  - BMC-Operator (read/write invoices)
  - BMC-Viewer (read-only reports)
  - BMC-External (SFTP access only)

Policies:
  - Least privilege principle
  - Resource-based permissions
  - Time-based access (business hours)
  - IP restriction for admin access
```

#### Monitoring & Compliance
```yaml
CloudTrail:
  - All API calls logged
  - Data events for S3 buckets
  - Management events for all services

CloudWatch:
  - Custom metrics for business KPIs
  - Log aggregation from all services
  - Real-time dashboards
  - Automated alerting

Compliance:
  - Data residency: Colombia region only
  - Encryption: AES-256 at rest, TLS 1.3 in transit
  - Audit trail: 7-year retention
  - Access logging: All data access recorded
```

## Cronograma de Implementación

### Fase 1: Fundación (Semanas 1-8)
- Setup AWS environment
- Database migration (60M products)
- Product Service implementation
- Basic API Gateway setup

### Fase 2: Procesamiento (Semanas 9-16)
- OCR Service implementation
- Invoice Service development
- Document processing pipeline
- Textract integration

### Fase 3: Lógica de Negocio (Semanas 17-22)
- Commission Service
- Validation Service
- Business rules engine
- Step Functions workflows

### Fase 4: Integración (Semanas 23-26)
- Certificate Service
- SFTP Gateway setup
- Email service integration
- Frontend migration

### Fase 5: Optimización (Semanas 27-30)
- Performance tuning
- Security hardening
- Compliance validation
- Go-live preparation

## Métricas de Éxito

### Performance KPIs
- OCR Processing: <5 segundos (imágenes), <3 segundos (PDFs)
- Product Lookup: <500ms (60M records)
- Invoice Processing: <3 segundos (individual), <30 minutos (lotes)
- System Availability: >99.9%

### Business KPIs
- OCR Accuracy: >95%
- Processing Throughput: 10,000 invoices/hour
- Compliance Rate: 100% DIAN validation
- User Satisfaction: >4.5/5.0
