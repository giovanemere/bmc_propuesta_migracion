#!/usr/bin/env python3
"""
Diagram API - API REST para generación de diagramas PNG y DrawIO
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import tempfile
from pathlib import Path
from typing import Dict, Any
import traceback

from ..core.universal_schema import UniversalDiagramSchema, DiagramType, OutputFormat, SchemaBuilder
from ..generators.universal_generator import UniversalGenerator

app = Flask(__name__)
CORS(app)

# Configuración
OUTPUT_DIR = Path("outputs/api")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

generator = UniversalGenerator(str(OUTPUT_DIR))

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Diagram Generator API",
        "version": "1.0.0"
    })

@app.route('/api/v1/diagrams/generate', methods=['POST'])
def generate_diagram():
    """
    Genera diagrama desde esquema universal
    
    Body:
    {
        "title": "BMC Architecture",
        "diagram_type": "network",
        "project_name": "bmc_input",
        "output_format": "both",
        "components": [...],
        "containers": [...],
        "connections": [...]
    }
    """
    try:
        # Validar request
        if not request.is_json:
            return jsonify({"error": "Content-Type debe ser application/json"}), 400
        
        data = request.get_json()
        
        # Validar campos requeridos
        required_fields = ["title", "diagram_type", "project_name"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo requerido: {field}"}), 400
        
        # Crear esquema desde JSON
        schema = UniversalDiagramSchema.from_dict(data)
        
        # Generar diagramas
        results = generator.generate(schema)
        
        # Preparar respuesta
        response = {
            "success": True,
            "schema": {
                "title": schema.title,
                "diagram_type": schema.diagram_type.value,
                "project_name": schema.project_name,
                "output_format": schema.output_format.value
            },
            "generated_files": {}
        }
        
        # Agregar rutas de archivos generados
        for format_type, file_path in results.items():
            if Path(file_path).exists():
                response["generated_files"][format_type] = {
                    "path": file_path,
                    "filename": Path(file_path).name,
                    "size_kb": round(Path(file_path).stat().st_size / 1024, 2),
                    "download_url": f"/api/v1/diagrams/download/{Path(file_path).name}"
                }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500

@app.route('/api/v1/diagrams/templates/<diagram_type>', methods=['GET'])
def get_template(diagram_type: str):
    """
    Obtiene template para tipo de diagrama
    
    Parámetros:
    - diagram_type: network, microservices, security, data_flow
    """
    try:
        # Validar tipo de diagrama
        if diagram_type not in [dt.value for dt in DiagramType]:
            return jsonify({"error": f"Tipo de diagrama no válido: {diagram_type}"}), 400
        
        # Generar template según tipo
        if diagram_type == "network":
            schema = SchemaBuilder.build_network_schema("sample_project")
        elif diagram_type == "microservices":
            schema = SchemaBuilder.build_microservices_schema("sample_project")
        else:
            # Template genérico
            schema = UniversalDiagramSchema(
                title=f"Sample {diagram_type.title()} Architecture",
                diagram_type=DiagramType(diagram_type),
                project_name="sample_project"
            )
        
        return jsonify({
            "success": True,
            "template": schema.to_dict(),
            "description": f"Template para diagrama de tipo {diagram_type}"
        }), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/v1/diagrams/download/<filename>', methods=['GET'])
def download_file(filename: str):
    """Descarga archivo generado"""
    try:
        # Buscar archivo en directorios de salida
        for subdir in ["png", "drawio"]:
            file_path = OUTPUT_DIR / subdir / filename
            if file_path.exists():
                return send_file(str(file_path), as_attachment=True)
        
        return jsonify({"error": "Archivo no encontrado"}), 404
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/v1/diagrams/validate', methods=['POST'])
def validate_schema():
    """
    Valida esquema sin generar diagrama
    
    Body: Mismo que /generate
    """
    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type debe ser application/json"}), 400
        
        data = request.get_json()
        
        # Intentar crear esquema
        schema = UniversalDiagramSchema.from_dict(data)
        
        # Validaciones adicionales
        errors = []
        warnings = []
        
        # Validar componentes
        if not schema.components and not schema.containers:
            errors.append("Debe tener al menos un componente o contenedor")
        
        # Validar conexiones
        all_component_ids = set()
        for comp in schema.components:
            all_component_ids.add(comp.id)
        for cont in schema.containers:
            for comp in cont.components:
                all_component_ids.add(comp.id)
        
        for conn in schema.connections:
            if conn.from_id not in all_component_ids:
                errors.append(f"Conexión desde componente inexistente: {conn.from_id}")
            if conn.to_id not in all_component_ids:
                errors.append(f"Conexión hacia componente inexistente: {conn.to_id}")
        
        # Validar canvas
        if schema.canvas.width < 800 or schema.canvas.height < 600:
            warnings.append("Canvas muy pequeño, recomendado mínimo 800x600")
        
        return jsonify({
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "schema_summary": {
                "components": len(schema.components),
                "containers": len(schema.containers),
                "connections": len(schema.connections),
                "canvas_size": f"{schema.canvas.width}x{schema.canvas.height}"
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            "valid": False,
            "errors": [str(e)],
            "warnings": []
        }), 400

@app.route('/api/v1/diagrams/batch', methods=['POST'])
def generate_batch():
    """
    Genera múltiples diagramas en batch
    
    Body:
    {
        "schemas": [
            { "title": "Network", "diagram_type": "network", ... },
            { "title": "Security", "diagram_type": "security", ... }
        ]
    }
    """
    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type debe ser application/json"}), 400
        
        data = request.get_json()
        schemas_data = data.get("schemas", [])
        
        if not schemas_data:
            return jsonify({"error": "Campo 'schemas' requerido con al menos un esquema"}), 400
        
        results = []
        
        for i, schema_data in enumerate(schemas_data):
            try:
                schema = UniversalDiagramSchema.from_dict(schema_data)
                generated_files = generator.generate(schema)
                
                results.append({
                    "index": i,
                    "success": True,
                    "title": schema.title,
                    "generated_files": {
                        format_type: {
                            "filename": Path(file_path).name,
                            "size_kb": round(Path(file_path).stat().st_size / 1024, 2)
                        }
                        for format_type, file_path in generated_files.items()
                    }
                })
                
            except Exception as e:
                results.append({
                    "index": i,
                    "success": False,
                    "error": str(e)
                })
        
        return jsonify({
            "success": True,
            "total_schemas": len(schemas_data),
            "successful": len([r for r in results if r["success"]]),
            "failed": len([r for r in results if not r["success"]]),
            "results": results
        }), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint no encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
