# Uso del Modelo MCP Integrado con Index.md

## Flujo Integrado

El sistema ahora usa el `index.md` estructurado como fuente de datos para todos los MCPs:

### 1. Workflow Completo
```bash
# Ejecutar todas las fases usando datos del index.md
python3 mcp-workflow.py complete
```

### 2. Fases Individuales con Datos del Index
```bash
# Precaracterización basada en index.md
python3 mcp-workflow.py prechar

# Estructuración usando contexto del index.md  
python3 mcp-workflow.py estructura

# Catálogo derivado de funcionalidades del index.md
python3 mcp-workflow.py catalogo

# Lineamientos basados en requerimientos del index.md
python3 mcp-workflow.py lineamientos
```

### 3. MCPs Originales (Independientes)
```bash
# MCPs originales sin integración
python3 mcp-precaracterizacion.py proposal
python3 mcp-estructuracion.py architecture
python3 mcp-catalogo.py catalog
python3 mcp-lineamientos.py standards
```

### 4. Parser del Index
```bash
# Parsear contenido estructurado
python3 mcp-parser.py parse

# Contexto de migración
python3 mcp-parser.py context
```

## Ventajas del Modelo Integrado

1. **Consistencia:** Todos los MCPs usan la misma fuente de datos
2. **Trazabilidad:** Cada output referencia el index.md como fuente
3. **Actualización:** Cambios en index.md se reflejan en todos los MCPs
4. **Contextualización:** Recomendaciones específicas basadas en datos reales

## Flujo Recomendado

1. **Actualizar index.md** con información del sistema
2. **Ejecutar workflow completo** para generar todas las fases
3. **Revisar outputs** por fase individual si es necesario
4. **Usar MCPs independientes** para análisis específicos

## Ejemplo de Uso

```bash
# 1. Verificar que index.md esté actualizado
cat index.md

# 2. Generar análisis completo
python3 mcp-workflow.py complete > bmc-analysis-complete.json

# 3. Revisar fase específica
python3 mcp-workflow.py estructura > bmc-architecture.json
```
