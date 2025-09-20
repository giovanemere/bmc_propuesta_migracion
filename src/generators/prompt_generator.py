#!/usr/bin/env python3
"""
MCP Prompt Generator - Genera prompts del modelo MCP
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class MCPPromptGenerator:
    """Generador de prompts MCP"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str = "outputs/mcp"):
        self.config = config
        self.output_dir = Path(output_dir)
        
    def generate_prompts(self, project_name: str = "bmc_input") -> Dict[str, str]:
        """Genera todos los prompts MCP"""
        
        prompts_dir = self.output_dir / project_name
        prompts_dir.mkdir(parents=True, exist_ok=True)
        
        results = {}
        
        # Prompt de arquitectura
        arch_prompt = self._generate_architecture_prompt()
        arch_file = prompts_dir / "architecture_prompt.md"
        with open(arch_file, 'w', encoding='utf-8') as f:
            f.write(arch_prompt)
        results["architecture"] = str(arch_file)
        
        # Prompt de migración
        migration_prompt = self._generate_migration_prompt()
        migration_file = prompts_dir / "migration_prompt.md"
        with open(migration_file, 'w', encoding='utf-8') as f:
            f.write(migration_prompt)
        results["migration"] = str(migration_file)
        
        # Prompt de implementación
        impl_prompt = self._generate_implementation_prompt()
        impl_file = prompts_dir / "implementation_prompt.md"
        with open(impl_file, 'w', encoding='utf-8') as f:
            f.write(impl_prompt)
        results["implementation"] = str(impl_file)
        
        print(f"✓ MCP prompts generated in {prompts_dir}")
        return results
    
    def _generate_architecture_prompt(self) -> str:
        """Genera prompt de arquitectura"""
        
        project = self.config.get("project", {})
        microservices = self.config.get("microservices", {})
        aws_services = self.config.get("aws_services", {})
        
        prompt = f"""# Prompt de Arquitectura MCP - {project.get('name', 'BMC')}

## Contexto del Sistema
**Proyecto:** {project.get('name', 'BMC Bolsa Comisionista')}
**Tipo:** {project.get('type', 'Sistema Regulatorio')}
**Función:** {project.get('main_function', 'Procesamiento de facturas')}

## Microservicios Identificados

"""
        
        for service_name, service_config in microservices.items():
            business_function = service_config.get('business_function', 'N/A')
            compute = service_config.get('compute', {})
            
            prompt += f"""### {service_name.replace('_', ' ').title()}
- **Función de negocio:** {business_function}
- **CPU:** {compute.get('cpu', 'N/A')} 
- **Memoria:** {compute.get('memory', 'N/A')}MB
- **Escalamiento:** {service_config.get('scaling', {}).get('min_capacity', 1)}-{service_config.get('scaling', {}).get('max_capacity', 5)} instancias

"""
        
        prompt += f"""## Servicios AWS Requeridos

"""
        
        for service_name, service_config in aws_services.items():
            service_type = service_config.get('type', 'N/A')
            business_purpose = service_config.get('business_purpose', 'N/A')
            
            prompt += f"""### {service_name.replace('_', ' ').title()}
- **Tipo:** {service_type}
- **Propósito:** {business_purpose}

"""
        
        prompt += f"""## Prompt para Arquitecto

Basado en esta información, diseña una arquitectura AWS que:

1. **Cumpla con regulaciones DIAN** para el procesamiento de facturas
2. **Soporte 60M productos** con alta disponibilidad
3. **Procese 10,000 facturas/hora** con escalamiento automático
4. **Integre OCR** para procesamiento de imágenes/PDFs
5. **Mantenga compliance** regulatorio y auditabilidad

### Consideraciones Técnicas
- Usar patrones de microservicios
- Implementar cache distribuido
- Configurar monitoreo y alertas
- Diseñar para multi-AZ
- Incluir backup y disaster recovery

### Diagramas Requeridos
Genera los siguientes diagramas en **Mermaid**:

1. **Diagrama de Arquitectura**
```mermaid
graph TB
    subgraph "AWS Cloud"
        subgraph "Application Layer"
            MS1[Invoice Service]
            MS2[Product Service]
            MS3[OCR Service]
        end
        subgraph "Data Layer"
            RDS[PostgreSQL]
            S3[S3 Storage]
        end
    end
```

2. **Diagrama de Flujo de Datos**
```mermaid
sequenceDiagram
    Usuario->>API: Upload Invoice
    API->>OCR: Process Document
    OCR->>Products: Match Items
    Products->>Commission: Calculate
```

3. **Diagrama de Migración**
```mermaid
gantt
    title Migration Plan
    section Phase 1
    Infrastructure Setup: 2w
    section Phase 2
    Data Migration: 3w
```

Los diagramas Mermaid están disponibles en: `outputs/mcp/diagrams/bmc_input/mermaid/`

Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        return prompt
    
    def _generate_migration_prompt(self) -> str:
        """Genera prompt de migración"""
        
        workflow = self.config.get("workflow", {})
        
        prompt = f"""# Prompt de Migración MCP

## Estrategia de Migración

### Patrón Recomendado: Strangler Fig
Migración gradual reemplazando componentes del sistema legacy.

### Fases de Migración

#### Fase 1: Precaracterización
- Análisis del sistema actual
- Identificación de dependencias
- Mapeo de datos (60M productos)

#### Fase 2: Estructuración  
- Diseño de microservicios
- Arquitectura de datos (PostgreSQL + Redshift)
- Definición de APIs

#### Fase 3: Catálogo
- Mapeo de aplicaciones
- Priorización de componentes
- Plan de implementación

#### Fase 4: Lineamientos
- Estándares de implementación
- Compliance regulatorio DIAN
- Métricas de rendimiento

## Prompt para Especialista en Migración

Desarrolla un plan detallado que:

1. **Minimice el downtime** durante la migración
2. **Preserve la integridad** de 60M registros de productos
3. **Mantenga compliance** DIAN durante todo el proceso
4. **Implemente rollback** en caso de problemas
5. **Valide la migración** con pruebas exhaustivas

### Riesgos Identificados
- Pérdida de datos durante migración
- Interrupción del servicio regulatorio
- Incompatibilidad con sistemas SFTP existentes
- Degradación de performance con 60M registros

### Mitigaciones Propuestas
- Migración por lotes con validación
- Ambiente de staging idéntico a producción
- Pruebas de carga con datos reales
- Plan de rollback automatizado

Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        return prompt
    
    def _generate_implementation_prompt(self) -> str:
        """Genera prompt de implementación"""
        
        kpis = self.config.get("performance_kpis", {})
        
        prompt = f"""# Prompt de Implementación MCP

## Especificaciones Técnicas

### Performance KPIs
- **Throughput:** {kpis.get('throughput', {}).get('invoices_per_hour', '10,000')} facturas/hora
- **Base de datos:** {kpis.get('throughput', {}).get('products_database', '60M')} productos
- **Categorías:** {kpis.get('throughput', {}).get('categories', '16,000')} tipos

### Tiempos de Respuesta Objetivo
- **Lookup de productos:** < 300ms
- **Procesamiento de facturas:** < 3000ms  
- **Generación de certificados:** < 2000ms

### Precisión Requerida
- **OCR:** > 95% precisión
- **Matching de productos:** > 99% precisión
- **Compliance regulatorio:** > 99.8% precisión

## Prompt para Desarrollador

Implementa el sistema con estas especificaciones:

### 1. Servicios Core
```
invoice_service:
  - Procesamiento de facturas individuales y por lotes
  - Integración con OCR (Textract)
  - Validación DIAN

product_service:
  - Gestión de 60M productos
  - Cache distribuido (Redis)
  - API de búsqueda optimizada

ocr_service:
  - Análisis de facturas PDF/imagen
  - Matching con base de datos
  - Precisión > 95%

commission_service:
  - Cálculos regulatorios
  - Compliance DIAN
  - Auditabilidad completa

certificate_service:
  - Generación PDF
  - Envío por email
  - Almacenamiento seguro
```

### 2. Infraestructura AWS
- **ECS Fargate** para microservicios
- **RDS PostgreSQL Multi-AZ** para datos transaccionales
- **Redshift** para analytics
- **S3** para documentos
- **ElastiCache Redis** para cache
- **Textract** para OCR

### 3. Monitoreo y Alertas
- CloudWatch métricas custom
- Alertas por SLA breach
- Dashboard de compliance
- Logs centralizados

### 4. Seguridad
- Encriptación AES-256 en reposo
- TLS 1.3 en tránsito
- RBAC con MFA
- Audit trail completo

Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        return prompt
