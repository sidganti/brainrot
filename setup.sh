#!/bin/bash

# AI Video Script & Creator Setup Script
echo "🎬 Setting up AI Video Script & Creator..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python version $python_version is too old. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python $python_version detected"

# Create virtual environment if it doesn't exist
if [ ! -d "env" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv env
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source env/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file..."
    cp env_example.txt .env
    echo "✅ .env file created"
    echo "⚠️ Please edit .env and add your OpenAI API key"
else
    echo "✅ .env file already exists"
fi

# Create output directory
mkdir -p output

# Test the setup
echo "🧪 Testing setup..."
python test_setup.py

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your OpenAI API key"
echo "2. Run the web app: streamlit run app.py"
echo "3. Or use CLI: python cli.py 'your video idea'"
echo ""
echo "For help, see README.md"