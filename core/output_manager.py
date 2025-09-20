#!/usr/bin/env python3
"""
Output Manager - Gestiona la estructura de salida de archivos MCP
"""

import os
from pathlib import Path
from typing import Dict, Any
from datetime import datetime

class OutputManager:
    """Gestor de estructura de salida organizada"""
    
    def __init__(self, base_output_dir: str = "outputs"):
        self.base_output_dir = Path(base_output_dir)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def create_project_structure(self, project_name: str) -> Dict[str, Path]:
        """Crea estructura organizada para un proyecto"""
        
        # Normalizar nombre del proyecto
        clean_name = project_name.lower().replace(" ", "_").replace("-", "_")
        
        # Crear estructura de directorios
        project_dir = self.base_output_dir / clean_name
        
        structure = {
            "project_root": project_dir,
            "diagrams": project_dir / "diagrams",
            "png": project_dir / "diagrams" / "png",
            "drawio": project_dir / "diagrams" / "drawio", 
            "svg": project_dir / "diagrams" / "svg",
            "documentation": project_dir / "documentation",
            "config": project_dir / "config",
            "reports": project_dir / "reports"
        }
        
        # Crear todos los directorios
        for dir_path in structure.values():
            dir_path.mkdir(parents=True, exist_ok=True)
        
        return structure
    
    def organize_outputs(self, project_name: str, generated_files: Dict[str, str]) -> Dict[str, str]:
        """Organiza archivos generados en estructura correcta"""
        
        structure = self.create_project_structure(project_name)
        organized_files = {}
        
        for file_type, file_path in generated_files.items():
            if not os.path.exists(file_path):
                continue
                
            source_path = Path(file_path)
            
            # Determinar destino según tipo de archivo
            if file_path.endswith('.png'):
                dest_dir = structure["png"]
                category = "diagrams_png"
            elif file_path.endswith('.drawio'):
                dest_dir = structure["drawio"]
                category = "diagrams_drawio"
            elif file_path.endswith('.svg'):
                dest_dir = structure["svg"]
                category = "diagrams_svg"
            else:
                dest_dir = structure["documentation"]
                category = "documentation"
            
            # Generar nombre de archivo organizado
            clean_type = file_type.replace("drawio_", "").replace("_", "-")
            dest_filename = f"{project_name.lower()}_{clean_type}_{self.timestamp}{source_path.suffix}"
            dest_path = dest_dir / dest_filename
            
            # Copiar archivo
            import shutil
            shutil.copy2(source_path, dest_path)
            
            organized_files[f"{category}_{clean_type}"] = str(dest_path)
        
        # Generar reporte de archivos
        self._generate_file_report(structure, organized_files)
        
        return organized_files
    
    def _generate_file_report(self, structure: Dict[str, Path], organized_files: Dict[str, str]):
        """Genera reporte de archivos organizados"""
        
        report_content = f"""# MCP Output Report
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Project Structure
```
{structure['project_root'].name}/
├── diagrams/
│   ├── png/          # PNG diagrams for presentations
│   ├── drawio/       # Editable Draw.io files
│   └── svg/          # SVG vector diagrams
├── documentation/    # Generated documentation
├── config/          # MCP configuration files
└── reports/         # Generation reports
```

## Generated Files
"""
        
        # Agrupar archivos por categoría
        categories = {}
        for file_key, file_path in organized_files.items():
            category = file_key.split('_')[0] + '_' + file_key.split('_')[1]
            if category not in categories:
                categories[category] = []
            categories[category].append((file_key, file_path))
        
        for category, files in categories.items():
            report_content += f"\n### {category.replace('_', ' ').title()}\n"
            for file_key, file_path in files:
                file_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0
                report_content += f"- `{Path(file_path).name}` ({file_size:,} bytes)\n"
        
        # Guardar reporte
        report_path = structure["reports"] / f"generation_report_{self.timestamp}.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
    
    def cleanup_old_outputs(self, keep_last: int = 5):
        """Limpia outputs antiguos manteniendo los últimos N"""
        
        if not self.base_output_dir.exists():
            return
        
        # Buscar directorios de proyectos
        for project_dir in self.base_output_dir.iterdir():
            if not project_dir.is_dir():
                continue
                
            reports_dir = project_dir / "reports"
            if not reports_dir.exists():
                continue
            
            # Obtener reportes ordenados por fecha
            reports = sorted(reports_dir.glob("generation_report_*.md"))
            
            # Eliminar reportes antiguos
            if len(reports) > keep_last:
                for old_report in reports[:-keep_last]:
                    timestamp = old_report.stem.split('_')[-1]
                    
                    # Eliminar archivos asociados a ese timestamp
                    for subdir in ["png", "drawio", "svg"]:
                        diagram_dir = project_dir / "diagrams" / subdir
                        if diagram_dir.exists():
                            for old_file in diagram_dir.glob(f"*_{timestamp}.*"):
                                old_file.unlink()
                    
                    # Eliminar reporte
                    old_report.unlink()
    
    def get_latest_outputs(self, project_name: str) -> Dict[str, str]:
        """Obtiene los outputs más recientes de un proyecto"""
        
        clean_name = project_name.lower().replace(" ", "_").replace("-", "_")
        project_dir = self.base_output_dir / clean_name
        
        if not project_dir.exists():
            return {}
        
        latest_files = {}
        
        # Buscar archivos más recientes en cada categoría
        for subdir in ["png", "drawio", "svg"]:
            diagram_dir = project_dir / "diagrams" / subdir
            if not diagram_dir.exists():
                continue
                
            files = sorted(diagram_dir.glob(f"{clean_name}_*"), key=lambda x: x.stat().st_mtime, reverse=True)
            
            for file_path in files:
                # Extraer tipo de diagrama del nombre
                parts = file_path.stem.split('_')
                if len(parts) >= 3:
                    diagram_type = '_'.join(parts[1:-1])  # Excluir proyecto y timestamp
                    key = f"{subdir}_{diagram_type}"
                    if key not in latest_files:  # Solo el más reciente
                        latest_files[key] = str(file_path)
        
        return latest_files
