# 🏗️ Arquitectura y Diseño de Componentes

## 📋 Resumen Ejecutivo

Sistema MCP Diagram Generator v4.1.0 - Plataforma profesional para generación automática de diagramas técnicos y documentación desde especificaciones de proyectos.

## 🎯 Arquitectura General

```mermaid
graph TB
    subgraph "MCP DIAGRAM GENERATOR"
        subgraph "🎮 ORCHESTRATION LAYER"
            WO[WorkflowOrchestrator]
            AC[AppConfig]
        end
        
        subgraph "🔧 GENERATION LAYER"
            UG[UniversalGenerator]
            DG[DiagramGenerator]
            PG[PromptGenerator]
            DOC[DocGenerator]
        end
        
        subgraph "✅ VALIDATION LAYER"
            XV[XMLValidator]
            MI[MCPIntegrator]
            AT[AutomatedTests]
        end
        
        subgraph "📐 TEMPLATE LAYER"
            DT[DrawIOTemplates]
            AWS[AWSComponents]
            SIM[StandardInputModel]
        end
        
        subgraph "🌐 API LAYER"
            API[DiagramAPI]
        end
    end
    
    WO --> UG
    WO --> DG
    WO --> PG
    WO --> DOC
    
    UG --> XV
    UG --> DT
    
    DG --> AWS
    
    AC --> WO
    
    XV --> MI
    
    API --> WO
```

## 🏛️ Principios de Diseño

### 1. Separación de Responsabilidades
```plantuml
@startuml
package "Orchestration" {
  [WorkflowOrchestrator] --> [AppConfig]
}

package "Generation" {
  [UniversalGenerator]
  [DiagramGenerator]
  [PromptGenerator]
  [DocGenerator]
}

package "Validation" {
  [XMLValidator]
  [MCPIntegrator]
}

[WorkflowOrchestrator] --> [UniversalGenerator]
[WorkflowOrchestrator] --> [DiagramGenerator]
[WorkflowOrchestrator] --> [PromptGenerator]
[WorkflowOrchestrator] --> [DocGenerator]

[UniversalGenerator] --> [XMLValidator]
[XMLValidator] --> [MCPIntegrator]
@enduml
```

## 📦 Componentes Detallados

### Core Components

#### AppConfig - Configuración Transversal
```mermaid
classDiagram
    class AppConfig {
        +AppPaths paths
        +Dict config_cache
        +Dict env
        +load_config(name) Dict
        +save_config(name, data) str
        +get_output_path(type, filename) Path
        +get_paths() AppPaths
    }
    
    class AppPaths {
        +Path root_dir
        +Path src_dir
        +Path config_dir
        +Path outputs_dir
        +Path outputs_png_dir
        +Path outputs_drawio_dir
        +from_root(path) AppPaths
    }
    
    AppConfig --> AppPaths
    AppConfig --> DynamicConfigGenerator
    
    class DynamicConfigGenerator {
        +generate_config_from_specification() Dict
        +is_specification_newer() bool
        +parse_specification(content) Dict
    }
```

#### WorkflowOrchestrator - Flujo End-to-End
```plantuml
@startuml
participant User
participant WorkflowOrchestrator
participant AppConfig
participant PromptGenerator
participant DocGenerator
participant UniversalGenerator
participant Validator

User -> WorkflowOrchestrator: execute_complete_workflow()

WorkflowOrchestrator -> AppConfig: load_config("bmc")
AppConfig -> WorkflowOrchestrator: config_data

WorkflowOrchestrator -> PromptGenerator: generate_prompts()
PromptGenerator -> WorkflowOrchestrator: 3 prompt files

WorkflowOrchestrator -> DocGenerator: generate_docs()
DocGenerator -> WorkflowOrchestrator: 4 doc files

WorkflowOrchestrator -> UniversalGenerator: generate_diagrams()
UniversalGenerator -> WorkflowOrchestrator: PNG + DrawIO files

WorkflowOrchestrator -> Validator: validate_results()
Validator -> WorkflowOrchestrator: quality_metrics

WorkflowOrchestrator -> User: consolidated_results
@enduml
```

### Generation Components

#### UniversalGenerator - PNG + DrawIO Unificado
```mermaid
graph LR
    subgraph "UniversalGenerator"
        A[MCP Config] --> B[StandardSchema Converter]
        B --> C[PNG Generator]
        B --> D[DrawIO Generator]
        
        C --> E[diagrams library]
        D --> F[mxgraph.aws4 shapes]
        
        E --> G[network.png]
        E --> H[microservices.png]
        E --> I[security.png]
        E --> J[data_flow.png]
        
        F --> K[complete_architecture.drawio]
    end
    
    subgraph "Validation"
        G --> L[File Validator]
        H --> L
        I --> L
        J --> L
        K --> M[XML Validator]
    end
```

#### DiagramGenerator - PNG Especializado
```plantuml
@startuml
class DiagramGenerator {
    +Dict config
    +generate_diagram(type, output_path) str
    -_generate_network_png() str
    -_generate_microservices_png() str
    -_generate_security_png() str
    -_generate_data_flow_png() str
}

class NetworkDiagram {
    +create_vpc_cluster()
    +add_microservices()
    +add_databases()
    +add_connections()
}

class MicroservicesDiagram {
    +create_service_cluster()
    +add_fargate_services()
    +add_api_connections()
}

DiagramGenerator --> NetworkDiagram
DiagramGenerator --> MicroservicesDiagram
@enduml
```

### Validation Components

#### XMLValidator - Calidad DrawIO
```mermaid
flowchart TD
    A[DrawIO XML] --> B{Estructura Válida?}
    B -->|Sí| C[Validar Componentes AWS]
    B -->|No| D[Error: XML Malformado]
    
    C --> E{Componentes mxgraph.aws4?}
    E -->|Sí| F[Validar Conexiones]
    E -->|No| G[Error: Iconos No Oficiales]
    
    F --> H{Referencias Correctas?}
    H -->|Sí| I[Validar Completitud]
    H -->|No| J[Error: Referencias Rotas]
    
    I --> K{Todos los Microservicios?}
    K -->|Sí| L[✅ Validación Exitosa]
    K -->|No| M[⚠️ Advertencia: Incompleto]
```

#### MCPIntegrator - Coherencia MCP
```plantuml
@startuml
class MCPIntegrator {
    +convert_mcp_to_standard_model(mcp_config) StandardSchema
    +validate_mcp_generated_xml(xml, mcp_config) ValidationResult
    +load_mcp_config() Dict
}

class StandardSchema {
    +metadata: Metadata
    +architecture: Architecture
    +validate() bool
}

class Architecture {
    +components: List[Component]
    +containers: List[Container]
    +connections: List[Connection]
}

MCPIntegrator --> StandardSchema
StandardSchema --> Architecture
@enduml
```

### Template Components

#### DrawIOTemplates - XML Profesional
```mermaid
graph TD
    subgraph "DrawIO Templates"
        A[BASE_TEMPLATE] --> B[mxfile structure]
        C[COMPONENT_TEMPLATE] --> D[AWS Components]
        E[CONTAINER_TEMPLATE] --> F[VPC/AZ Containers]
        G[CONNECTION_TEMPLATE] --> H[Styled Connections]
    end
    
    subgraph "AWS Styles"
        D --> I[Compute: Fargate, Lambda]
        D --> J[Database: RDS, DynamoDB]
        D --> K[Storage: S3, EFS]
        D --> L[Network: API Gateway, CloudFront]
        D --> M[Security: WAF, Cognito]
    end
    
    subgraph "Output"
        B --> N[Valid XML]
        I --> N
        J --> N
        K --> N
        L --> N
        M --> N
        F --> N
        H --> N
    end
```

#### AWSComponents - Clases Especializadas
```plantuml
@startuml
abstract class AWSComponent {
    +String id
    +String label
    +Dict properties
    +validate() bool
    +to_png_component() DiagramComponent
    +to_drawio_xml() String
}

class Fargate extends AWSComponent {
    +String cpu
    +String memory
    +int replicas
}

class RDS extends AWSComponent {
    +String engine
    +String instance_class
    +boolean multi_az
}

class S3 extends AWSComponent {
    +String storage_class
    +boolean versioning
    +String encryption
}

class APIGateway extends AWSComponent {
    +String throttle_rate
    +String burst_limit
}

class ComponentFactory {
    +create_component(type, config) AWSComponent
}

ComponentFactory --> AWSComponent
@enduml
```

## 🔄 Flujos de Datos

### Flujo Principal de Generación
```mermaid
sequenceDiagram
    participant S as 📋 Specification
    participant AC as 🔧 AppConfig
    participant WO as 🎮 Orchestrator
    participant G as 🔧 Generators
    participant V as ✅ Validators
    participant FS as 💾 FileSystem

    S->>AC: 1. bmc-input-specification.md
    AC->>AC: 2. Dynamic config generation
    AC->>WO: 3. Consolidated config
    
    WO->>G: 4. Generate prompts (3 files)
    G->>FS: 5. Save prompts/bmc_input/
    
    WO->>G: 6. Generate docs (4 files)
    G->>FS: 7. Save documentation/bmc_input/
    
    WO->>G: 8. Generate diagrams (5 files)
    G->>FS: 9. Save png/ + drawio/
    
    WO->>V: 10. Validate all outputs
    V->>WO: 11. Quality metrics
    
    WO->>FS: 12. Consolidated results
```

### Flujo de Validación
```mermaid
graph TD
    A[📐 DrawIO XML] --> B[🔍 Structure Validator]
    B --> C{Valid XML?}
    C -->|Yes| D[🎨 Component Validator]
    C -->|No| E[❌ Structure Error]
    
    D --> F{AWS Components?}
    F -->|Yes| G[🔗 Connection Validator]
    F -->|No| H[❌ Component Error]
    
    G --> I{Valid References?}
    I -->|Yes| J[📋 Completeness Validator]
    I -->|No| K[❌ Reference Error]
    
    J --> L[🔄 MCP Integrator]
    L --> M{Coherent with MCP?}
    M -->|Yes| N[✅ Validation Success]
    M -->|No| O[⚠️ Coherence Warning]
```

## 📁 Estructura de Outputs

```mermaid
graph TD
    subgraph "outputs/"
        subgraph "png/"
            A[network_architecture.png]
            B[microservices_detailed.png]
            C[security_architecture.png]
            D[data_flow.png]
        end
        
        subgraph "drawio/"
            E[complete_architecture.drawio]
        end
        
        subgraph "prompts/"
            F[architecture_prompt.md]
            G[implementation_prompt.md]
            H[migration_prompt.md]
        end
        
        subgraph "documentation/"
            I[technical_architecture.md]
            J[implementation_guide.md]
            K[migration_plan.md]
            L[infrastructure_config.md]
        end
        
        subgraph "generated/"
            M[bmc.json]
            N[consolidated.json]
            O[results.json]
        end
    end
```

## 🧪 Testing y Calidad

### Tests Automatizados
```plantuml
@startuml
package "Test Suite" {
  class StandardModelTests {
    +test_model_validation()
    +test_component_factory()
    +test_component_validation()
  }
  
  class XMLValidationTests {
    +test_xml_structure_validation()
    +test_aws_components_validation()
    +test_diagram_completeness()
  }
  
  class TemplateGenerationTests {
    +test_network_template_generation()
    +test_xml_generation_from_template()
    +test_component_style_mapping()
  }
  
  class MCPIntegrationTests {
    +test_mcp_to_standard_conversion()
    +test_mcp_xml_validation()
  }
  
  class EndToEndTests {
    +test_complete_workflow()
    +test_file_operations()
  }
}
@enduml
```

### Métricas de Calidad
```mermaid
pie title Cobertura de Tests
    "StandardModel" : 23
    "XMLValidation" : 23
    "TemplateGeneration" : 23
    "MCPIntegration" : 15
    "EndToEnd" : 16
```

## 🔧 Configuración y Extensibilidad

### Variables de Entorno
```mermaid
graph LR
    subgraph "Environment Variables"
        A[DEBUG=false]
        B[LOG_LEVEL=INFO]
        C[OUTPUT_FORMAT=both]
        D[AWS_REGION=us-east-1]
        E[PROJECT_NAME=mcp_diagrams]
    end
    
    subgraph "AppConfig"
        F[Configuration Manager]
    end
    
    A --> F
    B --> F
    C --> F
    D --> F
    E --> F
```

### Extensión Multi-Cloud
```plantuml
@startuml
abstract class CloudComponent {
    +String provider
    +String region
    +validate() bool
}

class AWSComponent extends CloudComponent {
    +String aws_service_type
}

class AzureComponent extends CloudComponent {
    +String azure_service_type
}

class GCPComponent extends CloudComponent {
    +String gcp_service_type
}

class MultiCloudFactory {
    +create_component(provider, type) CloudComponent
}

MultiCloudFactory --> CloudComponent
@enduml
```

## 📊 Métricas de Performance

```mermaid
gantt
    title Tiempos de Generación
    dateFormat X
    axisFormat %s
    
    section Configuración
    Carga Config     :0, 1s
    
    section Generación
    Prompts (3)      :1s, 2s
    Docs (4)         :2s, 4s
    PNG (4)          :4s, 8s
    DrawIO (1)       :8s, 9s
    
    section Validación
    XML Validation   :9s, 10s
    
    section Total
    Flujo Completo   :0, 10s
```

## 🚀 Roadmap Técnico

### Evolución de Arquitectura
```mermaid
timeline
    title Roadmap de Arquitectura
    
    section v4.1.0 (Actual)
        : Configuración Dinámica
        : Generadores Básicos
        : Validación XML
        : Tests Automatizados
    
    section v4.2.0 (Multi-Cloud)
        : Soporte Azure
        : Soporte GCP
        : Templates Multi-Provider
        : Validación Cross-Cloud
    
    section v4.3.0 (IA Integration)
        : Layout Automático IA
        : Optimización Visual
        : Generación desde Código
        : Análisis Dependencias
    
    section v5.0.0 (Platform)
        : Dashboard Web
        : Colaboración Real-Time
        : Versionado Diagramas
        : Integración CI/CD
```

---

**Esta arquitectura garantiza escalabilidad, mantenibilidad y extensibilidad para evolucionar hacia una plataforma enterprise completa con diagramas editables en código.**
