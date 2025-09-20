# MCP Diagram Generator

Generador unificado de diagramas, prompts y documentación para arquitecturas AWS.

## 🏗️ Estructura del Proyecto

```
├── src/                    # Código fuente principal
│   ├── core/              # Módulos core (config, utils)
│   ├── generators/        # Generadores (diagramas, prompts, docs)
│   ├── parsers/           # Parsers de especificaciones
│   ├── cases/             # Casos de uso específicos
│   └── main.py            # Punto de entrada principal
├── tools/                 # Herramientas y scripts
│   ├── scripts/           # Scripts de automatización
│   └── utilities/         # Utilidades de desarrollo
├── config/                # Configuraciones del proyecto
├── outputs/               # Archivos generados
├── docs/                  # Documentación
└── tests/                 # Tests unitarios
```

## 🚀 Uso

```bash
# Generar diagramas BMC
python src/main.py --case bmc-input

# Ver estructura generada
ls outputs/mcp/
```

## 📦 Componentes Principales

### Generadores
- **DiagramGenerator** - Diagramas PNG/DrawIO
- **MCPGenerator** - Diagramas Mermaid unificados  
- **PromptGenerator** - Prompts especializados MCP
- **DocGenerator** - Documentación de implementación

### Parsers
- **BMCInputParser** - Parser de especificaciones BMC

### Core
- **ConfigManager** - Gestión de configuración única

## 🎯 Características

- ✅ Generación unificada desde configuración MCP
- ✅ Diagramas Mermaid, PNG y DrawIO
- ✅ Prompts especializados por rol
- ✅ Documentación técnica automática
- ✅ Estructura organizada sin duplicados
