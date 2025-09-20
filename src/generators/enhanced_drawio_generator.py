#!/usr/bin/env python3
"""
Enhanced DrawIO Generator - Con todas las mejoras implementadas
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
import sys
sys.path.append('/home/giovanemere/Migracion/src')

from models.diagram_model import DiagramModel, DiagramModelBuilder
from layouts.diagram_layouts import LayoutEngine, LayoutType
from validators.drawio_validator import DrawIOValidator, DrawIOPreview, DrawIOTester
from styles.diagram_styles import StyleManager, LegendGenerator, AnnotationManager
from reports.html_report_generator import HTMLReportGenerator

class EnhancedDrawIOGenerator:
    """Generador DrawIO mejorado con todas las características"""
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.html_generator = HTMLReportGenerator(output_dir)
    
    def generate_enhanced_diagrams(self, config: Dict[str, Any], project_name: str = "bmc_input") -> Dict[str, Any]:
        """Genera diagramas mejorados con todas las características"""
        
        results = {
            "diagrams": [],
            "previews": [],
            "validations": [],
            "report_path": None,
            "summary": {}
        }
        
        print("🎨 Generando diagramas mejorados...")
        
        # 1. Crear múltiples diagramas con diferentes layouts
        diagram_configs = [
            {"name": "Network Architecture", "layout": LayoutType.HIERARCHICAL},
            {"name": "Microservices Grid", "layout": LayoutType.GRID},
            {"name": "Security Circle", "layout": LayoutType.CIRCULAR},
            {"name": "Data Flow Force", "layout": LayoutType.FORCE_DIRECTED}
        ]
        
        for diagram_config in diagram_configs:
            diagram_result = self._generate_single_diagram(
                config, 
                project_name, 
                diagram_config["name"],
                diagram_config["layout"]
            )
            
            if diagram_result:
                results["diagrams"].append(diagram_result)
        
        # 2. Generar previews
        print("🖼️ Generando previews...")
        for diagram in results["diagrams"]:
            preview_path = self._generate_preview(diagram["path"])
            if preview_path:
                results["previews"].append(preview_path)
        
        # 3. Ejecutar validaciones
        print("🔍 Ejecutando validaciones...")
        for diagram in results["diagrams"]:
            validation_result = self._validate_diagram(diagram["path"])
            results["validations"].append(validation_result)
        
        # 4. Generar reporte HTML
        print("📄 Generando reporte HTML...")
        report_path = self._generate_html_report(results["diagrams"], project_name)
        results["report_path"] = report_path
        
        # 5. Resumen
        results["summary"] = {
            "total_diagrams": len(results["diagrams"]),
            "valid_diagrams": sum(1 for v in results["validations"] if v["all_passed"]),
            "previews_generated": len(results["previews"]),
            "report_generated": report_path is not None
        }
        
        print(f"✅ Generación completa: {results['summary']}")
        return results
    
    def _generate_single_diagram(self, config: Dict, project_name: str, diagram_name: str, layout: LayoutType) -> Dict:
        """Genera un diagrama individual"""
        
        try:
            # 1. Crear modelo desde configuración
            model = DiagramModelBuilder.from_config(config)
            model.name = diagram_name
            model.layout = layout
            
            # 2. Aplicar estilos consistentes
            self._apply_consistent_styles(model)
            
            # 3. Aplicar layout
            LayoutEngine.apply_layout(model)
            
            # 4. Agregar leyenda y anotaciones
            self._add_legend_and_annotations(model)
            
            # 5. Generar XML
            xml_content = self._render_enhanced_xml(model)
            
            # 6. Guardar archivo
            file_path = self._save_diagram_file(xml_content, project_name, diagram_name)
            
            return {
                "name": diagram_name,
                "path": file_path,
                "type": "drawio",
                "layout": layout.value,
                "valid": True,
                "components": len(model.components),
                "connections": len(model.connections)
            }
        
        except Exception as e:
            print(f"❌ Error generando {diagram_name}: {e}")
            return None
    
    def _apply_consistent_styles(self, model: DiagramModel) -> None:
        """Aplica estilos consistentes por categoría"""
        
        for component in model.components:
            # Obtener estilo basado en el servicio
            style = StyleManager.get_style_for_service(component.name)
            
            # Aplicar estilo al componente
            component.style.fill_color = style.fill_color
            component.style.stroke_color = style.stroke_color
            component.style.font_color = style.font_color
        
        for connection in model.connections:
            # Determinar tipo de conexión
            connection_type = self._determine_connection_type(connection.label)
            style = StyleManager.get_connection_style(connection_type)
            
            # Aplicar estilo a la conexión
            connection.style.stroke_color = style.stroke_color
            connection.style.font_color = style.font_color
            connection.style.stroke_width = style.stroke_width
    
    def _determine_connection_type(self, label: str) -> str:
        """Determina tipo de conexión basado en label"""
        
        label_lower = label.lower()
        
        if any(word in label_lower for word in ["database", "write", "read"]):
            return "data"
        elif any(word in label_lower for word in ["auth", "security", "encrypt"]):
            return "security"
        elif any(word in label_lower for word in ["api", "route", "request"]):
            return "api"
        elif any(word in label_lower for word in ["cache", "redis"]):
            return "cache"
        elif any(word in label_lower for word in ["monitor", "log", "metric"]):
            return "monitoring"
        else:
            return "default"
    
    def _add_legend_and_annotations(self, model: DiagramModel) -> None:
        """Agrega leyenda y anotaciones al modelo"""
        
        from models.diagram_model import Component, ComponentType, Position, Style
        
        # Agregar leyenda
        legend_components = LegendGenerator.create_legend_components()
        
        for legend_item in legend_components:
            component = Component(
                id=legend_item["id"],
                name=legend_item["label"],
                component_type=ComponentType.TITLE,
                position=Position(
                    legend_item["position"]["x"],
                    legend_item["position"]["y"],
                    legend_item["position"].get("width", 200),
                    legend_item["position"].get("height", 30)
                ),
                style=Style(
                    fill_color=legend_item["style"].get("fillColor", "#FFFFFF"),
                    stroke_color=legend_item["style"].get("strokeColor", "#000000"),
                    font_color=legend_item["style"].get("fontColor", "#000000")
                ),
                label=legend_item["label"]
            )
            model.add_component(component)
        
        # Agregar notas explicativas
        notes = AnnotationManager.create_architecture_notes()
        
        for note in notes:
            note_text = f"{note['title']}\\n" + "\\n".join(note['content'])
            
            component = Component(
                id=note["id"],
                name=note["title"],
                component_type=ComponentType.CONTAINER,
                position=Position(
                    note["position"]["x"],
                    note["position"]["y"],
                    300,
                    150
                ),
                style=Style(
                    fill_color=note["style"]["fillColor"],
                    stroke_color=note["style"]["strokeColor"],
                    font_color=note["style"]["fontColor"]
                ),
                label=note_text
            )
            model.add_component(component)
    
    def _render_enhanced_xml(self, model: DiagramModel) -> str:
        """Renderiza XML mejorado con todas las características"""
        
        from generators.refactored_drawio_generator import XMLRenderer
        
        renderer = XMLRenderer()
        return renderer.render_model(model)
    
    def _save_diagram_file(self, xml_content: str, project_name: str, diagram_name: str) -> str:
        """Guarda archivo de diagrama"""
        
        output_dir = self.output_dir / "drawio" / project_name
        output_dir.mkdir(parents=True, exist_ok=True)
        
        safe_name = diagram_name.lower().replace(" ", "_")
        filename = f"enhanced_{safe_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.drawio"
        file_path = output_dir / filename
        
        file_path.write_text(xml_content, encoding='utf-8')
        
        print(f"✅ {diagram_name} generado: {file_path.name}")
        return str(file_path)
    
    def _generate_preview(self, diagram_path: str) -> str:
        """Genera preview PNG del diagrama"""
        
        preview_dir = self.output_dir / "previews"
        preview_dir.mkdir(parents=True, exist_ok=True)
        
        return DrawIOPreview.generate_png_preview(diagram_path, str(preview_dir))
    
    def _validate_diagram(self, diagram_path: str) -> Dict:
        """Valida diagrama completo"""
        
        # Validación con API
        xml_content = Path(diagram_path).read_text(encoding='utf-8')
        api_valid, api_msg = DrawIOValidator.validate_with_api(xml_content)
        
        # Validación con drawio-export
        export_valid, export_msg = DrawIOValidator.validate_with_drawio_export(diagram_path)
        
        # Tests de renderizado
        all_passed, test_results = DrawIOTester.run_full_test_suite(diagram_path)
        
        return {
            "path": diagram_path,
            "api_validation": {"valid": api_valid, "message": api_msg},
            "export_validation": {"valid": export_valid, "message": export_msg},
            "render_tests": test_results,
            "all_passed": all_passed
        }
    
    def _generate_html_report(self, diagrams: List[Dict], project_name: str) -> str:
        """Genera reporte HTML con previews"""
        
        return self.html_generator.generate_diagram_report(diagrams, project_name)
