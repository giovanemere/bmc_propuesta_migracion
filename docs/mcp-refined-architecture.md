# MCP Refined Architecture - Modelo Refinado para Diagramas Profesionales

## Contexto Refinado del Sistema

### Información del Proyecto
```yaml
project:
  name: "BMC AWS Platform"
  description: "Bolsa Mercantil de Colombia - 60M Products Platform"
  version: "2.0.0"
  environment: "production"
  region: "us-east-1"
  
architecture_style: "microservices"
deployment_pattern: "blue_green"
scaling_strategy: "auto_horizontal"
```

### Configuración Visual de Diagramas
```yaml
diagram_config:
  layout:
    direction: "TB"  # Top to Bottom
    spacing: 
      cluster: 20
      node: 15
      edge: 10
    
  colors:
    primary: "#232F3E"      # AWS Dark Blue
    secondary: "#FF9900"    # AWS Orange
    success: "#4CAF50"      # Green
    warning: "#FF9800"      # Orange
    danger: "#F44336"       # Red
    info: "#2196F3"         # Blue
    
  fonts:
    title: 16
    cluster: 12
    service: 10
    label: 8
    
  icons:
    size: "medium"          # small, medium, large
    style: "official"       # official, simple, detailed
```

### Arquitectura de Red Detallada
```yaml
network_architecture:
  vpc:
    name: "bmc-production-vpc"
    cidr: "10.0.0.0/16"
    
    availability_zones:
      - name: "us-east-1a"
        subnets:
          public: "10.0.1.0/24"
          private: "10.0.10.0/24"
          isolated: "10.0.20.0/24"
      - name: "us-east-1b"
        subnets:
          public: "10.0.2.0/24"
          private: "10.0.11.0/24"
          isolated: "10.0.21.0/24"
    
    gateways:
      internet_gateway: true
      nat_gateways:
        - az: "us-east-1a"
          subnet: "public"
        - az: "us-east-1b"
          subnet: "public"
    
    routing:
      public_routes:
        - destination: "0.0.0.0/0"
          target: "internet_gateway"
      private_routes:
        - destination: "0.0.0.0/0"
          target: "nat_gateway"
```

### Microservicios con Configuración Detallada
```yaml
microservices:
  invoice_service:
    # Compute Configuration
    compute:
      platform: "ecs_fargate"
      cpu: 2048
      memory: 4096
      
    # Container Configuration
    container:
      image: "bmc/invoice-service:v2.1.0"
      port: 8000
      health_check:
        path: "/health"
        interval: 30
        timeout: 5
        retries: 3
    
    # Scaling Configuration
    scaling:
      min_capacity: 2
      max_capacity: 10
      target_cpu: 70
      target_memory: 80
      scale_out_cooldown: 300
      scale_in_cooldown: 300
    
    # Network Configuration
    network:
      subnets: "private"
      security_groups:
        - "invoice_service_sg"
        - "common_app_sg"
      load_balancer:
        type: "application"
        scheme: "internal"
        listeners:
          - port: 80
            protocol: "HTTP"
            target_port: 8000
    
    # Environment Variables
    environment:
      LOG_LEVEL: "INFO"
      DATABASE_URL: "${rds_primary.endpoint}"
      CACHE_URL: "${redis_cluster.endpoint}"
      OCR_QUEUE_URL: "${sqs_ocr_queue.url}"
      
    # Dependencies
    dependencies:
      - service: "rds_primary"
        type: "database"
      - service: "redis_cluster"
        type: "cache"
      - service: "sqs_ocr_queue"
        type: "queue"
    
    # Business Metrics
    business_metrics:
      throughput: "1000 invoices/hour"
      response_time: "<3 seconds"
      accuracy: ">99.5%"
      
  product_service:
    # Compute Configuration
    compute:
      platform: "ecs_fargate"
      cpu: 4096
      memory: 8192
      
    # Container Configuration
    container:
      image: "bmc/product-service:v2.1.0"
      port: 8001
      health_check:
        path: "/health"
        interval: 30
        timeout: 5
        retries: 3
    
    # Scaling Configuration
    scaling:
      min_capacity: 3
      max_capacity: 15
      target_cpu: 70
      target_memory: 80
      
    # Data Configuration
    data:
      primary_dataset: "60M products"
      cache_strategy: "write_through"
      cache_ttl: "24h"
      
    # Performance
    performance:
      lookup_time: "<500ms"
      cache_hit_ratio: ">95%"
      concurrent_users: "10000"
      
  ocr_service:
    # Compute Configuration
    compute:
      platform: "ecs_fargate"
      cpu: 2048
      memory: 4096
      
    # AI/ML Configuration
    ai_ml:
      ocr_engine: "textract"
      accuracy_target: ">95%"
      processing_time: "<5s"
      supported_formats:
        - "PDF"
        - "JPEG"
        - "PNG"
        - "TIFF"
      
    # Integration
    integration:
      input_source: "s3_documents"
      output_destination: "s3_processed"
      notification_topic: "ocr_completed"
      
  commission_service:
    compute:
      platform: "ecs_fargate"
      cpu: 1024
      memory: 2048
      
    business_logic:
      calculation_engine: "rules_based"
      commission_types:
        - "percentage"
        - "fixed"
        - "tiered"
      processing_frequency: "real_time"
      
  certificate_service:
    compute:
      platform: "ecs_fargate"
      cpu: 1024
      memory: 2048
      
    document_generation:
      format: "PDF"
      template_engine: "jinja2"
      digital_signature: true
      compliance: "DIAN_approved"
```

### Servicios AWS con Configuración Detallada
```yaml
aws_services:
  # Database Services
  rds_primary:
    type: "rds"
    engine: "postgresql"
    version: "14.9"
    instance_class: "db.r6g.2xlarge"
    
    # Storage Configuration
    storage:
      allocated: 1000
      max_allocated: 5000
      storage_type: "gp3"
      iops: 12000
      
    # High Availability
    high_availability:
      multi_az: true
      backup_retention: 35
      backup_window: "03:00-04:00"
      maintenance_window: "sun:04:00-sun:05:00"
      
    # Performance
    performance:
      performance_insights: true
      monitoring_interval: 60
      
    # Security
    security:
      encryption_at_rest: true
      encryption_in_transit: true
      kms_key: "alias/rds-encryption"
      
    # Network
    network:
      subnet_group: "isolated"
      security_groups:
        - "rds_sg"
      port: 5432
      
    # Monitoring
    monitoring:
      cloudwatch_logs: true
      slow_query_log: true
      
  redis_cluster:
    type: "elasticache"
    engine: "redis"
    version: "7.0"
    node_type: "cache.r6g.xlarge"
    
    # Cluster Configuration
    cluster:
      num_nodes: 3
      cluster_mode: true
      automatic_failover: true
      
    # Performance
    performance:
      ttl_default: "24h"
      max_memory_policy: "allkeys-lru"
      
    # Security
    security:
      encryption_at_rest: true
      encryption_in_transit: true
      auth_token: true
      
  s3_documents:
    type: "s3"
    
    # Storage Configuration
    storage:
      storage_class: "intelligent_tiering"
      versioning: true
      
    # Lifecycle Management
    lifecycle:
      rules:
        - name: "archive_old_documents"
          transition_days: 90
          target_class: "glacier"
        - name: "delete_temp_files"
          expiration_days: 7
          prefix: "temp/"
          
    # Security
    security:
      encryption: "aws:kms"
      kms_key: "alias/s3-encryption"
      public_access_block: true
      
    # Performance
    performance:
      transfer_acceleration: true
      multipart_threshold: "64MB"
      
  api_gateway:
    type: "api_gateway"
    api_type: "REST"
    
    # Configuration
    configuration:
      throttling:
        rate_limit: 1000
        burst_limit: 2000
      
      # Caching
      caching:
        enabled: true
        ttl: 300
        
      # CORS
      cors:
        enabled: true
        origins: ["https://bmc.com.co"]
        methods: ["GET", "POST", "PUT", "DELETE"]
        
    # Security
    security:
      authentication: "cognito"
      authorization: "custom"
      api_keys: true
      
    # Monitoring
    monitoring:
      logging_level: "INFO"
      metrics_enabled: true
      tracing_enabled: true
      
  cloudfront_cdn:
    type: "cloudfront"
    
    # Origins
    origins:
      - domain: "${api_gateway.domain}"
        path: "/api/*"
        origin_type: "api"
      - domain: "${s3_static.domain}"
        path: "/static/*"
        origin_type: "s3"
        
    # Caching Behavior
    caching:
      default_ttl: 86400
      max_ttl: 31536000
      compress: true
      
    # Security
    security:
      waf_enabled: true
      ssl_certificate: "*.bmc.com.co"
      security_headers: true
      
    # Performance
    performance:
      price_class: "PriceClass_100"
      http_version: "http2"
      
  textract_ocr:
    type: "textract"
    
    # Configuration
    configuration:
      features:
        - "TEXT"
        - "FORMS"
        - "TABLES"
        - "SIGNATURES"
      
      # Performance
      performance:
        confidence_threshold: 95
        async_processing: true
        
      # Integration
      integration:
        input_bucket: "${s3_documents.bucket}"
        output_bucket: "${s3_processed.bucket}"
        notification_topic: "${sns_ocr.topic}"
```

### Configuración de Integración y Eventos
```yaml
integration_layer:
  event_bridge:
    type: "eventbridge"
    
    # Event Bus
    event_bus:
      name: "bmc-production-bus"
      
    # Rules
    rules:
      invoice_processing:
        source: "bmc.invoice"
        detail_type: "Invoice Created"
        targets:
          - arn: "${sqs_ocr_queue.arn}"
            input_transformer:
              input_paths:
                invoice_id: "$.detail.invoiceId"
              input_template: '{"invoiceId": "<invoice_id>"}'
              
      ocr_completed:
        source: "bmc.ocr"
        detail_type: "OCR Processing Completed"
        targets:
          - arn: "${lambda_classifier.arn}"
          - arn: "${sns_notifications.arn}"
          
  sqs_queues:
    ocr_queue:
      type: "sqs"
      queue_type: "FIFO"
      
      # Configuration
      configuration:
        visibility_timeout: 300
        message_retention: 1209600
        max_receive_count: 3
        
      # Dead Letter Queue
      dlq:
        enabled: true
        max_receive_count: 3
        
    audit_queue:
      type: "sqs"
      queue_type: "standard"
      
      # Batch Processing
      batch:
        batch_size: 10
        batch_window: 5
        
  sns_topics:
    notifications:
      type: "sns"
      
      # Subscriptions
      subscriptions:
        - protocol: "email"
          endpoint: "operations@bmc.com.co"
        - protocol: "sms"
          endpoint: "+57300123456"
        - protocol: "lambda"
          endpoint: "${lambda_notifier.arn}"
```

### Configuración de Monitoreo Avanzado
```yaml
monitoring_observability:
  cloudwatch:
    type: "cloudwatch"
    
    # Custom Metrics
    custom_metrics:
      business_metrics:
        - name: "InvoicesProcessedPerHour"
          namespace: "BMC/Business"
          unit: "Count"
          
        - name: "OCRAccuracyRate"
          namespace: "BMC/Quality"
          unit: "Percent"
          
        - name: "ProductLookupLatency"
          namespace: "BMC/Performance"
          unit: "Milliseconds"
          
    # Dashboards
    dashboards:
      operational:
        name: "BMC-Operational-Dashboard"
        widgets:
          - type: "metric"
            title: "Service Health"
            metrics: ["CPUUtilization", "MemoryUtilization"]
          - type: "log"
            title: "Error Logs"
            log_group: "/aws/ecs/bmc-services"
            
      business:
        name: "BMC-Business-Dashboard"
        widgets:
          - type: "metric"
            title: "Invoice Processing"
            metrics: ["InvoicesProcessedPerHour"]
          - type: "metric"
            title: "OCR Quality"
            metrics: ["OCRAccuracyRate"]
            
    # Alarms
    alarms:
      critical:
        - name: "HighErrorRate"
          metric: "ErrorRate"
          threshold: 5
          comparison: "GreaterThanThreshold"
          evaluation_periods: 2
          
        - name: "DatabaseConnectionFailure"
          metric: "DatabaseConnections"
          threshold: 0
          comparison: "LessThanThreshold"
          evaluation_periods: 1
          
      warning:
        - name: "HighCPUUtilization"
          metric: "CPUUtilization"
          threshold: 80
          comparison: "GreaterThanThreshold"
          evaluation_periods: 3
```

### Configuración de Seguridad Detallada
```yaml
security_configuration:
  cognito_auth:
    type: "cognito"
    
    # User Pool
    user_pool:
      name: "bmc-users"
      
      # Password Policy
      password_policy:
        min_length: 12
        require_uppercase: true
        require_lowercase: true
        require_numbers: true
        require_symbols: true
        
      # MFA
      mfa:
        configuration: "OPTIONAL"
        methods: ["SMS", "TOTP"]
        
      # Account Recovery
      account_recovery:
        methods: ["verified_email", "verified_phone_number"]
        
    # Identity Pool
    identity_pool:
      name: "bmc-identity"
      allow_unauthenticated: false
      
  waf_protection:
    type: "waf"
    
    # Web ACL
    web_acl:
      name: "bmc-protection"
      scope: "CLOUDFRONT"
      
      # Rules
      rules:
        rate_limiting:
          type: "rate_based"
          limit: 2000
          action: "block"
          
        sql_injection:
          type: "managed"
          rule_group: "AWSManagedRulesCommonRuleSet"
          action: "block"
          
        geo_blocking:
          type: "geo_match"
          countries: ["CN", "RU", "KP"]
          action: "block"
          
        ip_whitelist:
          type: "ip_set"
          addresses: ["203.0.113.0/24"]
          action: "allow"
          
  kms_encryption:
    keys:
      rds_key:
        alias: "bmc-rds-encryption"
        description: "RDS encryption key"
        rotation: true
        
      s3_key:
        alias: "bmc-s3-encryption"
        description: "S3 encryption key"
        rotation: true
        
      secrets_key:
        alias: "bmc-secrets-encryption"
        description: "Secrets Manager encryption key"
        rotation: true
```

### Métricas de Rendimiento y KPIs
```yaml
performance_kpis:
  response_times:
    api_gateway: 
      target: "200ms"
      p95_target: "500ms"
      p99_target: "1000ms"
      
    product_lookup:
      target: "300ms"
      p95_target: "500ms"
      cache_hit_target: "50ms"
      
    invoice_processing:
      target: "3000ms"
      p95_target: "5000ms"
      
    ocr_processing:
      target: "4000ms"
      p95_target: "6000ms"
      
  throughput:
    invoices_per_hour: 10000
    peak_invoices_per_hour: 30000
    concurrent_users: 10000
    api_requests_per_second: 1000
    
  availability:
    system_sla: 99.9
    database_sla: 99.95
    api_sla: 99.9
    
  business_metrics:
    ocr_accuracy: 95.5
    data_validation_accuracy: 99.8
    commission_calculation_accuracy: 99.99
    
  cost_metrics:
    monthly_budget: 8650
    cost_per_invoice: 0.0009
    cost_per_product_lookup: 0.000001
    cost_optimization_target: 15
```

### Configuración de Despliegue
```yaml
deployment_configuration:
  strategy:
    type: "blue_green"
    
    # Blue/Green Settings
    blue_green:
      health_check_grace_period: 300
      rollback_on_failure: true
      
      # Traffic Shifting
      traffic_shifting:
        type: "linear"
        increment: 10
        interval: 300
        
  environments:
    production:
      region: "us-east-1"
      availability_zones: ["us-east-1a", "us-east-1b"]
      
    staging:
      region: "us-east-1"
      availability_zones: ["us-east-1a"]
      
  pipeline:
    stages:
      - name: "source"
        source: "github"
        
      - name: "build"
        actions: ["test", "security_scan", "build_image"]
        
      - name: "deploy_staging"
        environment: "staging"
        
      - name: "integration_tests"
        tests: ["api_tests", "load_tests", "security_tests"]
        
      - name: "deploy_production"
        environment: "production"
        approval_required: true
```

Este MCP refinado incluye:

1. **Configuración visual detallada** para diagramas
2. **Arquitectura de red completa** con VPC, subnets, routing
3. **Microservicios con configuración exhaustiva**
4. **Servicios AWS con parámetros específicos**
5. **Integración y eventos detallados**
6. **Monitoreo y observabilidad avanzados**
7. **Seguridad granular**
8. **KPIs y métricas específicas**
9. **Configuración de despliegue completa**

¿Quieres que ahora mejore el generador de diagramas para usar toda esta información refinada?
