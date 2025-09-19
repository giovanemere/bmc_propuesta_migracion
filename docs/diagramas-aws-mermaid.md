# Diagramas de Arquitectura BMC - AWS con Iconos Mermaid

## 1. Arquitectura General AWS

```mermaid
graph TB
    subgraph "🌐 Internet"
        Users[👥 Usuarios BMC]
        External[🏢 Sistemas Externos]
    end
    
    subgraph "☁️ AWS Cloud"
        subgraph "🔒 Security & Access"
            CloudFront[🌍 CloudFront<br/>CDN]
            WAF[🛡️ AWS WAF<br/>Web Firewall]
            Cognito[🔐 Cognito<br/>Authentication]
        end
        
        subgraph "🚪 API Layer"
            ALB[⚖️ Application<br/>Load Balancer]
            APIGateway[🚪 API Gateway<br/>REST/GraphQL]
        end
        
        subgraph "⚙️ Compute Layer"
            ECS[🐳 ECS Fargate<br/>Microservices]
            Lambda[⚡ Lambda<br/>Serverless Functions]
            StepFunctions[🔄 Step Functions<br/>Workflows]
        end
        
        subgraph "💾 Data Layer"
            RDS[🗄️ RDS PostgreSQL<br/>60M Products]
            Redshift[📊 Redshift<br/>Analytics]
            ElastiCache[⚡ ElastiCache<br/>Redis Cache]
            S3[📦 S3<br/>Document Storage]
        end
        
        subgraph "🔗 Integration Layer"
            EventBridge[⚡ EventBridge<br/>Event Bus]
            SQS[📬 SQS<br/>Message Queue]
            SNS[📢 SNS<br/>Notifications]
            TransferFamily[📁 Transfer Family<br/>SFTP Gateway]
        end
        
        subgraph "🤖 AI/ML Services"
            Textract[👁️ Textract<br/>OCR Service]
            Comprehend[🧠 Comprehend<br/>NLP Analysis]
        end
        
        subgraph "📊 Monitoring"
            CloudWatch[📈 CloudWatch<br/>Monitoring]
            XRay[🔍 X-Ray<br/>Tracing]
            CloudTrail[📋 CloudTrail<br/>Audit Logs]
        end
    end
    
    subgraph "🏛️ External Systems"
        DIAN[🏛️ DIAN API<br/>Tax Authority]
        Email[📧 External Email<br/>SMTP/SES]
    end
    
    Users --> CloudFront
    External --> TransferFamily
    
    CloudFront --> WAF
    WAF --> ALB
    ALB --> APIGateway
    
    APIGateway --> Cognito
    APIGateway --> ECS
    APIGateway --> Lambda
    
    ECS --> RDS
    ECS --> ElastiCache
    ECS --> S3
    Lambda --> Textract
    Lambda --> EventBridge
    
    EventBridge --> SQS
    EventBridge --> SNS
    EventBridge --> StepFunctions
    
    StepFunctions --> Lambda
    Lambda --> Redshift
    
    ECS --> DIAN
    SNS --> Email
    
    CloudWatch --> SNS
    XRay --> CloudWatch
    
    style CloudFront fill:#ff9800
    style APIGateway fill:#4caf50
    style ECS fill:#2196f3
    style RDS fill:#9c27b0
    style S3 fill:#ff5722
    style Textract fill:#e91e63
```

## 2. Microservicios en ECS Fargate

```mermaid
graph TB
    subgraph "🚪 API Gateway"
        Gateway[API Gateway<br/>Central Router]
    end
    
    subgraph "🐳 ECS Fargate Cluster"
        subgraph "📄 Invoice Service"
            InvoiceTask[📄 Invoice Task<br/>2 vCPU, 4GB RAM]
            InvoiceALB[⚖️ Invoice ALB<br/>Load Balancer]
        end
        
        subgraph "🏷️ Product Service"
            ProductTask[🏷️ Product Task<br/>4 vCPU, 8GB RAM]
            ProductALB[⚖️ Product ALB<br/>Load Balancer]
        end
        
        subgraph "👁️ OCR Service"
            OCRTask[👁️ OCR Task<br/>2 vCPU, 4GB RAM]
            OCRALB[⚖️ OCR ALB<br/>Load Balancer]
        end
        
        subgraph "💰 Commission Service"
            CommissionTask[💰 Commission Task<br/>1 vCPU, 2GB RAM]
            CommissionALB[⚖️ Commission ALB<br/>Load Balancer]
        end
        
        subgraph "📜 Certificate Service"
            CertTask[📜 Certificate Task<br/>1 vCPU, 2GB RAM]
            CertALB[⚖️ Certificate ALB<br/>Load Balancer]
        end
    end
    
    subgraph "💾 Data Services"
        RDS[(🗄️ RDS PostgreSQL<br/>Multi-AZ)]
        Redis[(⚡ ElastiCache Redis<br/>Cluster Mode)]
        S3[(📦 S3 Buckets<br/>Documents)]
    end
    
    subgraph "🤖 AWS AI Services"
        Textract[👁️ Amazon Textract<br/>OCR Processing]
    end
    
    subgraph "⚡ Event Processing"
        EventBridge[⚡ EventBridge<br/>Event Router]
        SQS[📬 SQS Queues<br/>FIFO & Standard]
    end
    
    Gateway --> InvoiceALB
    Gateway --> ProductALB
    Gateway --> OCRALB
    Gateway --> CommissionALB
    Gateway --> CertALB
    
    InvoiceALB --> InvoiceTask
    ProductALB --> ProductTask
    OCRALB --> OCRTask
    CommissionALB --> CommissionTask
    CertALB --> CertTask
    
    InvoiceTask --> RDS
    ProductTask --> RDS
    ProductTask --> Redis
    OCRTask --> S3
    OCRTask --> Textract
    
    InvoiceTask --> EventBridge
    OCRTask --> EventBridge
    EventBridge --> SQS
    SQS --> CommissionTask
    
    style InvoiceTask fill:#fff3e0
    style ProductTask fill:#e3f2fd
    style OCRTask fill:#fce4ec
    style CommissionTask fill:#e8f5e8
    style CertTask fill:#f3e5f5
```

## 3. Pipeline de Procesamiento de Documentos

```mermaid
graph TB
    subgraph "📁 Document Input"
        Upload[📤 Document Upload<br/>Web/Mobile/SFTP]
        S3Raw[📦 S3 Raw Bucket<br/>bmc-documents-raw]
    end
    
    subgraph "🔄 Step Functions Workflow"
        StepFunc[🔄 Document Processing<br/>Step Functions]
        
        subgraph "Processing Steps"
            Validate[✅ Validate Document<br/>Lambda Function]
            Preprocess[🖼️ Preprocess Image<br/>Lambda Function]
            OCRExtract[👁️ OCR Extraction<br/>Textract Integration]
            ParseData[📊 Parse Structured Data<br/>Lambda Function]
            ValidateData[✅ Validate Business Rules<br/>Lambda Function]
            MatchProducts[🔍 Match Products<br/>ECS Service Call]
            CalcCommission[💰 Calculate Commission<br/>ECS Service Call]
            GenCertificate[📜 Generate Certificate<br/>Lambda Function]
        end
    end
    
    subgraph "💾 Data Storage"
        S3Processed[📦 S3 Processed<br/>bmc-documents-processed]
        RDS[(🗄️ RDS PostgreSQL<br/>Transaction Data)]
        Redis[(⚡ ElastiCache<br/>Product Cache)]
    end
    
    subgraph "📊 Monitoring & Events"
        CloudWatch[📈 CloudWatch<br/>Metrics & Logs]
        EventBridge[⚡ EventBridge<br/>Event Notifications]
        SNS[📢 SNS<br/>User Notifications]
    end
    
    subgraph "🏛️ External Integration"
        DIAN[🏛️ DIAN API<br/>Product Classification]
        SES[📧 Amazon SES<br/>Email Delivery]
    end
    
    Upload --> S3Raw
    S3Raw --> StepFunc
    
    StepFunc --> Validate
    Validate --> Preprocess
    Preprocess --> OCRExtract
    OCRExtract --> ParseData
    ParseData --> ValidateData
    ValidateData --> MatchProducts
    MatchProducts --> CalcCommission
    CalcCommission --> GenCertificate
    
    OCRExtract --> S3Processed
    ParseData --> RDS
    MatchProducts --> Redis
    MatchProducts --> DIAN
    GenCertificate --> S3Processed
    
    StepFunc --> CloudWatch
    StepFunc --> EventBridge
    EventBridge --> SNS
    SNS --> SES
    
    style StepFunc fill:#ff9800
    style OCRExtract fill:#e91e63
    style MatchProducts fill:#2196f3
    style CalcCommission fill:#4caf50
    style GenCertificate fill:#9c27b0
```

## 4. Arquitectura de Datos Multi-Tier

```mermaid
graph TB
    subgraph "📱 Application Layer"
        WebApp[📱 Web Application<br/>React SPA]
        MobileApp[📱 Mobile App<br/>React Native]
        AdminPortal[🔧 Admin Portal<br/>Management UI]
    end
    
    subgraph "🚪 API Layer"
        APIGateway[🚪 API Gateway<br/>REST Endpoints]
        GraphQL[🔗 GraphQL API<br/>Unified Data Access]
    end
    
    subgraph "⚙️ Business Logic Layer"
        ProductService[🏷️ Product Service<br/>60M Records Lookup]
        InvoiceService[📄 Invoice Service<br/>Document Processing]
        CommissionService[💰 Commission Service<br/>Business Rules]
    end
    
    subgraph "💾 Data Tier Architecture"
        subgraph "🔥 Hot Data (Real-time)"
            Redis[⚡ ElastiCache Redis<br/>Product Cache<br/>TTL: 24h]
            RDSPrimary[🗄️ RDS Primary<br/>PostgreSQL 14<br/>Multi-AZ]
        end
        
        subgraph "🌡️ Warm Data (Operational)"
            RDSReadReplica[🗄️ RDS Read Replica<br/>Query Optimization<br/>Cross-AZ]
            S3Intelligent[📦 S3 Intelligent Tiering<br/>Document Storage<br/>Auto-archiving]
        end
        
        subgraph "❄️ Cold Data (Analytics)"
            Redshift[📊 Redshift Cluster<br/>Data Warehouse<br/>Columnar Storage]
            S3Glacier[🧊 S3 Glacier<br/>Long-term Archive<br/>7-year retention]
        end
    end
    
    subgraph "🔄 Data Pipeline"
        Glue[🔄 AWS Glue<br/>ETL Jobs<br/>Data Catalog]
        Kinesis[🌊 Kinesis Data Streams<br/>Real-time Analytics]
        Firehose[🚰 Kinesis Firehose<br/>Data Delivery]
    end
    
    subgraph "📊 Analytics & BI"
        QuickSight[📊 QuickSight<br/>Business Intelligence<br/>Dashboards]
        Athena[🔍 Amazon Athena<br/>Serverless Queries<br/>S3 Data Lake]
    end
    
    WebApp --> APIGateway
    MobileApp --> APIGateway
    AdminPortal --> GraphQL
    
    APIGateway --> ProductService
    APIGateway --> InvoiceService
    GraphQL --> CommissionService
    
    ProductService --> Redis
    ProductService --> RDSPrimary
    InvoiceService --> RDSPrimary
    CommissionService --> RDSReadReplica
    
    RDSPrimary --> RDSReadReplica
    InvoiceService --> S3Intelligent
    
    RDSPrimary --> Glue
    S3Intelligent --> Glue
    Glue --> Redshift
    
    ProductService --> Kinesis
    Kinesis --> Firehose
    Firehose --> S3Intelligent
    
    S3Intelligent --> S3Glacier
    Redshift --> QuickSight
    S3Intelligent --> Athena
    Athena --> QuickSight
    
    style Redis fill:#ff5722
    style RDSPrimary fill:#9c27b0
    style Redshift fill:#ff9800
    style S3Intelligent fill:#4caf50
    style Glue fill:#2196f3
```

## 5. Seguridad y Compliance

```mermaid
graph TB
    subgraph "🌐 Edge Security"
        CloudFront[🌍 CloudFront<br/>Global CDN]
        WAF[🛡️ AWS WAF<br/>Web Application Firewall]
        Shield[🛡️ AWS Shield<br/>DDoS Protection]
    end
    
    subgraph "🔐 Identity & Access"
        Cognito[🔐 Amazon Cognito<br/>User Authentication]
        IAM[👤 AWS IAM<br/>Role-based Access]
        SecretsManager[🔑 Secrets Manager<br/>API Keys & Passwords]
    end
    
    subgraph "🏢 Network Security"
        VPC[🏢 VPC<br/>Isolated Network]
        PrivateSubnets[🔒 Private Subnets<br/>Application Tier]
        PublicSubnets[🌐 Public Subnets<br/>Load Balancers]
        NATGateway[🚪 NAT Gateway<br/>Outbound Internet]
        VPCEndpoints[🔗 VPC Endpoints<br/>AWS Services]
    end
    
    subgraph "🔒 Data Encryption"
        KMS[🔐 AWS KMS<br/>Key Management<br/>Customer Managed Keys]
        S3Encryption[📦 S3 Encryption<br/>AES-256 at Rest]
        RDSEncryption[🗄️ RDS Encryption<br/>TDE + Backup Encryption]
        EBSEncryption[💽 EBS Encryption<br/>Volume Encryption]
    end
    
    subgraph "📊 Monitoring & Compliance"
        CloudTrail[📋 CloudTrail<br/>API Audit Logs<br/>7-year retention]
        Config[⚙️ AWS Config<br/>Compliance Rules<br/>Resource Tracking]
        GuardDuty[🔍 GuardDuty<br/>Threat Detection<br/>ML-based Security]
        SecurityHub[🛡️ Security Hub<br/>Centralized Security<br/>Compliance Dashboard]
    end
    
    subgraph "🚨 Incident Response"
        CloudWatch[📈 CloudWatch<br/>Security Metrics<br/>Real-time Alerts]
        SNS[📢 SNS<br/>Alert Notifications<br/>Multi-channel]
        Lambda[⚡ Lambda<br/>Automated Response<br/>Security Remediation]
    end
    
    CloudFront --> WAF
    WAF --> Shield
    Shield --> PublicSubnets
    
    PublicSubnets --> PrivateSubnets
    PrivateSubnets --> NATGateway
    PrivateSubnets --> VPCEndpoints
    
    Cognito --> IAM
    IAM --> SecretsManager
    
    KMS --> S3Encryption
    KMS --> RDSEncryption
    KMS --> EBSEncryption
    
    CloudTrail --> SecurityHub
    Config --> SecurityHub
    GuardDuty --> SecurityHub
    SecurityHub --> CloudWatch
    
    CloudWatch --> SNS
    SNS --> Lambda
    
    style WAF fill:#f44336
    style KMS fill:#9c27b0
    style CloudTrail fill:#ff9800
    style GuardDuty fill:#e91e63
    style SecurityHub fill:#2196f3
```

## 6. Monitoreo y Observabilidad

```mermaid
graph TB
    subgraph "📊 Metrics Collection"
        CloudWatch[📈 CloudWatch<br/>System Metrics<br/>Custom Metrics]
        XRay[🔍 X-Ray<br/>Distributed Tracing<br/>Service Map]
        ContainerInsights[🐳 Container Insights<br/>ECS/Fargate Metrics<br/>Performance Monitoring]
    end
    
    subgraph "📋 Logging"
        CloudWatchLogs[📋 CloudWatch Logs<br/>Centralized Logging<br/>Log Groups]
        LogInsights[🔍 CloudWatch Insights<br/>Log Analysis<br/>Query Engine]
        S3LogArchive[📦 S3 Log Archive<br/>Long-term Storage<br/>Cost Optimization]
    end
    
    subgraph "🚨 Alerting & Notifications"
        CloudWatchAlarms[🚨 CloudWatch Alarms<br/>Threshold Monitoring<br/>Anomaly Detection]
        SNS[📢 SNS Topics<br/>Multi-channel Alerts<br/>Email, SMS, Slack]
        PagerDuty[📱 PagerDuty<br/>Incident Management<br/>On-call Rotation]
    end
    
    subgraph "📊 Dashboards & Visualization"
        CloudWatchDashboards[📊 CloudWatch Dashboards<br/>Real-time Metrics<br/>Custom Widgets]
        QuickSight[📊 QuickSight<br/>Business Intelligence<br/>Executive Reports]
        Grafana[📊 Grafana<br/>Advanced Visualization<br/>Custom Dashboards]
    end
    
    subgraph "🔍 Application Performance"
        APMAgent[🔍 APM Agent<br/>Application Monitoring<br/>Performance Insights]
        RUMAgent[📱 RUM Agent<br/>Real User Monitoring<br/>Frontend Performance]
        SyntheticMonitoring[🤖 Synthetic Monitoring<br/>Proactive Testing<br/>Availability Checks]
    end
    
    subgraph "💰 Cost Monitoring"
        CostExplorer[💰 Cost Explorer<br/>Spend Analysis<br/>Cost Optimization]
        Budgets[💳 AWS Budgets<br/>Cost Alerts<br/>Spend Forecasting]
        TrustedAdvisor[💡 Trusted Advisor<br/>Best Practices<br/>Optimization Recommendations]
    end
    
    CloudWatch --> CloudWatchAlarms
    XRay --> CloudWatch
    ContainerInsights --> CloudWatch
    
    CloudWatchLogs --> LogInsights
    CloudWatchLogs --> S3LogArchive
    
    CloudWatchAlarms --> SNS
    SNS --> PagerDuty
    
    CloudWatch --> CloudWatchDashboards
    CloudWatch --> QuickSight
    CloudWatch --> Grafana
    
    APMAgent --> XRay
    RUMAgent --> CloudWatch
    SyntheticMonitoring --> CloudWatchAlarms
    
    CostExplorer --> Budgets
    Budgets --> SNS
    TrustedAdvisor --> SNS
    
    style CloudWatch fill:#ff9800
    style XRay fill:#2196f3
    style CloudWatchAlarms fill:#f44336
    style SNS fill:#4caf50
    style QuickSight fill:#9c27b0
```

## 7. Disaster Recovery y Backup

```mermaid
graph TB
    subgraph "🌎 Primary Region (us-east-1)"
        subgraph "🏢 Production Environment"
            ProdVPC[🏢 Production VPC<br/>10.0.0.0/16]
            ProdECS[🐳 ECS Fargate<br/>Production Cluster]
            ProdRDS[🗄️ RDS Primary<br/>Multi-AZ PostgreSQL]
            ProdS3[📦 S3 Production<br/>Cross-Region Replication]
            ProdRedshift[📊 Redshift Cluster<br/>Production Analytics]
        end
        
        subgraph "📊 Monitoring"
            CloudWatch[📈 CloudWatch<br/>Health Monitoring]
            Route53Health[🌐 Route 53<br/>Health Checks]
        end
    end
    
    subgraph "🌎 DR Region (us-west-2)"
        subgraph "🔄 Disaster Recovery"
            DRVPC[🏢 DR VPC<br/>10.1.0.0/16]
            DRECS[🐳 ECS Fargate<br/>DR Cluster (Standby)]
            DRRDS[🗄️ RDS Read Replica<br/>Cross-Region]
            DRS3[📦 S3 DR Bucket<br/>Replica Destination]
            DRRedshift[📊 Redshift DR<br/>Snapshot Restore]
        end
    end
    
    subgraph "💾 Backup Strategy"
        subgraph "🔄 Automated Backups"
            RDSBackup[🗄️ RDS Automated Backup<br/>35-day retention<br/>Point-in-time Recovery]
            S3Versioning[📦 S3 Versioning<br/>Object-level Backup<br/>Lifecycle Policies]
            RedshiftSnapshot[📊 Redshift Snapshots<br/>Daily Automated<br/>Cross-region Copy]
        end
        
        subgraph "📦 Long-term Archive"
            S3Glacier[🧊 S3 Glacier<br/>7-year Compliance<br/>Deep Archive]
            BackupVault[🔒 AWS Backup Vault<br/>Centralized Backup<br/>Cross-service]
        end
    end
    
    subgraph "🚨 Failover Automation"
        Route53Failover[🌐 Route 53 Failover<br/>DNS-based Routing<br/>Health Check Triggers]
        LambdaFailover[⚡ Lambda Functions<br/>Automated Failover<br/>Infrastructure Provisioning]
        StepFunctionsOrchestration[🔄 Step Functions<br/>DR Orchestration<br/>Multi-step Recovery]
    end
    
    subgraph "📋 Recovery Procedures"
        RunbookAutomation[📋 Runbook Automation<br/>Systems Manager<br/>Documented Procedures]
        RecoveryTesting[🧪 DR Testing<br/>Quarterly Tests<br/>RTO/RPO Validation]
    end
    
    ProdRDS --> DRRDS
    ProdS3 --> DRS3
    ProdRedshift --> RedshiftSnapshot
    
    ProdRDS --> RDSBackup
    ProdS3 --> S3Versioning
    ProdRedshift --> RedshiftSnapshot
    
    S3Versioning --> S3Glacier
    RDSBackup --> BackupVault
    
    CloudWatch --> Route53Failover
    Route53Health --> Route53Failover
    Route53Failover --> LambdaFailover
    LambdaFailover --> StepFunctionsOrchestration
    
    StepFunctionsOrchestration --> DRECS
    StepFunctionsOrchestration --> DRRedshift
    
    RunbookAutomation --> RecoveryTesting
    
    style ProdRDS fill:#9c27b0
    style DRRDS fill:#673ab7
    style Route53Failover fill:#ff9800
    style LambdaFailover fill:#4caf50
    style S3Glacier fill:#2196f3
```
