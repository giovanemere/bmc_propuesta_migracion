# MCP AWS Model - Modelo Transversal para Arquitecturas AWS

## Contexto del Modelo

### Propósito
Modelo MCP genérico y reutilizable para definir arquitecturas AWS que pueden ser convertidas automáticamente en diagramas profesionales. Sirve como fuente de verdad única para documentación, implementación y evolución de arquitecturas cloud.

### Alcance
- **Servicios AWS**: Compute, Storage, Network, Security, AI/ML, Integration, Monitoring
- **Patrones**: Microservicios, Event-Driven, Serverless, Data Lakes
- **Escalabilidad**: Auto-scaling, Multi-AZ, Cross-Region
- **Seguridad**: IAM, Encryption, Compliance, Monitoring

## Estructura del Modelo MCP

### 1. Información General del Proyecto
```yaml
project:
  name: "Project Name"
  description: "Project description"
  version: "1.0.0"
  environment: "production"  # dev, staging, production
  region: "us-east-1"
  
metadata:
  owner: "Team Name"
  contact: "team@company.com"
  created: "2024-01-01"
  updated: "2024-01-01"
  
tags:
  project: "project-name"
  environment: "production"
  team: "platform"
  cost-center: "engineering"
```

### 2. Configuración de Microservicios
```yaml
microservices:
  service_name:
    # Compute Configuration
    cpu: 2048                    # CPU units (1024 = 1 vCPU)
    memory: 4096                 # Memory in MB
    port: 8000                   # Container port
    
    # Scaling Configuration
    min_capacity: 2              # Minimum instances
    max_capacity: 10             # Maximum instances
    target_cpu: 70               # CPU target for scaling
    target_memory: 80            # Memory target for scaling
    
    # Health Check
    health_check: "/health"      # Health check endpoint
    health_timeout: 30           # Health check timeout (seconds)
    
    # Environment Variables
    environment:
      LOG_LEVEL: "INFO"
      DATABASE_URL: "${rds.endpoint}"
      CACHE_URL: "${redis.endpoint}"
    
    # Dependencies
    depends_on:
      - "database"
      - "cache"
    
    # Networking
    vpc_config:
      subnets: "private"         # private, public, isolated
      security_groups:
        - "app_sg"
        - "database_sg"
```

### 3. Servicios AWS de Infraestructura
```yaml
services:
  # Database Services
  database:
    type: "rds"
    engine: "postgresql"         # postgresql, mysql, mariadb
    version: "14.9"
    instance_class: "db.r6g.large"
    allocated_storage: 100       # GB
    max_allocated_storage: 1000  # GB
    multi_az: true
    backup_retention: 7          # days
    deletion_protection: true
    
    # Performance
    performance_insights: true
    monitoring_interval: 60
    
    # Security
    encryption: true
    kms_key: "alias/rds-key"
    
    # Network
    vpc_security_groups:
      - "database_sg"
    subnet_group: "private"
  
  # Cache Services  
  cache:
    type: "elasticache"
    engine: "redis"              # redis, memcached
    version: "7.0"
    node_type: "cache.r6g.large"
    num_nodes: 3
    cluster_mode: true
    
    # Configuration
    parameter_group: "default.redis7"
    ttl_default: "24h"
    
    # Security
    encryption_at_rest: true
    encryption_in_transit: true
    auth_token: true
    
    # Network
    subnet_group: "private"
    security_groups:
      - "cache_sg"
  
  # Storage Services
  storage:
    type: "s3"
    storage_class: "intelligent_tiering"  # standard, ia, glacier
    versioning: true
    encryption: "AES256"         # AES256, aws:kms
    
    # Lifecycle
    lifecycle_rules:
      - name: "archive_old_data"
        transition_days: 30
        target_class: "glacier"
    
    # Access Control
    public_access_block: true
    bucket_policy: "private"
    
    # Features
    intelligent_tiering: true
    cross_region_replication: true
    target_region: "us-west-2"
  
  # API Gateway
  api_gateway:
    type: "api_gateway"
    api_type: "REST"             # REST, HTTP, WebSocket
    
    # Configuration
    throttling:
      rate_limit: 1000           # requests per second
      burst_limit: 2000
    
    # Security
    authentication: "cognito"    # cognito, iam, api_key
    cors_enabled: true
    
    # Monitoring
    logging_level: "INFO"        # OFF, ERROR, INFO
    metrics_enabled: true
    tracing_enabled: true
  
  # Content Delivery
  cdn:
    type: "cloudfront"
    
    # Origins
    origins:
      - domain: "${api_gateway.domain}"
        path: "/api/*"
      - domain: "${s3.domain}"
        path: "/static/*"
    
    # Caching
    default_ttl: 86400           # seconds
    max_ttl: 31536000           # seconds
    
    # Security
    waf_enabled: true
    ssl_certificate: "*.domain.com"
    
    # Geographic Restrictions
    geo_restriction: "none"      # none, whitelist, blacklist
```

### 4. Servicios de Seguridad
```yaml
security:
  # Authentication
  authentication:
    type: "cognito"
    
    # User Pool Configuration
    user_pool:
      password_policy:
        min_length: 8
        require_uppercase: true
        require_lowercase: true
        require_numbers: true
        require_symbols: true
      
      # MFA Configuration
      mfa_configuration: "OPTIONAL"  # OFF, ON, OPTIONAL
      mfa_types:
        - "SMS"
        - "TOTP"
    
    # Identity Pool
    identity_pool:
      allow_unauthenticated: false
      
  # Web Application Firewall
  waf:
    type: "waf"
    
    # Rules
    rules:
      - name: "rate_limiting"
        type: "rate_based"
        limit: 2000
        action: "block"
      
      - name: "sql_injection"
        type: "managed"
        rule_group: "AWSManagedRulesCommonRuleSet"
        action: "block"
      
      - name: "geo_blocking"
        type: "geo_match"
        countries: ["CN", "RU"]
        action: "block"
  
  # Key Management
  kms:
    keys:
      - alias: "rds-key"
        description: "RDS encryption key"
        rotation: true
      
      - alias: "s3-key" 
        description: "S3 encryption key"
        rotation: true
```

### 5. Servicios de AI/ML
```yaml
ai_ml:
  # OCR Service
  ocr:
    type: "textract"
    
    # Configuration
    features:
      - "TEXT"
      - "FORMS"
      - "TABLES"
    
    # Performance
    confidence_threshold: 95     # percentage
    async_processing: true
    
    # Integration
    input_bucket: "${storage.bucket_name}"
    output_bucket: "${storage.bucket_name}"
    notification_topic: "${notifications.ocr_topic}"
  
  # NLP Service (Future)
  nlp:
    type: "comprehend"
    
    # Features
    features:
      - "sentiment"
      - "entities"
      - "key_phrases"
    
    # Languages
    languages:
      - "es"  # Spanish
      - "en"  # English
```

### 6. Servicios de Integración
```yaml
integration:
  # Event Bus
  event_bus:
    type: "eventbridge"
    
    # Rules
    rules:
      - name: "invoice_processing"
        source: "invoice.service"
        detail_type: "Invoice Created"
        targets:
          - "ocr_queue"
          - "notification_topic"
      
      - name: "ocr_completed"
        source: "ocr.service"
        detail_type: "OCR Completed"
        targets:
          - "product_service"
          - "audit_queue"
  
  # Message Queues
  queues:
    ocr_queue:
      type: "sqs"
      queue_type: "FIFO"          # standard, FIFO
      
      # Configuration
      visibility_timeout: 300     # seconds
      message_retention: 1209600  # seconds (14 days)
      max_receive_count: 3
      
      # Dead Letter Queue
      dlq_enabled: true
      dlq_max_receive_count: 3
    
    audit_queue:
      type: "sqs"
      queue_type: "standard"
      
      # Batch Processing
      batch_size: 10
      batch_window: 5             # seconds
  
  # Notifications
  notifications:
    ocr_topic:
      type: "sns"
      
      # Subscriptions
      subscriptions:
        - protocol: "email"
          endpoint: "team@company.com"
        - protocol: "sqs"
          endpoint: "${queues.audit_queue.arn}"
    
    alerts_topic:
      type: "sns"
      
      # Subscriptions
      subscriptions:
        - protocol: "sms"
          endpoint: "+1234567890"
```

### 7. Monitoreo y Observabilidad
```yaml
monitoring:
  # Metrics and Logs
  cloudwatch:
    type: "cloudwatch"
    
    # Log Groups
    log_groups:
      - name: "/aws/ecs/microservices"
        retention_days: 30
      - name: "/aws/lambda/functions"
        retention_days: 14
    
    # Custom Metrics
    custom_metrics:
      - name: "business.invoices.processed"
        namespace: "BMC/Business"
        unit: "Count"
      
      - name: "business.ocr.accuracy"
        namespace: "BMC/Quality"
        unit: "Percent"
    
    # Alarms
    alarms:
      - name: "high_cpu_utilization"
        metric: "CPUUtilization"
        threshold: 80
        comparison: "GreaterThanThreshold"
        evaluation_periods: 2
        actions:
          - "${notifications.alerts_topic}"
      
      - name: "high_error_rate"
        metric: "ErrorRate"
        threshold: 5
        comparison: "GreaterThanThreshold"
        evaluation_periods: 1
        actions:
          - "${notifications.alerts_topic}"
  
  # Distributed Tracing (Future)
  tracing:
    type: "xray"
    
    # Configuration
    sampling_rate: 0.1           # 10% of requests
    service_map: true
    
    # Integration
    services:
      - "api_gateway"
      - "microservices"
      - "lambda_functions"
```

### 8. Métricas y KPIs
```yaml
metrics:
  # Performance Metrics
  performance:
    response_time:
      target: 500                # milliseconds
      p95_target: 1000          # milliseconds
      measurement: "average"
    
    throughput:
      target: 1000              # requests per second
      peak_target: 5000         # requests per second
      measurement: "sustained"
    
    availability:
      target: 99.9              # percentage
      measurement: "monthly"
      downtime_budget: 43       # minutes per month
  
  # Business Metrics
  business:
    processing_capacity:
      invoices_per_hour: 10000
      documents_per_day: 240000
      peak_multiplier: 3
    
    accuracy:
      ocr_accuracy: 95          # percentage
      data_validation: 99.5     # percentage
      false_positive_rate: 0.1  # percentage
  
  # Cost Metrics
  cost:
    monthly_budget: 8650        # USD
    cost_per_invoice: 0.0009    # USD
    cost_per_gb_storage: 0.023  # USD
    
    # Cost Optimization
    reserved_instances: 60      # percentage
    spot_instances: 20          # percentage
    s3_intelligent_tiering: 80  # percentage
```

### 9. Configuración de Red
```yaml
network:
  # VPC Configuration
  vpc:
    cidr_block: "10.0.0.0/16"
    enable_dns_hostnames: true
    enable_dns_support: true
    
    # Subnets
    subnets:
      public:
        - cidr: "10.0.1.0/24"
          az: "us-east-1a"
        - cidr: "10.0.2.0/24"
          az: "us-east-1b"
      
      private:
        - cidr: "10.0.10.0/24"
          az: "us-east-1a"
        - cidr: "10.0.11.0/24"
          az: "us-east-1b"
      
      isolated:
        - cidr: "10.0.20.0/24"
          az: "us-east-1a"
        - cidr: "10.0.21.0/24"
          az: "us-east-1b"
    
    # Internet Gateway
    internet_gateway: true
    
    # NAT Gateways
    nat_gateways:
      - subnet: "public-1a"
      - subnet: "public-1b"
  
  # Security Groups
  security_groups:
    app_sg:
      description: "Application security group"
      ingress:
        - protocol: "tcp"
          port: 80
          source: "0.0.0.0/0"
        - protocol: "tcp"
          port: 443
          source: "0.0.0.0/0"
      egress:
        - protocol: "all"
          destination: "0.0.0.0/0"
    
    database_sg:
      description: "Database security group"
      ingress:
        - protocol: "tcp"
          port: 5432
          source: "${app_sg}"
      egress: []
```

### 10. Configuración de Despliegue
```yaml
deployment:
  # CI/CD Configuration
  pipeline:
    source: "github"
    repository: "company/project"
    branch: "main"
    
    # Stages
    stages:
      - name: "build"
        actions:
          - "test"
          - "security_scan"
          - "build_image"
      
      - name: "deploy_staging"
        environment: "staging"
        approval_required: false
      
      - name: "deploy_production"
        environment: "production"
        approval_required: true
  
  # Blue/Green Deployment
  deployment_strategy:
    type: "blue_green"
    
    # Configuration
    health_check_grace_period: 300  # seconds
    rollback_on_failure: true
    
    # Traffic Shifting
    traffic_shifting:
      type: "linear"
      increment: 10               # percentage
      interval: 5                 # minutes
```

## Uso del Modelo

### Validación del Modelo
```yaml
validation:
  required_sections:
    - "project"
    - "microservices"
    - "services"
    - "metrics"
  
  optional_sections:
    - "security"
    - "ai_ml"
    - "integration"
    - "monitoring"
    - "network"
    - "deployment"
  
  constraints:
    - "microservices must have at least 1 service"
    - "services.database is required"
    - "metrics.performance is required"
```

### Extensibilidad
```yaml
extensions:
  custom_services:
    - type: "custom_service"
      implementation: "custom_generator.py"
  
  custom_metrics:
    - namespace: "Custom/Business"
      metrics: ["custom.metric.name"]
  
  custom_integrations:
    - type: "third_party_api"
      configuration: "external_config.json"
```

---

**Este modelo MCP AWS sirve como base para generar diagramas profesionales y exactos de arquitecturas AWS, facilitando la evolución controlada y documentada de las soluciones cloud.**
