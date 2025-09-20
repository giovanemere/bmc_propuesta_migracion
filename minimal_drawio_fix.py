#!/usr/bin/env python3
"""
Solución mínima para error mxCell DrawIO
"""

def create_valid_drawio():
    """Crea archivo DrawIO válido mínimo"""
    
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net">
  <diagram name="BMC Architecture" id="1">
    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="2" value="BMC System" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="200" width="120" height="60" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    output_file = "outputs/mcp/diagrams/bmc_input/drawio/bmc_minimal_fixed.drawio"
    
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w') as f:
        f.write(xml)
    
    print(f"✅ DrawIO mínimo creado: {output_file}")
    return output_file

if __name__ == "__main__":
    create_valid_drawio()
