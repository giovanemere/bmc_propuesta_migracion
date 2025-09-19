#!/bin/bash

# BMC AWS Architecture Diagram Generator Script
# Generates PNG diagrams with AWS icons

echo "🚀 BMC AWS Architecture Diagram Generator"
echo "=========================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3 first."
    exit 1
fi

# Install system dependencies for graphviz
echo "📦 Installing system dependencies..."
if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y graphviz
elif command -v yum &> /dev/null; then
    sudo yum install -y graphviz
elif command -v brew &> /dev/null; then
    brew install graphviz
else
    echo "⚠️  Please install graphviz manually for your system"
fi

# Create virtual environment
echo "🐍 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Generate diagrams
echo "🎨 Generating BMC AWS Architecture Diagrams..."
python3 bmc_architecture.py

# Check if diagrams were generated
if ls *.png 1> /dev/null 2>&1; then
    echo ""
    echo "✅ Diagrams generated successfully!"
    echo ""
    echo "📁 Generated files:"
    ls -la *.png
    echo ""
    echo "🖼️  You can now view the PNG files with any image viewer"
    echo "📤 Upload these diagrams to your documentation or presentations"
else
    echo "❌ Error: No PNG files were generated"
    exit 1
fi

# Deactivate virtual environment
deactivate

echo ""
echo "🎉 BMC AWS Architecture Diagrams Generation Complete!"
echo "📍 Location: $(pwd)"
