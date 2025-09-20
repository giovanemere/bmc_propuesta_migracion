#!/usr/bin/env python3
"""
Script para mostrar prompts MCP generados
"""

from pathlib import Path

def show_mcp_prompts():
    """Muestra los prompts MCP generados"""
    
    print("📝 Prompts MCP Generados")
    print("=" * 40)
    
    prompts_dir = Path("outputs/mcp/diagrams/bmc_input/prompts/BMC_Input")
    
    if not prompts_dir.exists():
        print("❌ No se encontraron prompts MCP")
        return
    
    prompt_files = list(prompts_dir.glob("*.md"))
    
    if not prompt_files:
        print("❌ No hay archivos de prompts")
        return
    
    for prompt_file in sorted(prompt_files):
        print(f"\n📄 {prompt_file.name}")
        print(f"   📁 {prompt_file}")
        print(f"   📊 {prompt_file.stat().st_size:,} bytes")
        
        # Mostrar primeras líneas
        with open(prompt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()[:3]
            for line in lines:
                print(f"   {line.strip()}")
        
        if len(lines) >= 3:
            print("   ...")
    
    print(f"\n✅ Total prompts: {len(prompt_files)}")
    print(f"📁 Ubicación: {prompts_dir}")

if __name__ == "__main__":
    show_mcp_prompts()
