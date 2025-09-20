# 🔄 Diagramas de Secuencia - Workflow Completo

## 📋 Proceso End-to-End Actual

### 1. Secuencia Principal - Generación Completa

```mermaid
sequenceDiagram
    participant User as 👤 Usuario
    participant Spec as 📋 bmc-input-specification.md
    participant DynGen as 🔄 DynamicConfigGenerator
    participant WO as 🎮 WorkflowOrchestrator
    participant AppConfig as ⚙️ AppConfig
    participant PG as 🎯 PromptGenerator
    participant DG as 📚 DocGenerator
    participant UG as 📐 UniversalGenerator
    participant Val as ✅ Validator

    User->>Spec: 1. Edita especificación
    User->>WO: 2. Ejecuta run_complete_workflow()
    
    WO->>AppConfig: 3. get_config("bmc")
    AppConfig->>DynGen: 4. generate_dynamic_config()
    DynGen->>Spec: 5. Lee especificación
    DynGen->>DynGen: 6. Parsea microservicios
    DynGen->>DynGen: 7. Infiere servicios AWS
    DynGen-->>AppConfig: 8. Retorna config JSON
    AppConfig-->>WO: 9. Config consolidada
    
    WO->>PG: 10. Genera prompts MCP
    PG->>PG: 11. Crea 3 prompts especializados
    PG-->>WO: 12. outputs/prompts/bmc_input/
    
    WO->>DG: 13. Genera documentación
    DG->>DG: 14. Crea 4 documentos técnicos
    DG-->>WO: 15. outputs/documentation/bmc_input/
    
    WO->>UG: 16. Genera diagramas
    UG->>UG: 17. PNG + DrawIO
    UG-->>WO: 18. outputs/png/ + outputs/drawio/
    
    WO->>Val: 19. Valida calidad
    Val->>Val: 20. Tests automáticos
    Val-->>WO: 21. Métricas de calidad
    
    WO->>WO: 22. Consolida resultados
    WO-->>User: 23. Reporte final + archivos
```

### 2. Secuencia Detallada - Configuración Dinámica

```mermaid
sequenceDiagram
    participant Spec as 📋 Especificación MD
    participant DG as 🔄 DynamicGenerator
    participant FS as 💾 FileSystem
    participant Cache as 🗄️ Cache

    DG->>FS: 1. Verificar timestamp spec
    DG->>FS: 2. Verificar timestamp config
    
    alt Especificación más nueva
        DG->>Spec: 3. Leer contenido MD
        DG->>DG: 4. Regex: extraer microservicios
        Note over DG: Invoice, Product, OCR,<br/>Commission, Certificate
        DG->>DG: 5. Regex: inferir AWS services
        Note over DG: RDS, S3, ElastiCache
        DG->>FS: 6. Guardar outputs/generated/bmc.json
        DG->>Cache: 7. Actualizar cache
    else Configuración actual
        DG->>Cache: 3. Usar config existente
    end
    
    DG-->>Cache: 8. Retornar configuración
```

### 3. Secuencia de Generación de Diagramas

```mermaid
sequenceDiagram
    participant WO as 🎮 Orchestrator
    participant UG as 📐 UniversalGenerator
    participant DT as 📄 DrawIOTemplates
    participant MC as 🔄 MCPIntegrator
    participant Val as ✅ XMLValidator
    participant FS as 💾 FileSystem

    WO->>UG: 1. generate_diagrams(config)
    UG->>MC: 2. convert_mcp_to_standard_model()
    MC->>MC: 3. Mapea microservicios → componentes
    MC->>MC: 4. Mapea AWS services → infraestructura
    MC-->>UG: 5. StandardDiagramSchema
    
    UG->>DT: 6. generate_drawio_xml(schema)
    DT->>DT: 7. Aplica templates AWS
    DT->>DT: 8. Genera XML válido
    DT-->>UG: 9. DrawIO XML
    
    UG->>Val: 10. validate_xml(xml)
    Val->>Val: 11. Verifica estructura
    Val->>Val: 12. Valida componentes AWS
    Val-->>UG: 13. Métricas de calidad
    
    UG->>FS: 14. Guarda PNG + DrawIO
    UG-->>WO: 15. Rutas de archivos generados
```

## 📊 Estado Actual vs Esperado

### ✅ Lo que SÍ se está generando:
```
outputs/
├── generated/
│   ├── bmc.json (✅ Config dinámica)
│   └── bmc_input_consolidated.json (✅ Config consolidada)
```

### ❌ Lo que FALTA generar:
```
outputs/
├── png/bmc_input/
│   ├── network_architecture.png (❌ FALTA)
│   ├── microservices_detailed.png (❌ FALTA)
│   ├── security_architecture.png (❌ FALTA)
│   └── data_flow.png (❌ FALTA)
├── drawio/bmc_input/
│   └── complete_architecture.drawio (❌ FALTA)
├── prompts/bmc_input/
│   ├── architecture_prompt.md (❌ FALTA)
│   ├── implementation_prompt.md (❌ FALTA)
│   └── migration_prompt.md (❌ FALTA)
└── documentation/bmc_input/
    ├── technical_architecture.md (❌ FALTA)
    ├── implementation_guide.md (❌ FALTA)
    ├── migration_plan.md (❌ FALTA)
    └── infrastructure_config.md (❌ FALTA)
```

## 🔧 Workflow de Implementación End-to-End

### Fase 1: ✅ COMPLETADA - Configuración Dinámica
- [x] DynamicConfigGenerator funcional
- [x] Parsing desde bmc-input-specification.md
- [x] Generación automática de bmc.json
- [x] Cache inteligente por timestamps

### Fase 2: ❌ PENDIENTE - Generadores Funcionales
```mermaid
graph TD
    A[Config BMC] --> B[PromptGenerator]
    A --> C[DocGenerator]
    A --> D[DiagramGenerator]
    
    B --> B1[architecture_prompt.md]
    B --> B2[implementation_prompt.md]
    B --> B3[migration_prompt.md]
    
    C --> C1[technical_architecture.md]
    C --> C2[implementation_guide.md]
    C --> C3[migration_plan.md]
    C --> C4[infrastructure_config.md]
    
    D --> D1[network_architecture.png]
    D --> D2[microservices_detailed.png]
    D --> D3[security_architecture.png]
    D --> D4[data_flow.png]
    D --> D5[complete_architecture.drawio]
    
    style B fill:#ffcccc
    style C fill:#ffcccc
    style D fill:#ffcccc
```

### Fase 3: ❌ PENDIENTE - Validación y Calidad
- [ ] XMLValidator para DrawIO
- [ ] Tests automatizados end-to-end
- [ ] Métricas de calidad
- [ ] Reportes de completitud

## 🎯 Plan de Implementación Inmediata

### 1. Arreglar Generadores (CRÍTICO)
```python
# Problema actual: Imports relativos fallan
from ..generators.prompt_generator import MCPPromptGenerator  # ❌ FALLA

# Solución: Imports absolutos
from generators.prompt_generator import MCPPromptGenerator  # ✅ FUNCIONA
```

### 2. Completar Generación de Archivos
```bash
# Objetivo: Generar 11 archivos por proyecto
outputs/bmc_input/
├── 4 PNG (network, microservices, security, data_flow)
├── 1 DrawIO (complete_architecture)
├── 3 Prompts (architecture, implementation, migration)
└── 4 Docs (technical, guide, plan, config)
```

### 3. Validación Automática
```python
# Verificar que todos los archivos se generen
expected_files = [
    "outputs/png/bmc_input/network_architecture.png",
    "outputs/drawio/bmc_input/complete_architecture.drawio",
    "outputs/prompts/bmc_input/architecture_prompt.md",
    # ... 8 archivos más
]
```

## 📋 Checklist de Desarrollo

### ✅ Completado:
- [x] Configuración dinámica desde especificación
- [x] Estructura de archivos limpia
- [x] AppConfig transversal
- [x] Documentación de arquitectura

### 🔄 En Progreso:
- [ ] Arreglar imports en WorkflowOrchestrator
- [ ] Completar generadores de archivos
- [ ] Validación XML DrawIO

### ❌ Pendiente:
- [ ] Generación PNG real (4 diagramas)
- [ ] Generación DrawIO funcional
- [ ] Tests end-to-end completos
- [ ] API REST endpoints

## 🚨 Problemas Críticos Identificados

### 1. Imports Relativos Fallan
```python
# En workflow_orchestrator.py línea ~100
from ..generators.prompt_generator import MCPPromptGenerator  # ❌ FALLA
```

### 2. Generadores No Producen Archivos
- PromptGenerator existe pero no genera archivos
- DocGenerator existe pero no genera archivos  
- DiagramGenerator no se ejecuta correctamente

### 3. Validación Incompleta
- XMLValidator existe pero no se usa
- No hay verificación de archivos generados
- Falta validación de completitud

## 🎯 Próximos Pasos Inmediatos

1. **Arreglar imports** en WorkflowOrchestrator
2. **Completar generadores** para producir archivos reales
3. **Implementar validación** de archivos generados
4. **Crear tests** end-to-end funcionales
5. **Documentar inputs** para cada proceso

---

**El sistema tiene la arquitectura correcta pero los generadores no están produciendo los archivos esperados. Necesitamos completar la implementación de cada generador.**
