# 🎨 Instrucciones para Generar Diagramas PNG

## 📋 Archivos Draw.io Creados

✅ **3 Diagramas Draw.io listos:**

1. **`drawio/bmc-context-diagram.drawio`**
   - Diagrama de Contexto (C4 Level 1)
   - Usuarios, Sistema BMC, Entidades Regulatorias

2. **`drawio/bmc-container-diagram.drawio`**
   - Diagrama de Contenedores (C4 Level 2)  
   - Frontend, API, Microservicios, Data Layer, Integraciones

3. **`drawio/bmc-aws-infrastructure.drawio`**
   - Infraestructura AWS Completa
   - VPC, Subnets, ECS, RDS, Lambda, Monitoring

## 🛠️ Métodos para Generar PNG

### Método 1: Draw.io Web (Más Fácil)

1. **Abrir** [app.diagrams.net](https://app.diagrams.net)
2. **Cargar archivo:** `File > Open from > Device`
3. **Seleccionar** archivo `.drawio`
4. **Exportar PNG:** `File > Export as > PNG`
5. **Configurar calidad:** 
   - Resolution: 300 DPI (alta calidad)
   - Zoom: 100%
   - Border Width: 0
6. **Descargar** archivo PNG

### Método 2: Script Automático

```bash
# Ejecutar script de conversión
./generate-png-diagrams.sh
```

**Requisitos:**
- Draw.io desktop app, O
- Docker instalado, O  
- Draw.io CLI

### Método 3: Draw.io Desktop

1. **Descargar:** [draw.io desktop](https://github.com/jgraph/drawio-desktop/releases)
2. **Instalar** aplicación
3. **Abrir** archivos `.drawio`
4. **Exportar:** `File > Export as > PNG`

### Método 4: Docker (Automático)

```bash
# Crear directorio PNG
mkdir -p drawio/png

# Convertir cada diagrama
docker run --rm -v "$(pwd)":/data minlag/drawio-cli \
  -f png -o /data/drawio/png/bmc-context-diagram.png \
  /data/drawio/bmc-context-diagram.drawio

docker run --rm -v "$(pwd)":/data minlag/drawio-cli \
  -f png -o /data/drawio/png/bmc-container-diagram.png \
  /data/drawio/bmc-container-diagram.drawio

docker run --rm -v "$(pwd)":/data minlag/drawio-cli \
  -f png -o /data/drawio/png/bmc-aws-infrastructure.png \
  /data/drawio/bmc-aws-infrastructure.drawio
```

## 📊 Configuraciones Recomendadas

### Para Presentaciones
- **Formato:** PNG
- **Resolución:** 300 DPI
- **Tamaño:** Ajustar al contenido
- **Fondo:** Transparente o blanco

### Para Documentación
- **Formato:** PNG o SVG
- **Resolución:** 150-300 DPI
- **Compresión:** Media-Alta calidad

### Para Web
- **Formato:** PNG optimizado
- **Resolución:** 72-150 DPI
- **Tamaño:** Máximo 2MB por imagen

## 🎯 Características de los Diagramas

### Diagrama de Contexto
- **Dimensiones:** ~1200x800px
- **Elementos:** 7 actores principales
- **Colores:** Codificados por tipo
- **Uso:** Presentaciones ejecutivas

### Diagrama de Contenedores  
- **Dimensiones:** ~1400x1000px
- **Elementos:** 25+ componentes AWS
- **Capas:** 5 layers arquitectónicos
- **Uso:** Revisiones técnicas

### Infraestructura AWS
- **Dimensiones:** ~1600x1200px
- **Elementos:** 30+ servicios AWS
- **Detalle:** VPC, subnets, instancias
- **Uso:** Implementación técnica

## 📁 Estructura Final

```
drawio/
├── README.md
├── bmc-context-diagram.drawio
├── bmc-container-diagram.drawio  
├── bmc-aws-infrastructure.drawio
└── png/
    ├── bmc-context-diagram.png
    ├── bmc-container-diagram.png
    └── bmc-aws-infrastructure.png
```

## ✅ Checklist de Calidad

### Antes de Exportar
- [ ] Verificar que todos los textos sean legibles
- [ ] Confirmar que los colores sean consistentes
- [ ] Validar que las conexiones estén claras
- [ ] Revisar ortografía y terminología técnica

### Después de Exportar
- [ ] Verificar calidad de imagen (300 DPI mínimo)
- [ ] Confirmar que el tamaño sea apropiado (<5MB)
- [ ] Validar que todos los elementos sean visibles
- [ ] Probar visualización en diferentes dispositivos

## 🚀 Próximos Pasos

1. **Generar PNG** usando método preferido
2. **Revisar calidad** de imágenes exportadas
3. **Usar en presentaciones** y documentación
4. **Actualizar** según feedback de stakeholders
5. **Mantener sincronizado** con cambios de arquitectura

## 💡 Tips Adicionales

- **Backup:** Mantener archivos `.drawio` como fuente
- **Versionado:** Usar Git para control de versiones
- **Colaboración:** Compartir archivos `.drawio` para edición
- **Presentaciones:** Usar PNG de alta resolución
- **Web:** Optimizar PNG para carga rápida
