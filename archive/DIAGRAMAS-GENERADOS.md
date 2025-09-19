# Diagramas Generados - Arquitectura BMC

## 1. Diagrama de Contexto (C4 Level 1)

```mermaid
graph TB
    Users[👥 Usuarios BMC<br/>Operadores]
    External[🏢 Sistemas Externos<br/>SFTP Integration]
    
    BMC[🏛️ Sistema BMC<br/>Regulatory Platform]
    
    DIAN[🏛️ DIAN<br/>Tax Authority]
    Regulatory[📋 Entidades Regulatorias<br/>Financial Oversight]
    
    Users --> BMC
    External --> BMC
    BMC --> DIAN
    BMC --> Regulatory
    
    style BMC fill:#e1f5fe
    style DIAN fill:#fff3e0
```

## 2. Diagrama de Contenedores (C4 Level 2)

```mermaid
graph TB
    subgraph "🌐 Frontend Layer"
        WebApp[📱 Web Frontend<br/>React SPA]
        AdminPortal[🔧 Admin Portal<br/>Management UI]
    end
    
    subgraph "🚪 API Layer"
        APIGateway[🚪 API Gateway<br/>Central Routing]
    end
    
    subgraph "⚙️ Microservices Layer"
        InvoiceService[📄 Invoice Service<br/>Processing & OCR]
        ProductService[🏷️ Product Service<br/>60M Records]
        OCRService[👁️ OCR Service<br/>Textract Integration]
        CommissionService[💰 Commission Service<br/>Business Rules]
    end
    
    subgraph "💾 Data Layer"
        RDS[(🗄️ RDS PostgreSQL<br/>Transactional Data)]
        Redis[(⚡ ElastiCache Redis<br/>Caching)]
        S3[(📦 S3<br/>Document Storage)]
    end
    
    WebApp --> APIGateway
    APIGateway --> InvoiceService
    APIGateway --> ProductService
    InvoiceService --> OCRService
    ProductService --> Redis
    InvoiceService --> RDS
    OCRService --> S3
```

## 3. Diagrama de Secuencia - Procesamiento de Facturas

```mermaid
sequenceDiagram
    participant User as 👤 User
    participant Frontend as 📱 Frontend
    participant API as 🚪 API Gateway
    participant Invoice as 📄 Invoice Service
    participant OCR as 👁️ OCR Service
    participant Product as 🏷️ Product Service
    
    User->>Frontend: Upload Invoice
    Frontend->>API: POST /invoices/upload
    API->>Invoice: Process Upload
    Invoice->>OCR: Extract Text/Data
    OCR-->>Invoice: Structured Data
    Invoice->>Product: Match Products (60M lookup)
    Product-->>Invoice: Matched Products
    Invoice-->>API: Processing Complete
```

## 4. Diagrama de Flujo de Datos

```mermaid
graph LR
    subgraph "Data Sources"
        Upload[📁 File Upload]
        Images[🖼️ Images/PDFs]
    end
    
    subgraph "Processing"
        OCR[👁️ OCR Processing]
        Validation[✅ Validation]
        Matching[🔍 Product Matching]
    end
    
    subgraph "Storage"
        RDS[(🗄️ PostgreSQL<br/>60M Products)]
        S3[(📦 S3 Storage)]
        Cache[(⚡ Redis Cache)]
    end
    
    Upload --> OCR
    Images --> OCR
    OCR --> Validation
    Validation --> Matching
    Matching --> RDS
    OCR --> S3
    Matching --> Cache
```

## 5. Arquitectura Completa del Sistema BMC

```mermaid
graph TB
    subgraph "👥 Usuarios"
        U1[👤 Operadores BMC]
        U2[👨‍💼 Administradores]
        U3[🏢 Sistemas Externos]
    end
    
    subgraph "🌐 Capa Frontend"
        F1[📱 Web App React]
        F2[🔧 Admin Portal]
        F3[📱 Mobile App]
    end
    
    subgraph "🚪 Capa API"
        API[🚪 API Gateway]
        AUTH[🔐 Cognito Auth]
        LB[⚖️ Load Balancer]
    end
    
    subgraph "⚙️ Microservicios"
        MS1[📄 Invoice Service<br/>Procesamiento Facturas]
        MS2[🏷️ Product Service<br/>60M Productos]
        MS3[👁️ OCR Service<br/>Textract >95%]
        MS4[💰 Commission Service<br/>Reglas Negocio]
        MS5[📜 Certificate Service<br/>PDF Generation]
        MS6[✅ Validation Service<br/>DIAN Compliance]
        MS7[📧 Notification Service<br/>Email & Alerts]
    end
    
    subgraph "💾 Capa de Datos"
        DB1[(🗄️ RDS PostgreSQL<br/>Transaccional)]
        DB2[(📊 Redshift<br/>Analytics)]
        DB3[(⚡ Redis Cache<br/>24h TTL)]
        DB4[(📦 S3 Storage<br/>Documentos)]
    end
    
    subgraph "🔗 Integraciones"
        I1[📁 SFTP Gateway]
        I2[📧 SES Email]
        I3[🏛️ DIAN API]
        I4[📊 CloudWatch]
    end
    
    %% Conexiones Usuarios
    U1 --> F1
    U2 --> F2
    U3 --> I1
    
    %% Conexiones Frontend
    F1 --> LB
    F2 --> LB
    F3 --> LB
    LB --> API
    
    %% Autenticación
    API --> AUTH
    
    %% Conexiones Microservicios
    API --> MS1
    API --> MS2
    API --> MS4
    
    MS1 --> MS3
    MS1 --> MS6
    MS2 --> MS6
    MS4 --> MS5
    MS5 --> MS7
    
    %% Conexiones Base de Datos
    MS1 --> DB1
    MS2 --> DB1
    MS4 --> DB1
    MS6 --> DB1
    
    MS2 --> DB3
    MS3 --> DB4
    MS5 --> DB4
    
    MS1 --> DB2
    MS4 --> DB2
    
    %% Integraciones Externas
    MS7 --> I2
    MS1 --> I1
    MS2 --> I3
    MS6 --> I3
    
    %% Monitoreo
    MS1 --> I4
    MS2 --> I4
    MS3 --> I4
    
    %% Estilos
    style API fill:#e8f5e8,stroke:#2e7d32,stroke-width:3px
    style MS1 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style MS2 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style MS3 fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    style DB1 fill:#f1f8e9,stroke:#558b2f,stroke-width:2px
    style DB3 fill:#fff8e1,stroke:#f57f17,stroke-width:2px
```

## 6. Flujo de Procesamiento OCR Detallado

```mermaid
sequenceDiagram
    participant User as 👤 Usuario
    participant Frontend as 📱 React Frontend
    participant API as 🚪 API Gateway
    participant Auth as 🔐 Cognito
    participant Invoice as 📄 Invoice Service
    participant S3 as 📦 S3 Storage
    participant OCR as 👁️ OCR Service
    participant Textract as 🤖 Textract
    participant Product as 🏷️ Product Service
    participant Cache as ⚡ Redis Cache
    participant DB as 🗄️ PostgreSQL
    participant Commission as 💰 Commission Service
    participant Certificate as 📜 Certificate Service
    participant Email as 📧 SES Email
    
    Note over User, Email: Flujo Completo de Procesamiento
    
    User->>Frontend: Subir Factura (Imagen/PDF)
    Frontend->>API: POST /auth/login
    API->>Auth: Validar Credenciales
    Auth-->>API: Token JWT
    API-->>Frontend: Autenticado
    
    Frontend->>API: POST /invoices/upload + Token
    API->>Invoice: Procesar Carga
    Invoice->>S3: Almacenar Documento Original
    S3-->>Invoice: URL Documento
    
    Invoice->>OCR: Extraer Texto (URL S3)
    OCR->>Textract: Procesar con AI
    
    Note over Textract: OCR Processing<br/>Target: >95% Confidence
    
    Textract-->>OCR: Texto + Confidence Score
    
    alt Confidence > 95%
        OCR-->>Invoice: ✅ Datos Estructurados
        Invoice->>Product: Buscar Productos (60M)
        Product->>Cache: Check Redis Cache
        
        alt Cache Hit
            Cache-->>Product: Productos Cacheados
        else Cache Miss
            Product->>DB: Query 60M Records
            DB-->>Product: Resultados
            Product->>Cache: Store (24h TTL)
        end
        
        Product-->>Invoice: Productos + DIAN Classification
        Invoice->>Commission: Calcular Comisión
        Commission->>DB: Aplicar Reglas Negocio
        Commission-->>Invoice: Comisión Calculada
        
        Invoice->>Certificate: Generar Certificado
        Certificate->>S3: Crear PDF
        Certificate->>Email: Enviar por Correo
        Email-->>Certificate: ✅ Enviado
        Certificate-->>Invoice: Certificado Listo
        
        Invoice-->>API: ✅ Procesamiento Completo
        API-->>Frontend: Success + Certificate URL
        Frontend-->>User: ✅ Factura Procesada
        
    else Confidence < 95%
        OCR-->>Invoice: ⚠️ Baja Confianza
        Invoice-->>API: Requiere Revisión Manual
        API-->>Frontend: Manual Review Required
        Frontend-->>User: ⚠️ Revisión Pendiente
    end
    
    Note over User, Email: Tiempo Total: <30 segundos
```

## 7. Arquitectura de Eventos (Event-Driven)

```mermaid
graph TB
    subgraph "📡 Event Producers"
        EP1[📁 File Upload Event]
        EP2[👁️ OCR Complete Event]
        EP3[✅ Validation Event]
        EP4[💰 Commission Event]
        EP5[📜 Certificate Event]
    end
    
    subgraph "⚡ Event Bus"
        EB[⚡ Amazon EventBridge<br/>Central Event Router]
    end
    
    subgraph "📬 Message Queues"
        Q1[📄 Invoice Queue<br/>SQS FIFO]
        Q2[👁️ OCR Queue<br/>SQS Standard]
        Q3[📧 Notification Queue<br/>SQS Standard]
        Q4[💀 Dead Letter Queue<br/>Error Handling]
    end
    
    subgraph "🎯 Event Consumers"
        EC1[📄 Process Invoice<br/>Lambda Function]
        EC2[💰 Calculate Commission<br/>Step Functions]
        EC3[📜 Generate Certificate<br/>Lambda Function]
        EC4[📧 Send Notification<br/>Lambda Function]
    end
    
    subgraph "🔔 Notifications"
        N1[📢 SNS Topics<br/>System Alerts]
        N2[📊 CloudWatch<br/>Metrics & Alarms]
    end
    
    %% Event Flow
    EP1 --> EB
    EP2 --> EB
    EP3 --> EB
    EP4 --> EB
    EP5 --> EB
    
    %% Queue Routing
    EB --> Q1
    EB --> Q2
    EB --> Q3
    
    %% Error Handling
    Q1 -.->|Failed| Q4
    Q2 -.->|Failed| Q4
    Q3 -.->|Failed| Q4
    
    %% Event Processing
    Q1 --> EC1
    Q1 --> EC2
    Q2 --> EC3
    Q3 --> EC4
    
    %% Notifications
    EC1 --> N1
    EC2 --> N2
    EC3 --> N2
    EC4 --> N1
    
    style EB fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    style Q1 fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style Q4 fill:#ffebee,stroke:#d32f2f,stroke-width:2px
```

## Resumen de Diagramas Generados

✅ **7 Diagramas Mermaid Creados:**
1. **Contexto** - Actores y sistema BMC
2. **Contenedores** - Arquitectura de alto nivel
3. **Secuencia** - Flujo de procesamiento
4. **Flujo de Datos** - Pipeline de información
5. **Arquitectura Completa** - Vista integral del sistema
6. **OCR Detallado** - Procesamiento con >95% precisión
7. **Eventos** - Arquitectura event-driven

**Características:**
- 📊 Visualización interactiva con emojis
- 🎯 Métricas de performance integradas
- 🔄 Flujos de datos claramente definidos
- ⚡ Arquitectura event-driven con AWS services
- 🏛️ Compliance DIAN y regulatorio
- 📈 Escalabilidad para 60M productos
