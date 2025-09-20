# Configuración BMC - Archivo Único

## 📁 Estructura Actual

```
config/
├── bmc-consolidated-config.json    # ✅ ARCHIVO ÚNICO ACTIVO
├── backup/                         # 📦 Archivos antiguos
│   ├── bmc-analysis-complete.json
│   ├── bmc-analysis-updated.json
│   ├── mcp-config.json
│   └── bmc-workflow-complete-with-diagrams.json
└── README.md                       # 📖 Esta documentación
```

## ✅ Configuración Consolidada

**Archivo activo:** `bmc-consolidated-config.json`
- **Versión:** 2.0.0
- **Proyecto:** BMC Bolsa Comisionista
- **Consolidado:** 2025-09-19

### Contenido Consolidado
- Configuración de workflow completa
- Información del proyecto BMC
- Configuración del servidor MCP
- Metadatos de consolidación

## 🔧 Scripts de Gestión

### Validar configuración única
```bash
python3 validate_single_config.py
```

### Re-consolidar si es necesario
```bash
python3 consolidate_config.py
```

## 📋 Reglas de Configuración

1. **Solo un archivo activo:** `bmc-consolidated-config.json`
2. **Backups automáticos:** Los archivos antiguos se mueven a `backup/`
3. **Validación:** Usar `validate_single_config.py` antes de generar diagramas
4. **Versionado:** Cada consolidación incrementa la versión

## 🚫 Archivos Deprecados

Los siguientes archivos están en `backup/` y NO deben usarse:
- `bmc-analysis-complete.json`
- `bmc-analysis-updated.json`
- `mcp-config.json`
- `bmc-workflow-complete-with-diagrams.json`

## 🎯 Uso en Generación

El sistema ahora usa automáticamente el archivo consolidado único:
```python
from core.config_manager import ConfigManager

manager = ConfigManager()
config = manager.load_config()  # Carga bmc-consolidated-config.json
```
