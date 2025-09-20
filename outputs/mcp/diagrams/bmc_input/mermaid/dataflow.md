# Flujo de Datos BMC - Mermaid

```mermaid
sequenceDiagram
    participant U as Usuario
    participant API as API Gateway
    participant IS as Invoice Service
    participant OCR as OCR Service
    participant PS as Product Service
    participant CS as Commission Service
    participant CERT as Certificate Service
    participant DB as PostgreSQL
    participant S3 as S3 Storage
    
    U->>API: Upload Invoice (PDF/Image)
    API->>IS: Process Invoice
    IS->>S3: Store Document
    IS->>OCR: Extract Text/Data
    OCR->>PS: Match Products
    PS->>DB: Query 60M Products
    DB-->>PS: Product Data
    PS-->>OCR: Matched Products
    OCR-->>IS: Processed Invoice
    IS->>CS: Calculate Commission
    CS->>DB: Apply DIAN Rules
    DB-->>CS: Commission Data
    CS-->>IS: Commission Result
    IS->>CERT: Generate Certificate
    CERT->>S3: Store Certificate
    CERT-->>IS: Certificate URL
    IS-->>API: Processing Complete
    API-->>U: Certificate Ready
```

## Métricas de Performance

- **Throughput:** 10,000 facturas/hora
- **Latencia OCR:** < 5 segundos
- **Lookup productos:** < 300ms
- **Generación certificado:** < 2 segundos

## Volúmenes de Datos

- **Productos:** 60M registros
- **Categorías:** 16,000 tipos
- **Facturas diarias:** ~240,000
