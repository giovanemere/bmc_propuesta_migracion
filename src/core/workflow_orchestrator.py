#!/usr/bin/env python3
"""
Workflow Orchestrator - Orquestador completo del flujo de generación
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
import json

from .app_config import get_config, save_config, get_output_path, get_paths

class WorkflowOrchestrator:
    """Orquestador del flujo completo de generación"""
    
    def __init__(self, project_name: str = "bmc_input"):
        self.project_name = project_name
        self.paths = get_paths()
        self.results = {}
        self.start_time = datetime.now()
    
    def execute_complete_workflow(self) -> Dict[str, Any]:
        """Ejecuta el flujo completo de generación"""
        
        print(f"🚀 Iniciando flujo completo para {self.project_name}")
        print("=" * 60)
        
        try:
            # 1. Cargar y validar configuración
            config = self._load_and_validate_config()
            
            # 2. Generar prompts MCP
            prompts = self._generate_mcp_prompts(config)
            
            # 3. Generar documentación
            documentation = self._generate_documentation(config)
            
            # 4. Generar diagramas
            diagrams = self._generate_diagrams(config)
            
            # 5. Consolidar resultados
            results = self._consolidate_results(config, prompts, documentation, diagrams)
            
            # 6. Generar reporte final
            report = self._generate_final_report(results)
            
            print(f"\n🎉 Flujo completado exitosamente")
            return results
            
        except Exception as e:
            print(f"\n❌ Error en flujo: {e}")
            raise
    
    def _load_and_validate_config(self) -> Dict[str, Any]:
        """Carga y valida configuración"""
        
        print("\n1️⃣ CARGANDO CONFIGURACIÓN")
        
        # Cargar configuración MCP
        mcp_config = get_config("bmc")
        print(f"✅ Configuración MCP cargada")
        
        # Cargar modelo estándar
        standard_model = get_config("standard_model")
        print(f"✅ Modelo estándar cargado")
        
        # Validar configuración
        microservices = mcp_config.get("microservices")
        if not microservices:
            # Buscar en estructura anidada
            workflow = mcp_config.get("workflow", {})
            arch_design = workflow.get("architecture_design", {})
            microservices = arch_design.get("microservices")
            
            if not microservices:
                print("⚠️ No se encontraron microservicios en configuración MCP, usando defaults")
                # Usar configuración por defecto con microservicios
                default_mcp = get_config("bmc")
                mcp_config.update(default_mcp)
        
        # Consolidar configuración
        consolidated_config = {
            "project_name": self.project_name,
            "mcp": mcp_config,
            "standard_model": standard_model,
            "timestamp": self.start_time.isoformat(),
            "version": "4.1.0"
        }
        
        # Guardar configuración consolidada
        config_path = save_config(f"{self.project_name}_consolidated", consolidated_config)
        print(f"✅ Configuración consolidada guardada: {Path(config_path).name}")
        
        return consolidated_config
    
    def _generate_mcp_prompts(self, config: Dict[str, Any]) -> Dict[str, str]:
        """Genera prompts MCP"""
        
        print("\n2️⃣ GENERANDO PROMPTS MCP")
        
        from generators.prompt_generator import MCPPromptGenerator
        
        prompt_generator = MCPPromptGenerator(config["mcp"], str(self.paths.outputs_prompts_dir))
        
        prompts = {}
        
        # Generar prompts usando método existente
        try:
            prompt_results = prompt_generator.generate_prompts(self.project_name)
            prompts.update(prompt_results)
            print(f"✅ Prompts generados: {len(prompt_results)}")
        except Exception as e:
            print(f"⚠️ Error generando prompts: {e}")
        
        return prompts
    
    def _generate_documentation(self, config: Dict[str, Any]) -> Dict[str, str]:
        """Genera documentación"""
        
        print("\n3️⃣ GENERANDO DOCUMENTACIÓN")
        
        from generators.doc_generator import ImplementationDocGenerator
        
        doc_generator = ImplementationDocGenerator(config["mcp"], str(self.paths.outputs_docs_dir))
        
        documentation = {}
        
        # Generar documentos usando método existente
        try:
            doc_results = doc_generator.generate_implementation_docs(self.project_name)
            documentation.update(doc_results)
            print(f"✅ Documentos generados: {len(doc_results)}")
        except Exception as e:
            print(f"⚠️ Error generando documentos: {e}")
        
        return documentation
    
    def _generate_diagrams(self, config: Dict[str, Any]) -> Dict[str, str]:
        """Genera diagramas"""
        
        print("\n4️⃣ GENERANDO DIAGRAMAS")
        
        from generators.universal_generator import UniversalGenerator
        from validators.xml_validator import MCPIntegrator
        from templates.drawio_templates import DrawIOTemplates
        
        diagrams = {}
        
        try:
            # Generar PNG usando diagram_generator
            from generators.diagram_generator import DiagramGenerator
            
            diagram_generator = DiagramGenerator(config["mcp"])
            
            # Generar diagramas PNG
            png_types = ["network", "microservices", "security", "data_flow"]
            
            for diagram_type in png_types:
                try:
                    png_path = diagram_generator.generate_diagram(
                        diagram_type, 
                        str(self.paths.outputs_png_dir / self.project_name)
                    )
                    diagrams[f"png_{diagram_type}"] = png_path
                    print(f"✅ PNG {diagram_type}: {Path(png_path).name}")
                except Exception as e:
                    print(f"⚠️ Error PNG {diagram_type}: {e}")
            
            # Generar DrawIO usando MCP integration
            integrator = MCPIntegrator()
            standard_model = integrator.convert_mcp_to_standard_model(config["mcp"])
            
            # Generar DrawIO
            drawio_xml = DrawIOTemplates.generate_drawio_xml(standard_model)
            
            drawio_path = get_output_path("drawio", f"{self.project_name}_complete.drawio", self.project_name)
            with open(drawio_path, 'w', encoding='utf-8') as f:
                f.write(drawio_xml)
            
            diagrams["drawio_complete"] = str(drawio_path)
            print(f"✅ DrawIO completo: {drawio_path.name}")
            
            # Validar DrawIO generado
            validation = integrator.validate_mcp_generated_xml(drawio_xml, config["mcp"])
            if validation["overall_valid"]:
                print(f"✅ DrawIO validado correctamente")
            else:
                print(f"⚠️ DrawIO con advertencias de validación")
            
        except Exception as e:
            print(f"❌ Error generando diagramas: {e}")
        
        return diagrams
    
    def _consolidate_results(self, config: Dict[str, Any], prompts: Dict[str, str], 
                           documentation: Dict[str, str], diagrams: Dict[str, str]) -> Dict[str, Any]:
        """Consolida todos los resultados"""
        
        print("\n5️⃣ CONSOLIDANDO RESULTADOS")
        
        results = {
            "project_name": self.project_name,
            "timestamp": self.start_time.isoformat(),
            "duration_seconds": (datetime.now() - self.start_time).total_seconds(),
            "config": config,
            "generated_files": {
                "prompts": prompts,
                "documentation": documentation,
                "diagrams": diagrams
            },
            "summary": {
                "total_files": len(prompts) + len(documentation) + len(diagrams),
                "prompts_count": len(prompts),
                "docs_count": len(documentation),
                "diagrams_count": len(diagrams)
            }
        }
        
        # Guardar resultados consolidados
        results_path = save_config(f"{self.project_name}_results", results)
        print(f"✅ Resultados consolidados: {Path(results_path).name}")
        
        return results
    
    def _generate_final_report(self, results: Dict[str, Any]) -> str:
        """Genera reporte final"""
        
        print("\n6️⃣ GENERANDO REPORTE FINAL")
        
        report_content = f"""# Reporte de Generación - {results['project_name'].upper()}

## 📊 Resumen Ejecutivo

- **Proyecto:** {results['project_name']}
- **Fecha:** {results['timestamp'][:19]}
- **Duración:** {results['duration_seconds']:.1f} segundos
- **Archivos generados:** {results['summary']['total_files']}

## 📋 Archivos Generados

### 🎯 Prompts MCP ({results['summary']['prompts_count']})
"""
        
        for prompt_type, prompt_path in results['generated_files']['prompts'].items():
            report_content += f"- **{prompt_type}:** `{Path(prompt_path).name}`\n"
        
        report_content += f"""
### 📚 Documentación ({results['summary']['docs_count']})
"""
        
        for doc_type, doc_path in results['generated_files']['documentation'].items():
            report_content += f"- **{doc_type}:** `{Path(doc_path).name}`\n"
        
        report_content += f"""
### 📐 Diagramas ({results['summary']['diagrams_count']})
"""
        
        for diagram_type, diagram_path in results['generated_files']['diagrams'].items():
            report_content += f"- **{diagram_type}:** `{Path(diagram_path).name}`\n"
        
        report_content += f"""
## 🎯 Configuración Utilizada

- **Microservicios:** {len(results['config']['mcp'].get('microservices', {}))}
- **Servicios AWS:** {len(results['config']['mcp'].get('aws_services', {}))}
- **Versión:** {results['config']['version']}

## ✅ Estado Final

Generación completada exitosamente. Todos los archivos están disponibles en la carpeta `outputs/`.

---
*Generado automáticamente por MCP Diagram Generator v{results['config']['version']}*
"""
        
        # Guardar reporte
        report_path = get_output_path("documentation", f"{self.project_name}_report.md", self.project_name)
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"✅ Reporte final: {report_path.name}")
        
        return str(report_path)

def run_complete_workflow(project_name: str = "bmc_input") -> Dict[str, Any]:
    """Ejecuta el flujo completo de generación"""
    
    orchestrator = WorkflowOrchestrator(project_name)
    return orchestrator.execute_complete_workflow()
