#!/bin/bash

# BMC Diagram Generator - Main Script with MCP Service
# Generates architecture diagrams from MCP model

echo "🚀 BMC Architecture Diagram Generator with MCP"
echo "=============================================="

# Check if MCP service should be used
if [ "$1" = "--mcp" ]; then
    echo "🔧 Using MCP Service..."
    cd "$(dirname "$0")"
    python3 mcp_service.py
    exit $?
fi

# Standard generation
cd "$(dirname "$0")/../infrastructure/diagrams"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Generate diagrams
echo "🎨 Generating diagrams..."
python3 generate_complete.py

# Move outputs
echo "📁 Moving outputs..."
mv *.png ../../output/png/ 2>/dev/null || true
mv *.drawio ../../output/drawio/ 2>/dev/null || true

echo "✅ Generation complete!"
echo "📊 PNG files: output/png/"
echo "🎨 Draw.io files: output/drawio/"
echo ""
echo "💡 Usage options:"
echo "  ./scripts/generate_diagrams.sh        # Standard generation"
echo "  ./scripts/generate_diagrams.sh --mcp  # Use MCP service"
