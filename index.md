# BMC - Bolsa Comisionista

## Sistema Regulatorio

**Entidad:** Bolsa Comisionista (Ente Regulador)
**Función Principal:** Procesamiento de facturas y cálculo de comisiones

## Características del Sistema

### Volumen de Datos
- **Productos:** 60M registros migrados desde Google Cloud
- **Tipos de Productos:** 16,000 categorías
- **Procesamiento:** Facturas individuales y por lotes

### Funcionalidades Backend
- APIs para procesamiento de facturas
- Base de datos de productos (migración desde Google)
- Desagregación por producto
    - Se requiere realziar una analiss de la factura con el la base de datos de prductos
    - Se debe entregar al front el listado de productos
- Cálculos de comisión (lote y individual)

### Funcionalidades Frontend
- Formularios web para carga de datos
    - Esta el serivio de caga de factiuras en imagene o pdf
- Opciones de exportación (PDF y Excel)
- Sistema de carga de archivos:
  - Archivos individuales
  - Archivos ZIP
  - Facturas pueden repetirse
- Procesamiento en background

### Clasificación DIAN
**Categorías principales:**
1. Alimentos (leche, carne, huevos)
2. Cantidad
3. Unidad

### Validaciones del Sistema
**Primera validación:**
- Producto
- Cantidad 
- Unidad

**Segunda validación:**
- Producto
- Clasificación de producto
- Unidad

### Arquitectura de Base de Datos
**Transaccional:**
- PostgreSQL principal

**Analítica:**
- Redshift para reportería

**Procesamiento:**
- Text processing para clasificación
- Búsqueda y matching de productos
- Campos vacíos cuando no se encuentra coincidencia

### Flujo de Negocio
1. **Carga de facturas** → Tabla de facturas
2. **Botón calcular** → Aplicación de reglas de negocio
3. **Generación de certificado** → PDF descargable o envío por correo

### Integraciones Externas
**SFTP Integration:**
- Transmisión de archivos con otros sistemas
- Intercambio de datos regulatorios

