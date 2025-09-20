# 📁 Estructura de Archivos - MCP Diagram Generator

## 🎯 Principio de Organización

**Separación clara entre archivos fuente y archivos generados:**
- `config/` - Solo especificaciones y configuraciones estáticas
- `outputs/` - Todos los archivos generados dinámicamente

## 📂 Estructura Completa

```
📦 MCP Diagram Generator
├── 📁 config/                          # Configuraciones estáticas
│   ├── 📄 bmc-input-specification.md   # ✅ Especificación fuente (EDITABLE)
│   └── 📄 README.md                    # Documentación de config
├── 📁 outputs/                         # Archivos generados (NO EDITAR)
│   ├── 📁 generated/                   # Configuraciones dinámicas
│   │   ├── 📄 bmc.json                 # ✅ Config generada desde spec
│   │   ├── 📄 bmc_input_consolidated.json
│   │   └── 📄 bmc_input_results.json
│   ├── 📁 png/                         # Diagramas PNG
│   │   └── 📁 {project}/
│   ├── 📁 drawio/                      # Diagramas DrawIO
│   │   └── 📁 {project}/
│   ├── 📁 prompts/                     # Prompts MCP
│   │   └── 📁 {project}/
│   └── 📁 documentation/               # Documentación generada
│       └── 📁 {project}/
├── 📁 src/                             # Código fuente
├── 📁 docs/                            # Documentación del sistema
├── 📁 schemas/                         # Esquemas JSON
├── 📁 templates/                       # Plantillas
└── 📁 tests/                           # Tests automatizados
```

## 🔄 Flujo de Archivos

### Archivos Fuente (Editables)
```
📋 config/bmc-input-specification.md
    ↓ (DynamicConfigGenerator)
💾 outputs/generated/bmc.json
    ↓ (WorkflowOrchestrator)
📊 outputs/{png,drawio,prompts,documentation}/
```

### Reglas de Archivos

| Directorio | Propósito | Editable | Versionado |
|------------|-----------|----------|------------|
| **config/** | Especificaciones fuente | ✅ SÍ | ✅ SÍ |
| **outputs/generated/** | Configs dinámicas | ❌ NO | ❌ NO |
| **outputs/png/** | Diagramas PNG | ❌ NO | ❌ NO |
| **outputs/drawio/** | Diagramas DrawIO | ❌ NO | ❌ NO |
| **outputs/prompts/** | Prompts generados | ❌ NO | ❌ NO |
| **outputs/documentation/** | Docs generadas | ❌ NO | ❌ NO |
| **src/** | Código fuente | ✅ SÍ | ✅ SÍ |
| **docs/** | Documentación sistema | ✅ SÍ | ✅ SÍ |

## 🎯 Beneficios de esta Estructura

### ✅ Ventajas
- **Separación clara:** Fuente vs generado
- **Sin confusión:** Solo editar archivos en config/
- **Sin cache:** Archivos generados siempre frescos
- **Versionado limpio:** Solo fuentes en Git
- **Regeneración:** Eliminar outputs/ regenera todo

### ❌ Problemas Evitados
- Editar archivos generados por error
- Conflictos entre archivos estáticos y dinámicos
- Cache de configuraciones obsoletas
- Confusión sobre qué archivos editar

## 🔧 Comandos de Mantenimiento

### Limpiar Archivos Generados
```bash
# Eliminar todos los archivos generados
rm -rf outputs/

# El sistema regenerará automáticamente desde config/
python src/main.py
```

### Regenerar Configuración
```bash
# Forzar regeneración desde especificación
python -c "
from src.core.dynamic_config_generator import generate_dynamic_config
generate_dynamic_config(force_regenerate=True)
"
```

### Verificar Estructura
```bash
# Ver archivos fuente (editables)
find config/ src/ docs/ schemas/ templates/ tests/ -name "*.py" -o -name "*.md" -o -name "*.json"

# Ver archivos generados (no editar)
find outputs/ -type f
```

## 📋 Checklist de Desarrollo

### ✅ Al Agregar Nueva Funcionalidad
- [ ] Código fuente en `src/`
- [ ] Tests en `tests/`
- [ ] Documentación en `docs/`
- [ ] Esquemas en `schemas/` si aplica
- [ ] **NO** agregar archivos en `outputs/`

### ✅ Al Cambiar Configuración
- [ ] Editar solo `config/bmc-input-specification.md`
- [ ] **NO** editar `outputs/generated/bmc.json`
- [ ] Ejecutar sistema para regenerar
- [ ] Verificar archivos generados

### ✅ Al Hacer Commit
- [ ] Incluir archivos de `config/`, `src/`, `docs/`
- [ ] **NO** incluir archivos de `outputs/`
- [ ] Agregar `outputs/` a `.gitignore` si no está

## 🚨 Archivos Críticos

### 📋 Archivo Fuente Principal
```
config/bmc-input-specification.md
```
**Este es el ÚNICO archivo que define la configuración del proyecto BMC.**

### 💾 Archivo Generado Principal
```
outputs/generated/bmc.json
```
**Este archivo se genera automáticamente. NUNCA editarlo manualmente.**

## 🔍 Troubleshooting

### Problema: Configuración no se actualiza
```bash
# Verificar timestamps
ls -la config/bmc-input-specification.md
ls -la outputs/generated/bmc.json

# Forzar regeneración
rm outputs/generated/bmc.json
python src/main.py
```

### Problema: Archivos generados corruptos
```bash
# Limpiar y regenerar todo
rm -rf outputs/
python src/main.py
```

### Problema: Cache de configuración
```bash
# El sistema usa cache inteligente basado en timestamps
# Si hay problemas, reiniciar Python limpia el cache
```

---

**Esta estructura garantiza separación clara entre archivos fuente y generados, evitando confusiones y problemas de cache.**
