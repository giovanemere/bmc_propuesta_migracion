# 🚀 BMC Diagram Generator - Guía de Uso

## 📋 Scripts Disponibles

### 1. **Script Principal Python** - `run.py`
Script completo con todas las opciones avanzadas.

```bash
# Ver ayuda completa
python run.py --help

# Flujo completo
python run.py --run complete

# Por secciones
python run.py --run config     # Solo configuración
python run.py --run png        # Solo PNG
python run.py --run drawio     # Solo DrawIO
python run.py --run prompts    # Solo prompts MCP
python run.py --run docs       # Solo documentación

# Limpieza
python run.py --clean all      # Limpiar todo
python run.py --clean png      # Solo PNG
python run.py --clean drawio   # Solo DrawIO

# Estado del sistema
python run.py --status

# Combinaciones
python run.py --clean png --run png    # Limpiar y regenerar PNG
```

### 2. **Script de Limpieza** - `clean.sh`
Limpieza rápida y simple.

```bash
# Limpiar todo
./clean.sh
./clean.sh all

# Por secciones
./clean.sh png      # Solo PNG
./clean.sh drawio   # Solo DrawIO
./clean.sh docs     # Solo documentación
./clean.sh prompts  # Solo prompts
./clean.sh config   # Solo configuración

# Ver estado
./clean.sh status
```

### 3. **Script de Generación** - `generate.sh`
Generación rápida y simple.

```bash
# Flujo completo
./generate.sh
./generate.sh complete

# Por secciones
./generate.sh config   # Solo configuración
./generate.sh png      # Solo PNG
./generate.sh drawio   # Solo DrawIO
./generate.sh prompts  # Solo prompts
./generate.sh docs     # Solo documentación

# Limpiar y regenerar
./generate.sh clean
```

## 🎯 Casos de Uso Comunes

### **Desarrollo y Testing**
```bash
# Limpiar y regenerar solo PNG para testing
./clean.sh png && ./generate.sh png

# Ver qué archivos se generaron
./clean.sh status
python run.py --status
```

### **Regeneración Completa**
```bash
# Opción 1: Script bash
./generate.sh clean

# Opción 2: Script python
python run.py --clean all --run complete
```

### **Desarrollo Incremental**
```bash
# Solo cambiar configuración
./generate.sh config

# Solo regenerar diagramas
./clean.sh png drawio
./generate.sh png
./generate.sh drawio
```

### **Verificación de Estado**
```bash
# Ver archivos generados
python run.py --status

# Estructura de directorios
./clean.sh status
```

## 📊 Archivos Generados

### **Estructura Esperada:**
```
outputs/
├── png/bmc_input/                    # 4 archivos PNG
│   ├── network_architecture.png
│   ├── microservices_detailed.png
│   ├── security_architecture.png
│   └── data_flow.png
├── drawio/bmc_input/                 # 2 archivos DrawIO
│   ├── complete_architecture.drawio
│   └── dynamic_architecture_*.drawio
├── prompts/bmc_input/                # 3 prompts MCP
│   ├── architecture_prompt.md
│   ├── implementation_prompt.md
│   └── migration_prompt.md
├── documentation/bmc_input/          # 5 documentos
│   ├── technical_architecture.md
│   ├── implementation_guide.md
│   ├── migration_plan.md
│   ├── infrastructure_config.md
│   └── bmc_input_report.md
└── generated/                        # 3 configuraciones
    ├── bmc.json
    ├── bmc_input_consolidated.json
    └── bmc_input_results.json
```

### **Total: 17 archivos**
- 🎨 **4 PNG** (diagramas visuales)
- 📐 **2 DrawIO** (editables)
- 🎯 **3 Prompts** (MCP especializados)
- 📚 **5 Documentos** (técnicos)
- ⚙️ **3 Configuraciones** (JSON)

## 🔧 Troubleshooting

### **Error: Módulo no encontrado**
```bash
# Verificar PYTHONPATH
export PYTHONPATH="$(pwd)/src:$(pwd):$PYTHONPATH"
python run.py --status
```

### **Error: Entorno virtual**
```bash
# Activar entorno virtual
source venv/bin/activate
pip install -r requirements.txt
```

### **Error: Permisos**
```bash
# Hacer ejecutables los scripts
chmod +x clean.sh generate.sh
```

### **Error: Especificación no encontrada**
```bash
# Verificar que existe el archivo fuente
ls -la config/bmc-input-specification.md
```

## 🚀 Flujo de Trabajo Recomendado

### **1. Primera Ejecución**
```bash
# Generar todo desde cero
./generate.sh complete
```

### **2. Desarrollo Iterativo**
```bash
# Editar especificación
vim config/bmc-input-specification.md

# Regenerar solo lo necesario
./generate.sh config
./generate.sh png
```

### **3. Verificación**
```bash
# Ver estado
python run.py --status

# Ver archivos específicos
ls -la outputs/png/bmc_input/
ls -la outputs/drawio/bmc_input/
```

### **4. Limpieza Periódica**
```bash
# Limpiar archivos antiguos
./clean.sh all

# Regenerar desde cero
./generate.sh complete
```

## 📋 Comandos de Referencia Rápida

| Acción | Comando Rápido | Comando Completo |
|--------|----------------|------------------|
| **Generar todo** | `./generate.sh` | `python run.py --run complete` |
| **Limpiar todo** | `./clean.sh` | `python run.py --clean all` |
| **Solo PNG** | `./generate.sh png` | `python run.py --run png` |
| **Solo DrawIO** | `./generate.sh drawio` | `python run.py --run drawio` |
| **Ver estado** | `./clean.sh status` | `python run.py --status` |
| **Limpiar y regenerar** | `./generate.sh clean` | `python run.py --clean all --run complete` |

---

**¡El sistema está listo para usar con scripts simples y potentes!** 🎉
