# 🏗️ Arquitectura y Diseño de Componentes

## 📋 Resumen Ejecutivo

Sistema MCP Diagram Generator v4.1.0 - Plataforma profesional para generación automática de diagramas técnicos y documentación desde especificaciones de proyectos.

## 🎯 Arquitectura General

```
┌─────────────────────────────────────────────────────────────┐
│                    MCP DIAGRAM GENERATOR                    │
├─────────────────────────────────────────────────────────────┤
│  🎮 ORCHESTRATION LAYER                                    │
│  ├── WorkflowOrchestrator (Flujo completo)                 │
│  └── AppConfig (Configuración transversal)                 │
├─────────────────────────────────────────────────────────────┤
│  🔧 GENERATION LAYER                                       │
│  ├── UniversalGenerator (PNG + DrawIO)                     │
│  ├── DiagramGenerator (PNG especializado)                  │
│  ├── PromptGenerator (Prompts MCP)                         │
│  └── DocGenerator (Documentación)                          │
├─────────────────────────────────────────────────────────────┤
│  ✅ VALIDATION LAYER                                       │
│  ├── XMLValidator (Calidad DrawIO)                         │
│  ├── MCPIntegrator (Coherencia MCP)                        │
│  └── AutomatedTests (Tests calidad)                        │
├─────────────────────────────────────────────────────────────┤
│  📐 TEMPLATE LAYER                                         │
│  ├── DrawIOTemplates (XML profesional)                     │
│  ├── AWSComponents (Clases especializadas)                 │
│  └── StandardInputModel (Esquema JSON)                     │
├─────────────────────────────────────────────────────────────┤
│  🌐 API LAYER                                              │
│  └── DiagramAPI (REST endpoints)                           │
└─────────────────────────────────────────────────────────────┘
```

## 🏛️ Principios de Diseño

### 1. Separación de Responsabilidades
- **Orquestación:** WorkflowOrchestrator coordina flujo completo
- **Generación:** Generadores especializados por formato
- **Validación:** Validadores independientes de calidad
- **Configuración:** AppConfig centraliza toda configuración

### 2. Inversión de Dependencias
- Componentes dependen de abstracciones, no implementaciones
- Configuración inyectada desde AppConfig
- Paths dinámicos sin rutas hardcoded

### 3. Principio Abierto/Cerrado
- Extensible para nuevos formatos (Azure, GCP)
- Cerrado para modificación de core
- Factory pattern para componentes AWS

### 4. Responsabilidad Única
- Cada clase tiene una responsabilidad específica
- Generadores especializados por tipo
- Validadores enfocados en calidad

## 📦 Componentes Detallados

### Core Components

#### AppConfig (`src/core/app_config.py`)
```python
Responsabilidades:
├── Gestión centralizada de configuraciones
├── Auto-detección de paths del proyecto
├── Cache inteligente de configuraciones
├── Variables de entorno integradas
└── Estructura de outputs organizada

APIs Principales:
├── get_config(name) → Dict[str, Any]
├── save_config(name, data) → str
├── get_output_path(type, filename) → Path
└── get_paths() → AppPaths

Patrones Aplicados:
├── Singleton (instancia global)
├── Factory (creación de paths)
└── Cache (configuraciones)
```

#### WorkflowOrchestrator (`src/core/workflow_orchestrator.py`)
```python
Responsabilidades:
├── Coordinación del flujo completo (6 fases)
├── Manejo robusto de errores
├── Consolidación de resultados
├── Generación de reportes ejecutivos
└── Validación de coherencia

Flujo de Ejecución:
1️⃣ Config → Carga y valida configuración
2️⃣ Prompts → Genera prompts MCP especializados
3️⃣ Docs → Crea documentación técnica
4️⃣ Diagramas → PNG + DrawIO profesionales
5️⃣ Consolidación → Resultados en JSON
6️⃣ Reporte → Métricas y resumen ejecutivo

Patrones Aplicados:
├── Command (fases del flujo)
├── Template Method (estructura fija)
└── Observer (reporte de progreso)
```

### Generation Components

#### UniversalGenerator (`src/generators/universal_generator.py`)
```python
Responsabilidades:
├── Generación unificada PNG + DrawIO
├── Mapeo automático componentes
├── Layout inteligente
├── Estilos AWS oficiales
└── Validación de salida

Mapeo de Componentes:
PNG (diagrams) ←→ DrawIO (mxgraph.aws4)
├── Fargate ←→ mxgraph.aws4.fargate
├── RDS ←→ mxgraph.aws4.rds
├── S3 ←→ mxgraph.aws4.s3
└── APIGateway ←→ mxgraph.aws4.api_gateway

Patrones Aplicados:
├── Bridge (PNG ↔ DrawIO)
├── Strategy (diferentes layouts)
└── Factory (creación componentes)
```

#### DiagramGenerator (`src/generators/diagram_generator.py`)
```python
Responsabilidades:
├── Generación PNG especializada (4 tipos)
├── Clusters automáticos jerárquicos
├── Iconos AWS reales de diagrams library
├── Optimización visual profesional
└── Exportación en alta calidad

Tipos de Diagramas:
├── Network: VPC, subnets, AZ, conectividad
├── Microservices: Servicios, APIs, comunicación
├── Security: WAF, Cognito, KMS, políticas
└── DataFlow: Flujos de datos, procesamiento

Patrones Aplicados:
├── Factory Method (tipos de diagramas)
├── Builder (construcción compleja)
└── Template Method (estructura común)
```

### Validation Components

#### XMLValidator (`src/validators/xml_validator.py`)
```python
Responsabilidades:
├── Validación estructura XML DrawIO
├── Verificación componentes AWS oficiales
├── Métricas de completitud automáticas
├── Integración con modelo MCP
└── Reportes de calidad detallados

Validaciones Realizadas:
├── Estructura: mxfile, diagram, mxGraphModel
├── Componentes: mxgraph.aws4.* válidos
├── Conexiones: referencias correctas
├── Completitud: vs especificación original
└── MCP: coherencia con configuración

Patrones Aplicados:
├── Chain of Responsibility (validaciones)
├── Visitor (análisis XML)
└── Strategy (tipos de validación)
```

#### MCPIntegrator (dentro de XMLValidator)
```python
Responsabilidades:
├── Conversión MCP → Modelo estándar
├── Preservación de configuración original
├── Mapeo automático de microservicios
├── Validación de coherencia bidireccional
└── Compatibilidad con versiones MCP

Proceso de Integración:
1. Carga configuración MCP existente
2. Extrae microservicios y servicios AWS
3. Convierte a modelo estándar unificado
4. Valida coherencia post-generación
5. Reporta discrepancias automáticamente

Patrones Aplicados:
├── Adapter (MCP → Estándar)
├── Facade (simplifica integración)
└── Memento (preserva estado original)
```

### Template Components

#### DrawIOTemplates (`templates/drawio_templates.py`)
```python
Responsabilidades:
├── Plantillas XML base profesionales
├── Estilos AWS oficiales por componente
├── Generación XML válido y bien formado
├── Personalización visual avanzada
└── Optimización para Draw.io

Estructura de Templates:
├── BASE_TEMPLATE: Estructura mxfile completa
├── COMPONENT_TEMPLATE: Componentes AWS
├── CONTAINER_TEMPLATE: Contenedores (VPC, AZ)
├── CONNECTION_TEMPLATE: Conexiones con estilos
└── TITLE_TEMPLATE: Títulos profesionales

Estilos por Categoría:
├── Compute: Fargate, Lambda, EC2 (naranja)
├── Database: RDS, DynamoDB (verde)
├── Storage: S3, EFS (verde claro)
├── Network: API Gateway, CloudFront (morado)
└── Security: WAF, Cognito (rojo)

Patrones Aplicados:
├── Template Method (estructura XML)
├── Factory (estilos por tipo)
└── Builder (construcción XML compleja)
```

#### AWSComponents (`src/components/aws_components.py`)
```python
Responsabilidades:
├── Clases especializadas por servicio AWS
├── Factory pattern para creación
├── Validación automática de propiedades
├── Mapeo directo PNG ↔ DrawIO
└── Metadata técnica integrada

Jerarquía de Clases:
AWSComponent (abstracta)
├── Compute: Fargate, Lambda, EC2
├── Database: RDS, DynamoDB, ElastiCache
├── Storage: S3, EFS, EBS
├── Network: APIGateway, ELB, CloudFront
├── Security: WAF, Cognito, KMS
└── Integration: SQS, SNS

Propiedades por Componente:
├── Fargate: cpu, memory, replicas
├── RDS: engine, instance_class, multi_az
├── S3: storage_class, versioning, encryption
└── APIGateway: throttle_rate, burst_limit

Patrones Aplicados:
├── Abstract Factory (componentes AWS)
├── Factory Method (creación específica)
└── Strategy (validación por tipo)
```

## 🔄 Flujos de Datos

### Flujo Principal de Generación
```
📋 Especificación → 🔧 AppConfig → 🎮 WorkflowOrchestrator
                                        ↓
🎯 Prompts ← 📚 Docs ← 📐 Diagramas ← ⚙️ Config Consolidada
    ↓           ↓         ↓
📄 3 archivos  📄 4 archivos  📄 PNG + DrawIO
    ↓           ↓         ↓
📊 Consolidación de Resultados
    ↓
📋 Reporte Ejecutivo Final
```

### Flujo de Validación
```
📐 DrawIO XML → ✅ XMLValidator → 📊 Métricas
                      ↓
🔍 Estructura → 🎨 Componentes → 🔗 Conexiones
                      ↓
📋 MCP Config → 🔄 MCPIntegrator → ✅ Coherencia
                      ↓
📊 Reporte de Calidad Final
```

## 📁 Estructura de Outputs

```
outputs/
├── png/                    # Diagramas PNG por proyecto
│   └── {project}/
│       ├── network_architecture.png
│       ├── microservices_detailed.png
│       ├── security_architecture.png
│       └── data_flow.png
├── drawio/                 # Diagramas DrawIO editables
│   └── {project}/
│       └── complete_architecture.drawio
├── mermaid/               # Diagramas Mermaid (futuro)
│   └── {project}/
├── prompts/               # Prompts MCP especializados
│   └── {project}/
│       ├── architecture_prompt.md
│       ├── implementation_prompt.md
│       └── migration_prompt.md
├── documentation/         # Documentación técnica
│   └── {project}/
│       ├── technical_architecture.md
│       ├── implementation_guide.md
│       ├── migration_plan.md
│       ├── infrastructure_config.md
│       └── {project}_report.md
└── generated/            # Configuraciones consolidadas
    ├── {project}_consolidated.json
    ├── {project}_results.json
    └── bmc.json
```

## 🧪 Testing y Calidad

### Tests Automatizados (`tests/automated_quality_tests.py`)
```python
Cobertura de Tests:
├── StandardModelTests (3 tests)
│   ├── Validación modelo JSON
│   ├── Factory de componentes
│   └── Validación componentes
├── XMLValidationTests (3 tests)
│   ├── Estructura XML DrawIO
│   ├── Componentes AWS válidos
│   └── Completitud vs especificación
├── TemplateGenerationTests (3 tests)
│   ├── Generación templates
│   ├── XML desde templates
│   └── Mapeo de estilos
├── MCPIntegrationTests (2 tests)
│   ├── Conversión MCP → Estándar
│   └── Validación XML desde MCP
└── EndToEndTests (2 tests)
    ├── Flujo completo
    └── Operaciones con archivos

Métricas de Calidad:
├── 13/13 tests passing (100%)
├── Cobertura end-to-end completa
├── Validación automática de XML
└── Integración MCP verificada
```

## 🔧 Configuración y Extensibilidad

### Variables de Entorno
```bash
DEBUG=false                 # Modo debug
LOG_LEVEL=INFO             # Nivel de logging
OUTPUT_FORMAT=both         # png, drawio, both
AWS_REGION=us-east-1       # Región AWS por defecto
PROJECT_NAME=mcp_diagrams  # Nombre proyecto por defecto
```

### Extensión para Nuevos Proveedores
```python
# Para agregar Azure/GCP:
1. Extender AWSComponent → CloudComponent
2. Agregar Azure/GCP shapes en templates
3. Implementar mapeo en UniversalGenerator
4. Actualizar tests de validación
```

## 📊 Métricas de Performance

| Operación | Tiempo | Archivos | Tamaño |
|-----------|--------|----------|--------|
| **Flujo Completo** | < 1s | 11 archivos | ~50KB total |
| **Generación PNG** | < 5s | 4 diagramas | ~1MB total |
| **Generación DrawIO** | < 1s | 1 diagrama | ~30KB |
| **Validación XML** | < 0.1s | - | - |
| **Tests Automatizados** | < 0.01s | - | - |

## 🚀 Roadmap Técnico

### v4.2.0 - Multi-Cloud
- [ ] Soporte Azure (azure4 shapes)
- [ ] Soporte GCP (gcp4 shapes)
- [ ] Templates multi-provider
- [ ] Validación cross-cloud

### v4.3.0 - IA Integration
- [ ] Layout automático con IA
- [ ] Optimización visual inteligente
- [ ] Generación desde código fuente
- [ ] Análisis de dependencias

### v5.0.0 - Platform
- [ ] Dashboard web completo
- [ ] Colaboración tiempo real
- [ ] Versionado de diagramas
- [ ] Integración CI/CD nativa

---

**Esta arquitectura garantiza escalabilidad, mantenibilidad y extensibilidad para evolucionar hacia una plataforma enterprise completa.**
