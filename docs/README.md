# BMC MCP Documentation

## 📋 Specifications

Este directorio contiene únicamente las especificaciones MCP (Model Context Protocol) para el proyecto BMC.

### 📁 Estructura

```
docs/
├── specifications/
│   ├── bmc-input-specification.md      # Especificación de entrada BMC
│   ├── mcp-diagrams-architecture.md    # MCP principal para diagramas
│   ├── mcp-refined-architecture.md     # MCP refinado profesional
│   ├── mcp-aws-model.md               # Modelo AWS genérico
│   ├── mcp-arquitectura-bmc.md        # Arquitectura BMC original
│   ├── mcp-arquitectura-bmc-updated.md # Arquitectura BMC actualizada
│   └── config/                        # Configuraciones JSON
└── README.md                          # Este archivo
```

### 🎯 Uso de Especificaciones

#### Especificación Principal
```bash
# Usar especificación BMC como entrada
./run.sh --case bmc-input
# Lee: docs/specifications/bmc-input-specification.md
```

#### MCP Diagramas
```bash
# Usar MCP de diagramas
./run.sh --case bmc
# Lee: docs/specifications/mcp-diagrams-architecture.md
```

#### MCP Refinado
```bash
# Usar MCP refinado profesional
./run.sh --case refined
# Lee: docs/specifications/mcp-refined-architecture.md
```

### 📊 Outputs

**Todos los archivos generados van a `outputs/`:**
- PNG profesionales
- Draw.io editables
- Reportes de generación
- Documentación generada

### 🔄 Flujo de Trabajo

1. **Especificación** → `docs/specifications/`
2. **Procesamiento** → Parsers MCP
3. **Generación** → Diagramas + Documentación
4. **Salida** → `outputs/{proyecto}/`

### 📝 Tipos de Especificaciones

#### 1. BMC Input Specification
- Especificación de negocio en lenguaje natural
- Requerimientos funcionales y no funcionales
- Volúmenes de datos y KPIs
- Integraciones externas

#### 2. MCP Architecture
- Model Context Protocol estructurado
- Configuración de microservicios
- Servicios AWS específicos
- Métricas y performance

#### 3. MCP Refined
- Versión profesional optimizada
- Diagramas enterprise-grade
- Configuraciones avanzadas
- Compliance y seguridad

### 🎨 Generación de Diagramas

Las especificaciones se transforman automáticamente en:
- **PNG** - Para presentaciones
- **Draw.io** - Para colaboración técnica
- **Reportes** - Con metadata completa

### 📈 Evolución

- **v1.0** - Especificaciones básicas
- **v2.0** - MCP estructurado + Output Manager
- **v2.1** - Validación y corrección automática

---

**📍 Nota:** Solo especificaciones en `docs/`. Todos los outputs en `outputs/`.
