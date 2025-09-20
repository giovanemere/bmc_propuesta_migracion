# MCP Diagram Generator v3.1.0

## 🎉 Nueva Característica Principal

### 📝 Generador de Prompts MCP
- **3 tipos de prompts especializados**: Arquitectura, Migración, Implementación
- **Especificaciones técnicas detalladas** extraídas de configuración BMC
- **Prompts contextualizados** para arquitectos, desarrolladores y especialistas
- **Métricas de rendimiento** incluidas (60M productos, 10K facturas/hora)
- **Compliance regulatorio** DIAN integrado

## 🔧 Mejoras Técnicas

### Prompts Generados
- **`architecture_prompt.md`** - Contexto del sistema y diseño AWS
- **`implementation_prompt.md`** - Especificaciones técnicas y código
- **`migration_prompt.md`** - Estrategia Strangler Fig y plan detallado

### Integración Automática
- Generación automática con `python3 main.py --case bmc-input`
- Ubicación organizada en `outputs/mcp/prompts/`
- Script `show_mcp_prompts.py` para visualización

## 📊 Contenido de Prompts

### Arquitectura
- 5 microservicios mapeados con recursos AWS
- Consideraciones de escalamiento y alta disponibilidad
- Patrones de diseño para compliance regulatorio

### Implementación  
- Performance KPIs específicos (< 300ms lookup, > 95% OCR)
- Configuración de infraestructura AWS detallada
- Especificaciones de seguridad y monitoreo

### Migración
- Patrón Strangler Fig con 4 fases definidas
- Análisis de riesgos y mitigaciones
- Plan de rollback y validación

## 🛠️ Herramientas Actualizadas

```bash
# Generar todos los artefactos MCP (diagramas + prompts)
python3 main.py --case bmc-input

# Visualizar prompts generados
python3 show_mcp_prompts.py

# Validar estructura completa
python3 validate_single_config.py
```

## 📁 Archivos del Release

- `bmc_mcp_diagrams_v3.1.0.zip` - Diagramas, prompts y configuración MCP
- `mcp_generator_source_v3.1.0.zip` - Código fuente con generador de prompts

## 🔄 Actualización desde v3.0.0

Los usuarios de v3.0.0 pueden actualizar ejecutando:
```bash
git pull origin main
python3 main.py --case bmc-input
```

Los prompts se generarán automáticamente en la estructura MCP existente.

Generado: 2025-09-19 20:44:41
