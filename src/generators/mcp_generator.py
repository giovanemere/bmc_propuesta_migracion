#!/usr/bin/env python3
"""
Unified MCP Generator - Generador unificado desde documentación MCP
Genera PNG, DrawIO y Mermaid desde la misma base de infraestructura
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, Any
import xml.etree.ElementTree as ET

class UnifiedMCPGenerator:
    """Generador unificado desde MCP"""
    
    def __init__(self, config: Dict[str, Any], output_dir: str = "outputs/mcp"):
        self.config = config
        self.output_dir = Path(output_dir)
        
    def generate_all_diagrams(self, project_name: str = "bmc_input") -> Dict[str, str]:
        """Genera todos los diagramas desde la misma base MCP"""
        
        # Usar directorio base directamente (ya viene con la ruta completa)
        base_dir = self.output_dir
        base_dir.mkdir(parents=True, exist_ok=True)
        
        # Crear subdirectorios
        (base_dir / "mermaid").mkdir(exist_ok=True)
        (base_dir / "drawio").mkdir(exist_ok=True)
        (base_dir / "png").mkdir(exist_ok=True)
        
        results = {}
        
        # Generar diagramas Mermaid
        mermaid_results = self._generate_mermaid_diagrams(base_dir, project_name)
        results.update(mermaid_results)
        
        # Generar DrawIO detallado y profesional
        from .enhanced_drawio_generator import EnhancedDrawIOGenerator
        enhanced_generator = EnhancedDrawIOGenerator(self.config, str(base_dir))
        detailed_drawio = enhanced_generator.generate_detailed_drawio(project_name)
        results["drawio_detailed"] = detailed_drawio
        
        print(f"✓ Unified diagrams generated from MCP infrastructure")
        return results
    
    def _generate_mermaid_diagrams(self, base_dir: Path, project_name: str) -> Dict[str, str]:
        """Genera diagramas Mermaid desde configuración MCP"""
        
        results = {}
        
        # Diagrama de arquitectura
        arch_mermaid = self._create_architecture_mermaid()
        arch_file = base_dir / "mermaid" / "architecture.md"
        with open(arch_file, 'w', encoding='utf-8') as f:
            f.write(arch_mermaid)
        results["mermaid_architecture"] = str(arch_file)
        
        # Diagrama de flujo de datos
        flow_mermaid = self._create_dataflow_mermaid()
        flow_file = base_dir / "mermaid" / "dataflow.md"
        with open(flow_file, 'w', encoding='utf-8') as f:
            f.write(flow_mermaid)
        results["mermaid_dataflow"] = str(flow_file)
        
        # Diagrama de migración
        migration_mermaid = self._create_migration_mermaid()
        migration_file = base_dir / "mermaid" / "migration.md"
        with open(migration_file, 'w', encoding='utf-8') as f:
            f.write(migration_mermaid)
        results["mermaid_migration"] = str(migration_file)
        
        return results
    
    def _create_architecture_mermaid(self) -> str:
        """Crea diagrama de arquitectura en Mermaid"""
        
        microservices = self.config.get("microservices", {})
        aws_services = self.config.get("aws_services", {})
        
        mermaid = f"""# Arquitectura BMC - Mermaid

```mermaid
graph TB
    subgraph "AWS Cloud"
        subgraph "Application Layer"
"""
        
        # Agregar microservicios
        for i, (service_name, service_config) in enumerate(microservices.items()):
            service_id = f"MS{i+1}"
            service_title = service_name.replace('_', ' ').title()
            mermaid += f"            {service_id}[{service_title}]\n"
        
        mermaid += "        end\n\n        subgraph \"Data Layer\"\n"
        
        # Agregar servicios AWS
        for i, (service_name, service_config) in enumerate(aws_services.items()):
            service_id = f"AWS{i+1}"
            service_title = service_name.replace('_', ' ').title()
            service_type = service_config.get('type', 'service').upper()
            mermaid += f"            {service_id}[{service_title}<br/>{service_type}]\n"
        
        mermaid += "        end\n    end\n\n"
        
        # Agregar conexiones
        mermaid += "    %% Connections\n"
        ms_count = len(microservices)
        aws_count = len(aws_services)
        
        for i in range(1, ms_count + 1):
            for j in range(1, aws_count + 1):
                mermaid += f"    MS{i} --> AWS{j}\n"
        
        mermaid += "```\n\n"
        
        # Agregar especificaciones
        mermaid += "## Especificaciones Técnicas\n\n"
        for service_name, service_config in microservices.items():
            business_function = service_config.get('business_function', 'N/A')
            compute = service_config.get('compute', {})
            mermaid += f"### {service_name.replace('_', ' ').title()}\n"
            mermaid += f"- **Función:** {business_function}\n"
            mermaid += f"- **CPU:** {compute.get('cpu', 'N/A')} vCPU\n"
            mermaid += f"- **Memoria:** {compute.get('memory', 'N/A')} MB\n\n"
        
        return mermaid
    
    def _create_dataflow_mermaid(self) -> str:
        """Crea diagrama de flujo de datos en Mermaid"""
        
        mermaid = f"""# Flujo de Datos BMC - Mermaid

```mermaid
sequenceDiagram
    participant U as Usuario
    participant API as API Gateway
    participant IS as Invoice Service
    participant OCR as OCR Service
    participant PS as Product Service
    participant CS as Commission Service
    participant CERT as Certificate Service
    participant DB as PostgreSQL
    participant S3 as S3 Storage
    
    U->>API: Upload Invoice (PDF/Image)
    API->>IS: Process Invoice
    IS->>S3: Store Document
    IS->>OCR: Extract Text/Data
    OCR->>PS: Match Products
    PS->>DB: Query 60M Products
    DB-->>PS: Product Data
    PS-->>OCR: Matched Products
    OCR-->>IS: Processed Invoice
    IS->>CS: Calculate Commission
    CS->>DB: Apply DIAN Rules
    DB-->>CS: Commission Data
    CS-->>IS: Commission Result
    IS->>CERT: Generate Certificate
    CERT->>S3: Store Certificate
    CERT-->>IS: Certificate URL
    IS-->>API: Processing Complete
    API-->>U: Certificate Ready
```

## Métricas de Performance

- **Throughput:** 10,000 facturas/hora
- **Latencia OCR:** < 5 segundos
- **Lookup productos:** < 300ms
- **Generación certificado:** < 2 segundos

## Volúmenes de Datos

- **Productos:** 60M registros
- **Categorías:** 16,000 tipos
- **Facturas diarias:** ~240,000
"""
        
        return mermaid
    
    def _create_migration_mermaid(self) -> str:
        """Crea diagrama de migración en Mermaid"""
        
        mermaid = f"""# Plan de Migración BMC - Mermaid

```mermaid
gantt
    title Migración BMC - Strangler Fig Pattern
    dateFormat  YYYY-MM-DD
    section Preparación
    Análisis Sistema Legacy    :prep1, 2024-01-01, 2w
    Setup AWS Staging         :prep2, after prep1, 2w
    
    section Migración Datos
    Migración Productos 60M   :data1, after prep2, 2w
    Validación Integridad     :data2, after data1, 1w
    
    section Microservicios
    Product Service           :ms1, after data2, 2w
    Invoice Service           :ms2, after ms1, 2w
    OCR Service              :ms3, after ms2, 1w
    Commission Service        :ms4, after ms3, 1w
    
    section Cutover
    Pruebas Integración      :cut1, after ms4, 1w
    Cutover Producción       :cut2, after cut1, 1w
```

## Estrategia de Migración

```mermaid
graph LR
    subgraph "Sistema Legacy"
        L1[Facturas Legacy]
        L2[Productos Legacy]
        L3[Comisiones Legacy]
    end
    
    subgraph "Período Transición"
        T1[Proxy/Router]
        T2[Sincronización]
    end
    
    subgraph "Sistema AWS"
        A1[Invoice Service]
        A2[Product Service]
        A3[Commission Service]
    end
    
    L1 --> T1
    L2 --> T2
    L3 --> T1
    
    T1 --> A1
    T2 --> A2
    T1 --> A3
    
    style T1 fill:#f9f,stroke:#333,stroke-width:2px
    style T2 fill:#f9f,stroke:#333,stroke-width:2px
```

## Criterios de Rollback

- Error rate > 5%
- Latencia > 5000ms
- Disponibilidad < 99%
"""
        
        return mermaid
    
    def _generate_unified_drawio(self, base_dir: Path, project_name: str) -> str:
        """Genera DrawIO unificado desde infraestructura MCP"""
        
        microservices = self.config.get("microservices", {})
        aws_services = self.config.get("aws_services", {})
        
        # Crear XML DrawIO
        mxfile = ET.Element("mxfile", host="app.diagrams.net")
        diagram = ET.SubElement(mxfile, "diagram", name=f"{project_name} MCP Architecture", id="mcp")
        model = ET.SubElement(diagram, "mxGraphModel", dx="1600", dy="900", grid="1", gridSize="10")
        root = ET.SubElement(model, "root")
        
        # Celdas base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")
        
        # Título
        title_cell = ET.SubElement(root, "mxCell",
            id="title",
            value=f"{project_name.upper()} - MCP Architecture",
            style="rounded=0;whiteSpace=wrap;html=1;fillColor=#232F3E;fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
            vertex="1", parent="1"
        )
        ET.SubElement(title_cell, "mxGeometry", x="50", y="20", width="1200", height="50", **{"as": "geometry"})
        
        # AWS Cloud
        aws_cell = ET.SubElement(root, "mxCell",
            id="aws_cloud",
            value="AWS Cloud - BMC Infrastructure",
            style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;fontSize=14;fontStyle=1;verticalAlign=top;",
            vertex="1", parent="1"
        )
        ET.SubElement(aws_cell, "mxGeometry", x="100", y="100", width="1100", height="600", **{"as": "geometry"})
        
        # Microservicios
        y_pos = 200
        for i, (service_name, service_config) in enumerate(microservices.items()):
            service_cell = ET.SubElement(root, "mxCell",
                id=f"ms_{i}",
                value=f"{service_name.replace('_', ' ').title()}\\n{service_config.get('business_function', '')[:30]}...",
                style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D05C17;fontColor=#FFFFFF;fontSize=10;",
                vertex="1", parent="1"
            )
            ET.SubElement(service_cell, "mxGeometry", x="200", y=str(y_pos), width="150", height="80", **{"as": "geometry"})
            y_pos += 100
        
        # Servicios AWS
        x_pos = 500
        for i, (service_name, service_config) in enumerate(aws_services.items()):
            aws_service_cell = ET.SubElement(root, "mxCell",
                id=f"aws_{i}",
                value=f"{service_name.replace('_', ' ').title()}\\n{service_config.get('type', '').upper()}",
                style="rounded=1;whiteSpace=wrap;html=1;fillColor=#116D5B;fontColor=#FFFFFF;fontSize=10;",
                vertex="1", parent="1"
            )
            ET.SubElement(aws_service_cell, "mxGeometry", x=str(x_pos), y="300", width="120", height="60", **{"as": "geometry"})
            x_pos += 150
        
        # Generar XML
        ET.indent(mxfile, space="  ")
        xml_str = ET.tostring(mxfile, encoding='unicode', xml_declaration=True)
        
        # Guardar archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{project_name}_mcp_unified_{timestamp}.drawio"
        output_path = base_dir / "drawio" / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        return str(output_path)
