#!/usr/bin/env python3
"""
BMC Input Parser - Parser específico para especificación BMC
Convierte la especificación BMC en configuración MCP
"""

import re
from typing import Dict, Any

class BMCInputParser:
    """Parser para especificación de entrada BMC"""
    
    def __init__(self, bmc_input_file: str):
        self.bmc_input_file = bmc_input_file
        self.content = ""
        
    def load(self) -> bool:
        """Carga el archivo de especificación BMC"""
        try:
            with open(self.bmc_input_file, 'r', encoding='utf-8') as f:
                self.content = f.read()
            return True
        except Exception as e:
            print(f"❌ Error loading BMC input: {e}")
            return False
    
    def parse_to_mcp_config(self) -> Dict[str, Any]:
        """Convierte especificación BMC a configuración MCP"""
        
        if not self.load():
            return {}
        
        # Extraer información clave
        volume_data = self._extract_volume_data()
        backend_functions = self._extract_backend_functions()
        frontend_functions = self._extract_frontend_functions()
        database_arch = self._extract_database_architecture()
        business_flow = self._extract_business_flow()
        integrations = self._extract_integrations()
        
        # Generar configuración MCP
        mcp_config = {
            "project": {
                "name": "BMC Bolsa Comisionista",
                "description": "Sistema Regulatorio - Procesamiento de facturas y cálculo de comisiones",
                "version": "2.0.0",
                "environment": "production",
                "region": "us-east-1"
            },
            
            "microservices": self._generate_microservices(backend_functions, volume_data),
            "aws_services": self._generate_aws_services(database_arch, volume_data),
            "business_logic": self._generate_business_logic(business_flow),
            "integrations": self._generate_integrations_config(integrations),
            "performance_kpis": self._generate_performance_kpis(volume_data)
        }
        
        return mcp_config
    
    def _extract_volume_data(self) -> Dict[str, Any]:
        """Extrae información de volumen de datos"""
        volume = {}
        
        # Buscar productos
        products_match = re.search(r'Productos:\*\*\s*(\d+)M?\s*registros', self.content)
        if products_match:
            volume["products_count"] = f"{products_match.group(1)}M"
        
        # Buscar categorías
        categories_match = re.search(r'Tipos de Productos:\*\*\s*([0-9,]+)\s*categorías', self.content)
        if categories_match:
            volume["categories_count"] = categories_match.group(1).replace(',', '')
        
        return volume
    
    def _extract_backend_functions(self) -> list:
        """Extrae funcionalidades backend"""
        functions = []
        
        # Buscar sección de backend
        backend_section = re.search(r'### Funcionalidades Backend(.*?)###', self.content, re.DOTALL)
        if backend_section:
            content = backend_section.group(1)
            
            if "APIs para procesamiento" in content:
                functions.append("invoice_processing")
            if "Base de datos de productos" in content:
                functions.append("product_management")
            if "Desagregación por producto" in content:
                functions.append("product_analysis")
            if "Cálculos de comisión" in content:
                functions.append("commission_calculation")
        
        return functions
    
    def _extract_frontend_functions(self) -> list:
        """Extrae funcionalidades frontend"""
        functions = []
        
        frontend_section = re.search(r'### Funcionalidades Frontend(.*?)###', self.content, re.DOTALL)
        if frontend_section:
            content = frontend_section.group(1)
            
            if "Formularios web" in content:
                functions.append("web_forms")
            if "caga de factiuras" in content or "carga de facturas" in content:
                functions.append("invoice_upload")
            if "exportación" in content:
                functions.append("export_services")
            if "Procesamiento en background" in content:
                functions.append("background_processing")
        
        return functions
    
    def _extract_database_architecture(self) -> Dict[str, str]:
        """Extrae arquitectura de base de datos"""
        db_arch = {}
        
        if "PostgreSQL principal" in self.content:
            db_arch["transactional"] = "postgresql"
        if "Redshift para reportería" in self.content:
            db_arch["analytical"] = "redshift"
        if "Text processing" in self.content:
            db_arch["processing"] = "text_processing"
        
        return db_arch
    
    def _extract_business_flow(self) -> list:
        """Extrae flujo de negocio"""
        flow_steps = []
        
        flow_section = re.search(r'### Flujo de Negocio(.*?)###', self.content, re.DOTALL)
        if flow_section:
            content = flow_section.group(1)
            
            if "Carga de facturas" in content:
                flow_steps.append("invoice_upload")
            if "Botón calcular" in content:
                flow_steps.append("calculation_trigger")
            if "Generación de certificado" in content:
                flow_steps.append("certificate_generation")
        
        return flow_steps
    
    def _extract_integrations(self) -> Dict[str, Any]:
        """Extrae integraciones externas"""
        integrations = {}
        
        if "SFTP Integration" in self.content:
            integrations["sftp"] = {
                "type": "sftp",
                "purpose": "regulatory_data_exchange"
            }
        
        return integrations
    
    def _generate_microservices(self, backend_functions: list, volume_data: Dict) -> Dict[str, Any]:
        """Genera configuración de microservicios"""
        
        microservices = {}
        
        if "invoice_processing" in backend_functions:
            microservices["invoice_service"] = {
                "compute": {"cpu": 2048, "memory": 4096},
                "scaling": {"min_capacity": 2, "max_capacity": 10},
                "business_function": "Procesamiento de facturas individuales y por lotes"
            }
        
        if "product_management" in backend_functions:
            products_count = volume_data.get("products_count", "60M")
            microservices["product_service"] = {
                "compute": {"cpu": 4096, "memory": 8192},
                "scaling": {"min_capacity": 3, "max_capacity": 15},
                "business_function": f"Gestión de {products_count} productos migrados desde Google Cloud"
            }
        
        if "product_analysis" in backend_functions:
            microservices["ocr_service"] = {
                "compute": {"cpu": 2048, "memory": 4096},
                "ai_ml": {"ocr_engine": "textract", "accuracy_target": ">95%"},
                "business_function": "Análisis de facturas y matching con base de datos"
            }
        
        if "commission_calculation" in backend_functions:
            microservices["commission_service"] = {
                "compute": {"cpu": 1024, "memory": 2048},
                "business_function": "Cálculos de comisión regulatoria (lote e individual)"
            }
        
        # Servicio de certificados (inferido del flujo)
        microservices["certificate_service"] = {
            "compute": {"cpu": 1024, "memory": 2048},
            "business_function": "Generación de certificados PDF DIAN compliance"
        }
        
        return microservices
    
    def _generate_aws_services(self, db_arch: Dict, volume_data: Dict) -> Dict[str, Any]:
        """Genera configuración de servicios AWS"""
        
        aws_services = {}
        
        if db_arch.get("transactional") == "postgresql":
            products_count = volume_data.get("products_count", "60M")
            aws_services["rds_primary"] = {
                "type": "rds",
                "engine": "postgresql",
                "instance_class": "db.r6g.2xlarge",
                "business_purpose": f"Base de datos transaccional - {products_count} productos"
            }
        
        if db_arch.get("analytical") == "redshift":
            aws_services["redshift_analytics"] = {
                "type": "redshift",
                "node_type": "dc2.large",
                "business_purpose": "Data warehouse para reportería regulatoria"
            }
        
        # Cache para productos (inferido)
        aws_services["redis_cache"] = {
            "type": "elasticache",
            "engine": "redis",
            "business_purpose": "Cache de productos frecuentes y sesiones"
        }
        
        # Storage para documentos
        aws_services["s3_documents"] = {
            "type": "s3",
            "storage_class": "intelligent_tiering",
            "business_purpose": "Almacenamiento de facturas PDF/imágenes"
        }
        
        return aws_services
    
    def _generate_business_logic(self, flow_steps: list) -> Dict[str, Any]:
        """Genera lógica de negocio"""
        
        business_logic = {
            "regulatory_compliance": "DIAN Colombia",
            "validation_levels": 2,
            "processing_modes": ["individual", "batch"],
            "output_formats": ["PDF", "Excel"]
        }
        
        if "certificate_generation" in flow_steps:
            business_logic["certificate_types"] = ["PDF_download", "email_delivery"]
        
        return business_logic
    
    def _generate_integrations_config(self, integrations: Dict) -> Dict[str, Any]:
        """Genera configuración de integraciones"""
        
        config = {}
        
        if "sftp" in integrations:
            config["sftp_regulatory"] = {
                "type": "sftp",
                "purpose": "Intercambio de datos regulatorios",
                "frequency": "daily",
                "compliance": "regulatory_reporting"
            }
        
        return config
    
    def _generate_performance_kpis(self, volume_data: Dict) -> Dict[str, Any]:
        """Genera KPIs de rendimiento"""
        
        return {
            "throughput": {
                "invoices_per_hour": 10000,
                "products_database": volume_data.get("products_count", "60M"),
                "categories": volume_data.get("categories_count", "16000")
            },
            "response_times": {
                "product_lookup": "300ms",
                "invoice_processing": "3000ms",
                "certificate_generation": "2000ms"
            },
            "accuracy": {
                "ocr_processing": ">95%",
                "product_matching": ">99%",
                "regulatory_compliance": ">99.8%"
            }
        }
