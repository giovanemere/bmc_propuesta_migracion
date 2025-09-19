#!/bin/bash

# BMC Enhanced Diagram Generator - PNG + Draw.io
# Generates both PNG and Draw.io formats

echo "🚀 BMC Enhanced Architecture Diagram Generator"
echo "=============================================="
echo "Generating PNG + Draw.io formats"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Navigate to diagrams directory
cd "$(dirname "$0")"

# Activate virtual environment or create if doesn't exist
if [ ! -d "venv" ]; then
    echo "🐍 Creating Python virtual environment..."
    python3 -m venv venv
fi

echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📚 Installing Python dependencies..."
pip install -q diagrams==0.23.4 graphviz==0.20.1 Pillow==10.0.1

# Generate enhanced diagrams
echo ""
echo "🎨 Generating BMC AWS Architecture Diagrams..."
echo "   - PNG format (for presentations)"
echo "   - Draw.io format (for editing)"
echo ""

python3 bmc_drawio_generator.py

# Check if diagrams were generated
if ls *.png *.drawio 1> /dev/null 2>&1; then
    echo ""
    echo "✅ Enhanced diagrams generated successfully!"
    echo ""
    echo "📁 Generated files:"
    echo "PNG Files (for presentations):"
    ls -la *.png 2>/dev/null | awk '{print "  - " $9 " (" $5 " bytes)"}'
    echo ""
    echo "Draw.io Files (for editing):"
    ls -la *.drawio 2>/dev/null | awk '{print "  - " $9 " (" $5 " bytes)"}'
    echo ""
    echo "💡 Usage Instructions:"
    echo "  📊 PNG files: Use in PowerPoint, Google Slides, documents"
    echo "  🎨 Draw.io files: Open in https://app.diagrams.net for editing"
    echo "  📤 Both formats ready for sharing and collaboration"
else
    echo "❌ Error: No diagram files were generated"
    exit 1
fi

# Deactivate virtual environment
deactivate

echo ""
echo "🎉 BMC Enhanced Diagram Generation Complete!"
echo "📍 Location: $(pwd)"
echo "🔗 Open Draw.io files at: https://app.diagrams.net"
