# Diagrama de Infraestructura - Sistema de Procesamiento de Facturas

```mermaid
graph TB
    %% External Sources
    User[👤 Usuario] --> S3Raw[📦 S3 Raw Bucket<br/>invoices-raw]
    
    %% S3 Storage Layer
    S3Raw --> |Trigger| SFN[⚙️ Step Functions<br/>Workflow]
    S3Raw --> S3Processed[📦 S3 Processed<br/>invoices-processed]
    S3Processed --> S3Lake[📦 S3 Data Lake<br/>data-lake]
    
    %% Step Functions Workflow
    SFN --> L1[🔧 Lambda Textract<br/>OCR Processing]
    L1 --> L2[🔧 Lambda Normalize<br/>Data Normalization]
    L2 --> L3[🔧 Lambda Matcher<br/>Product Matching]
    L3 --> L4[🔧 Lambda Calculator<br/>Commission Calc]
    
    %% AWS Services Integration
    L1 --> |OCR| Textract[📄 AWS Textract<br/>Document Analysis]
    L3 --> |Fast Lookup| DDB[🗃️ DynamoDB<br/>SKU Lookup Table]
    L3 --> |Search| OS[🔍 OpenSearch<br/>Product Index]
    
    %% Database Layer
    L4 --> Aurora[🗄️ Aurora Serverless<br/>PostgreSQL OLTP]
    
    %% Analytics Layer
    S3Lake --> Glue[⚡ AWS Glue<br/>ETL Job]
    Glue --> Redshift[📊 Redshift Cluster<br/>Analytics DW]
    
    %% Data Catalog
    Glue --> GlueCatalog[📚 Glue Catalog<br/>Data Lake DB]
    
    %% IAM Roles (simplified)
    IAMLambda[🔐 Lambda IAM Role] -.-> L1
    IAMLambda -.-> L2
    IAMLambda -.-> L3
    IAMLambda -.-> L4
    IAMGlue[🔐 Glue IAM Role] -.-> Glue
    IAMSFN[🔐 Step Functions Role] -.-> SFN
    
    %% Styling
    classDef storage fill:#e1f5fe
    classDef compute fill:#f3e5f5
    classDef database fill:#e8f5e8
    classDef analytics fill:#fff3e0
    classDef security fill:#ffebee
    
    class S3Raw,S3Processed,S3Lake storage
    class L1,L2,L3,L4,SFN,Glue compute
    class DDB,Aurora,OS database
    class Redshift,GlueCatalog analytics
    class IAMLambda,IAMGlue,IAMSFN security
```

## Componentes Principales

### 🔄 Flujo de Procesamiento
1. **Ingesta**: Facturas suben a S3 Raw Bucket
2. **Orquestación**: Step Functions coordina el workflow
3. **OCR**: Lambda + Textract extrae texto de documentos
4. **Normalización**: Lambda procesa y limpia datos
5. **Matching**: Lambda busca productos en DynamoDB/OpenSearch
6. **Cálculo**: Lambda calcula comisiones y métricas
7. **Persistencia**: Datos se guardan en Aurora y S3

### 📊 Capa de Analytics
- **Glue ETL**: Procesa datos de S3 → Redshift
- **Redshift**: Data warehouse para análisis
- **Glue Catalog**: Metadatos del data lake

### 🗄️ Almacenamiento
- **S3 Raw**: Facturas originales
- **S3 Processed**: Datos procesados
- **S3 Data Lake**: Repositorio central
- **DynamoDB**: Lookup rápido de SKUs
- **Aurora**: Base transaccional
- **OpenSearch**: Búsqueda híbrida

### 🔐 Seguridad
- Roles IAM específicos por servicio
- Encriptación en S3 y bases de datos
- Acceso controlado entre servicios

## Características Técnicas

- **Región**: us-east-1
- **Escalabilidad**: Serverless (Lambda, Aurora, Step Functions)
- **Durabilidad**: Versionado S3, backups RDS
- **Monitoreo**: CloudWatch integrado
- **Costos**: Pay-per-use en la mayoría de servicios
