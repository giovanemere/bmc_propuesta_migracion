# 📋 Casos de Uso y Componentes - MCP Diagram Generator

## 🎯 Casos de Uso Principales

### 1. Generación Automática de Diagramas
**Actor:** Arquitecto de Software / DevOps Engineer
**Objetivo:** Generar diagramas profesionales desde especificaciones

**Flujo Principal:**
1. Proporcionar especificación del proyecto (JSON/YAML/Markdown)
2. Sistema procesa y valida la especificación
3. Genera automáticamente:
   - 4 diagramas PNG (network, microservices, security, data_flow)
   - 1 diagrama DrawIO editable
   - 3 diagramas Mermaid (architecture, dataflow, migration)
4. Valida calidad y completitud
5. Entrega archivos listos para documentación

**Criterios de Aceptación:**
- ✅ Diagramas generados en < 30 segundos
- ✅ Calidad visual profesional (iconos AWS oficiales)
- ✅ DrawIO 100% editable
- ✅ Validación automática de completitud

### 2. Integración con Modelo MCP Existente
**Actor:** Desarrollador del Proyecto
**Objetivo:** Integrar con configuración MCP existente sin cambios

**Flujo Principal:**
1. Sistema lee configuración MCP actual (`config/bmc-config.json`)
2. Convierte automáticamente a modelo estándar
3. Genera diagramas manteniendo coherencia con MCP
4. Valida que todos los microservicios estén representados
5. Guarda resultados en estructura organizada

**Criterios de Aceptación:**
- ✅ 0 cambios requeridos en configuración MCP
- ✅ 100% microservicios representados
- ✅ Validación automática MCP ↔ Diagramas
- ✅ Estructura de salida organizada

### 3. Generación de Documentación Técnica
**Actor:** Technical Writer / Project Manager
**Objetivo:** Generar documentación técnica automática

**Flujo Principal:**
1. Analizar especificación del proyecto
2. Generar prompts MCP especializados
3. Crear documentación técnica:
   - Arquitectura técnica
   - Guía de implementación
   - Plan de migración
   - Configuración de infraestructura
4. Generar reporte ejecutivo
5. Organizar en estructura profesional

**Criterios de Aceptación:**
- ✅ 4+ documentos técnicos generados
- ✅ Prompts MCP listos para uso
- ✅ Reporte ejecutivo con métricas
- ✅ Formato profesional (Markdown)

### 4. Validación y Control de Calidad
**Actor:** QA Engineer / Arquitecto Senior
**Objetivo:** Asegurar calidad profesional de diagramas

**Flujo Principal:**
1. Ejecutar tests automatizados (13 tests)
2. Validar estructura XML de DrawIO
3. Verificar iconos AWS oficiales
4. Comprobar completitud vs especificación
5. Generar métricas de calidad
6. Reportar estado de validación

**Criterios de Aceptación:**
- ✅ 100% tests automatizados passing
- ✅ XML DrawIO válido y bien formado
- ✅ Iconos AWS oficiales (mxgraph.aws4)
- ✅ Métricas de calidad > 90%

### 5. API REST para Integración
**Actor:** Desarrollador Frontend / Sistema Externo
**Objetivo:** Integrar generación via API REST

**Flujo Principal:**
1. Enviar especificación via POST /api/v1/diagrams/generate
2. Sistema procesa asincrónicamente
3. Retorna URLs de descarga de archivos
4. Permite validación via GET /api/v1/diagrams/validate
5. Soporte para batch processing

**Criterios de Aceptación:**
- ✅ API REST completa documentada
- ✅ Endpoints de validación y generación
- ✅ Soporte para múltiples formatos
- ✅ Manejo de errores robusto

## 🏗️ Componentes de la Arquitectura

### Core Components

#### 1. App Config (`src/core/app_config.py`)
**Responsabilidad:** Configuración transversal y gestión de rutas
**Funciones:**
- Gestión centralizada de paths
- Carga/guardado de configuraciones
- Variables de entorno
- Cache de configuraciones

**APIs Principales:**
```python
get_config(config_name: str) -> Dict[str, Any]
save_config(config_name: str, config_data: Dict[str, Any]) -> str
get_output_path(file_type: str, filename: str) -> Path
```

#### 2. Workflow Orchestrator (`src/core/workflow_orchestrator.py`)
**Responsabilidad:** Orquestación del flujo completo
**Funciones:**
- Coordinación de generadores
- Validación de flujo
- Consolidación de resultados
- Reporte final

**APIs Principales:**
```python
execute_complete_workflow() -> Dict[str, Any]
run_complete_workflow(project_name: str) -> Dict[str, Any]
```

### Generators

#### 3. Universal Generator (`src/generators/universal_generator.py`)
**Responsabilidad:** Generación unificada PNG + DrawIO
**Funciones:**
- Mapeo PNG ↔ DrawIO
- Layout automático
- Estilos AWS oficiales
- Validación de salida

#### 4. Diagram Generator (`src/generators/diagram_generator.py`)
**Responsabilidad:** Generación PNG especializada
**Funciones:**
- 4 tipos de diagramas PNG
- Clusters automáticos
- Iconos AWS reales
- Optimización visual

#### 5. Prompt Generator (`src/generators/prompt_generator.py`)
**Responsabilidad:** Generación de prompts MCP
**Funciones:**
- Prompts especializados
- Templates contextuales
- Análisis de especificaciones
- Formato profesional

#### 6. Doc Generator (`src/generators/doc_generator.py`)
**Responsabilidad:** Generación de documentación
**Funciones:**
- Documentos técnicos
- Guías de implementación
- Planes de migración
- Reportes ejecutivos

### Validators & Integrators

#### 7. XML Validator (`src/validators/xml_validator.py`)
**Responsabilidad:** Validación de calidad DrawIO
**Funciones:**
- Validación estructura XML
- Verificación componentes AWS
- Integración MCP
- Métricas de completitud

#### 8. MCP Integrator (dentro de XML Validator)
**Responsabilidad:** Integración con modelo MCP
**Funciones:**
- Conversión MCP → Modelo estándar
- Validación coherencia
- Mapeo automático
- Preservación de configuración

### Templates & Schemas

#### 9. DrawIO Templates (`templates/drawio_templates.py`)
**Responsabilidad:** Plantillas XML profesionales
**Funciones:**
- Templates base DrawIO
- Estilos AWS oficiales
- Generación XML válido
- Personalización visual

#### 10. Standard Input Model (`schemas/standard_input_model.json`)
**Responsabilidad:** Esquema estándar de entrada
**Funciones:**
- Validación JSON Schema
- 15+ tipos de componentes
- Estructura normalizada
- Documentación integrada

### Components Library

#### 11. AWS Components (`src/components/aws_components.py`)
**Responsabilidad:** Clases de componentes AWS
**Funciones:**
- Factory pattern
- 15 clases especializadas
- Validación automática
- Mapeo PNG ↔ DrawIO

### API & Testing

#### 12. Diagram API (`src/api/diagram_api.py`)
**Responsabilidad:** API REST completa
**Funciones:**
- Endpoints de generación
- Validación de esquemas
- Batch processing
- Manejo de errores

#### 13. Automated Tests (`tests/automated_quality_tests.py`)
**Responsabilidad:** Tests automatizados de calidad
**Funciones:**
- 13 tests automatizados
- Validación end-to-end
- Métricas de calidad
- Integración continua

## 📊 Matriz de Responsabilidades

| Componente | Generación | Validación | Integración | API | Tests |
|------------|------------|------------|-------------|-----|-------|
| **App Config** | - | - | ✅ | - | ✅ |
| **Workflow Orchestrator** | ✅ | ✅ | ✅ | - | ✅ |
| **Universal Generator** | ✅ | ✅ | - | - | ✅ |
| **Diagram Generator** | ✅ | - | - | - | ✅ |
| **XML Validator** | - | ✅ | ✅ | - | ✅ |
| **DrawIO Templates** | ✅ | ✅ | - | - | ✅ |
| **AWS Components** | ✅ | ✅ | - | - | ✅ |
| **Diagram API** | ✅ | ✅ | - | ✅ | ✅ |
| **Automated Tests** | - | ✅ | ✅ | ✅ | ✅ |

## 🎯 Criterios de Calidad Profesional

### Funcionales
- ✅ **Completitud:** 100% microservicios representados
- ✅ **Precisión:** Iconos AWS oficiales únicamente
- ✅ **Consistencia:** Misma entrada → mismo resultado
- ✅ **Integración:** 0 cambios en configuración MCP

### No Funcionales
- ✅ **Performance:** Generación < 30 segundos
- ✅ **Calidad:** Tests automatizados 100% passing
- ✅ **Mantenibilidad:** Código modular y documentado
- ✅ **Escalabilidad:** API REST para integración

### Técnicos
- ✅ **Validación:** XML bien formado y válido
- ✅ **Estándares:** JSON Schema para entrada
- ✅ **Documentación:** Casos de uso completos
- ✅ **Testing:** Cobertura end-to-end

## 🚀 Roadmap de Mejoras

### Versión 4.2.0
- [ ] Soporte para Azure/GCP
- [ ] Layout automático inteligente
- [ ] Temas visuales múltiples
- [ ] Exportación SVG/PDF

### Versión 4.3.0
- [ ] Colaboración en tiempo real
- [ ] Versionado de diagramas
- [ ] Integración CI/CD
- [ ] Métricas de uso

### Versión 5.0.0
- [ ] IA para optimización automática
- [ ] Generación desde código fuente
- [ ] Análisis de dependencias
- [ ] Dashboard web completo

---

**Esta documentación define los estándares profesionales que debe cumplir la aplicación para ser considerada enterprise-ready.**
