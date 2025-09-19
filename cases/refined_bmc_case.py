#!/usr/bin/env python3
"""
Refined BMC Case - Caso BMC con diagramas refinados y profesionales
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.mcp_parser import MCPParser
from core.refined_diagram_generator import RefinedDiagramGenerator

def run_refined_bmc_case():
    """Ejecuta el caso BMC refinado"""
    
    print("🏢 BMC Refined Case - Professional Diagrams")
    print("=" * 55)
    
    # Cargar MCP refinado
    mcp_file = "docs/mcp-refined-architecture.md"
    
    if not os.path.exists(mcp_file):
        print(f"❌ MCP file not found: {mcp_file}")
        print("💡 Using fallback configuration...")
        
        # Configuración de fallback
        config = create_fallback_config()
    else:
        # Parsear MCP refinado
        parser = MCPParser(mcp_file)
        config = parser.parse()
        
        if not config:
            print("⚠️ Failed to parse MCP, using fallback...")
            config = create_fallback_config()
    
    # Crear generador refinado
    generator = RefinedDiagramGenerator(config, output_dir="output")
    
    # Generar diagramas refinados
    results = generator.generate_all_refined("BMC")
    
    if results:
        print(f"\n🎉 BMC refined diagrams generated successfully!")
        print("\n📁 Generated files:")
        for diagram_type, file_path in results.items():
            print(f"  - {diagram_type}: {file_path}")
        
        print(f"\n📊 Diagram features:")
        print("  - Professional AWS icons and styling")
        print("  - Detailed configuration labels")
        print("  - Performance metrics and KPIs")
        print("  - Security layers and compliance")
        print("  - Network topology with VPC details")
        print("  - Data flow with processing pipeline")
        
        return True
    else:
        print(f"\n❌ Failed to generate BMC refined diagrams")
        return False

def create_fallback_config():
    """Crea configuración de fallback para BMC"""
    
    return {
        "project": {
            "name": "BMC AWS Platform",
            "description": "Bolsa Mercantil de Colombia - 60M Products Platform",
            "version": "2.0.0",
            "environment": "production",
            "region": "us-east-1"
        },
        
        "diagram_config": {
            "colors": {
                "primary": "#232F3E",
                "secondary": "#FF9900", 
                "success": "#4CAF50",
                "warning": "#FF9800",
                "danger": "#F44336",
                "info": "#2196F3"
            },
            "fonts": {
                "title": 16,
                "cluster": 12,
                "service": 10,
                "label": 8
            }
        },
        
        "microservices": {
            "invoice_service": {
                "compute": {
                    "platform": "ecs_fargate",
                    "cpu": 2048,
                    "memory": 4096
                },
                "scaling": {
                    "min_capacity": 2,
                    "max_capacity": 10,
                    "target_cpu": 70
                },
                "business_metrics": {
                    "throughput": "1000 invoices/hour",
                    "response_time": "<3 seconds",
                    "accuracy": ">99.5%"
                }
            },
            
            "product_service": {
                "compute": {
                    "platform": "ecs_fargate",
                    "cpu": 4096,
                    "memory": 8192
                },
                "scaling": {
                    "min_capacity": 3,
                    "max_capacity": 15,
                    "target_cpu": 70
                },
                "data": {
                    "primary_dataset": "60M products",
                    "cache_strategy": "write_through",
                    "cache_ttl": "24h"
                },
                "performance": {
                    "lookup_time": "<500ms",
                    "cache_hit_ratio": ">95%",
                    "concurrent_users": "10000"
                }
            },
            
            "ocr_service": {
                "compute": {
                    "platform": "ecs_fargate",
                    "cpu": 2048,
                    "memory": 4096
                },
                "ai_ml": {
                    "ocr_engine": "textract",
                    "accuracy_target": ">95%",
                    "processing_time": "<5s",
                    "supported_formats": ["PDF", "JPEG", "PNG", "TIFF"]
                }
            }
        },
        
        "aws_services": {
            "rds_primary": {
                "type": "rds",
                "engine": "postgresql",
                "version": "14.9",
                "instance_class": "db.r6g.2xlarge",
                "storage": {
                    "allocated": 1000,
                    "max_allocated": 5000,
                    "storage_type": "gp3"
                },
                "high_availability": {
                    "multi_az": True,
                    "backup_retention": 35
                }
            },
            
            "redis_cluster": {
                "type": "elasticache",
                "engine": "redis",
                "version": "7.0",
                "node_type": "cache.r6g.xlarge",
                "cluster": {
                    "num_nodes": 3,
                    "cluster_mode": True
                }
            },
            
            "s3_documents": {
                "type": "s3",
                "storage": {
                    "storage_class": "intelligent_tiering",
                    "versioning": True
                }
            }
        },
        
        "performance_kpis": {
            "response_times": {
                "api_gateway": {
                    "target": "200ms",
                    "p95_target": "500ms"
                },
                "product_lookup": {
                    "target": "300ms",
                    "cache_hit_target": "50ms"
                },
                "ocr_processing": {
                    "target": "4000ms",
                    "p95_target": "6000ms"
                }
            },
            "throughput": {
                "invoices_per_hour": 10000,
                "concurrent_users": 10000,
                "api_requests_per_second": 1000
            },
            "availability": {
                "system_sla": 99.9,
                "database_sla": 99.95
            }
        }
    }

if __name__ == "__main__":
    success = run_refined_bmc_case()
    sys.exit(0 if success else 1)
