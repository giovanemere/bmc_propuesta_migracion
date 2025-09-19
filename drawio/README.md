# Diagramas Draw.io - Arquitectura BMC

## 📊 Diagramas Disponibles

### 1. **bmc-context-diagram.drawio**
**Diagrama de Contexto (C4 Level 1)**
- Actores externos: Usuarios BMC, Administradores, Sistemas Externos
- Sistema central: BMC Bolsa Comisionista
- Entidades regulatorias: DIAN, Entidades Regulatorias, Cumplimiento
- **Uso:** Presentaciones ejecutivas, vista de alto nivel

### 2. **bmc-container-diagram.drawio**
**Diagrama de Contenedores (C4 Level 2)**
- **Frontend Layer:** Web App React, Mobile App, Admin Portal, CloudFront
- **API Layer:** Load Balancer, API Gateway, Cognito, WAF
- **Microservices:** Invoice, Product (60M), OCR, Commission, Certificate, Validation, Notification
- **Data Layer:** RDS PostgreSQL, Redshift, ElastiCache Redis, S3, Elasticsearch
- **External Integrations:** SFTP, SES, DIAN API, Textract, CloudWatch
- **Uso:** Arquitectura técnica, revisiones de diseño

### 3. **bmc-aws-infrastructure.drawio**
**Infraestructura AWS Completa**
- **VPC:** Subnets públicas y privadas, Multi-AZ
- **Compute:** ECS Fargate, Lambda Functions, Step Functions
- **Data:** RDS Multi-AZ, Redshift Cluster, ElastiCache, Elasticsearch
- **Storage:** S3 Buckets, Transfer Family SFTP
- **Security:** WAF, GuardDuty, KMS, Config, CloudTrail
- **Monitoring:** CloudWatch, X-Ray
- **Uso:** Implementación técnica, documentación de infraestructura

## 🛠️ Cómo Usar los Diagramas

### Opción 1: Draw.io Web (Recomendado)
1. Ir a [app.diagrams.net](https://app.diagrams.net)
2. Abrir archivo `.drawio`
3. Editar según necesidades
4. Exportar como PNG/PDF: `File > Export as > PNG`

### Opción 2: Draw.io Desktop
1. Descargar [draw.io desktop](https://github.com/jgraph/drawio-desktop/releases)
2. Instalar aplicación
3. Abrir archivos `.drawio`
4. Exportar a PNG/PDF

### Opción 3: Conversión Automática
```bash
# Ejecutar script de conversión
chmod +x generate-png-diagrams.sh
./generate-png-diagrams.sh
```

## 📋 Especificaciones Técnicas

### Elementos Visuales
- **Emojis:** Identificación rápida de componentes
- **Colores:** Codificación por tipo de servicio
  - 🔵 Azul: Servicios de aplicación
  - 🟢 Verde: Infraestructura y red
  - 🟠 Naranja: Servicios AWS externos
  - 🔴 Rojo: Seguridad y monitoreo
  - 🟣 Morado: Analytics y datos

### Métricas Incluidas
- **Performance Targets:** OCR >95%, Product Lookup <500ms
- **Capacity:** 60M productos, 10K facturas/hora
- **Availability:** >99.9% uptime
- **Security:** Encryption at rest/transit, MFA, RBAC

## 🎯 Casos de Uso

### Para Stakeholders Ejecutivos
- **Contexto:** Vista de alto nivel del sistema
- **Beneficios:** Entender valor de negocio y compliance

### Para Arquitectos Técnicos
- **Contenedores:** Diseño de microservicios
- **Infraestructura:** Implementación AWS detallada

### Para Equipos de Desarrollo
- **Componentes:** Interfaces y dependencias
- **APIs:** Endpoints y integraciones

### Para Equipos de Operaciones
- **Infraestructura:** Configuración AWS
- **Monitoreo:** Métricas y alertas

## 📁 Estructura de Archivos

```
drawio/
├── README.md                           # Este archivo
├── bmc-context-diagram.drawio          # Diagrama de contexto
├── bmc-container-diagram.drawio        # Diagrama de contenedores  
├── bmc-aws-infrastructure.drawio       # Infraestructura AWS
└── png/                               # Archivos PNG generados
    ├── bmc-context-diagram.png
    ├── bmc-container-diagram.png
    └── bmc-aws-infrastructure.png
```

## 🔄 Actualización de Diagramas

### Proceso Recomendado
1. **Editar** archivos `.drawio` en draw.io
2. **Validar** cambios con equipo técnico
3. **Exportar** nuevas versiones PNG
4. **Actualizar** documentación relacionada
5. **Commit** cambios al repositorio

### Versionado
- Los archivos `.drawio` son la fuente de verdad
- Mantener historial en Git
- Exportar PNG para presentaciones
- Documentar cambios significativos

## 🚀 Próximos Pasos

1. **Revisar** diagramas con stakeholders
2. **Validar** arquitectura técnica
3. **Actualizar** según feedback
4. **Usar** en presentaciones y documentación
5. **Mantener** actualizado durante implementación
