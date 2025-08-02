#!/usr/bin/env python3
"""
Test script to verify the AI Video Script Generator setup
"""

import sys
import os

def test_imports():
    """Test if all required packages can be imported."""
    print("🔍 Testing imports...")

    try:
        import streamlit
        print("✅ streamlit imported successfully")
    except ImportError as e:
        print(f"❌ streamlit import failed: {e}")
        return False

    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ python-dotenv import failed: {e}")
        return False

    try:
        from langchain_openai import ChatOpenAI
        print("✅ langchain-openai imported successfully")
    except ImportError as e:
        print(f"❌ langchain-openai import failed: {e}")
        return False

    try:
        from langchain.prompts import ChatPromptTemplate
        print("✅ langchain.prompts imported successfully")
    except ImportError as e:
        print(f"❌ langchain.prompts import failed: {e}")
        return False

    try:
        import requests
        print("✅ requests imported successfully")
    except ImportError as e:
        print(f"❌ requests import failed: {e}")
        return False

    return True

def test_environment():
    """Test environment variables."""
    print("\n🔍 Testing environment...")

    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✅ Environment variables loaded")
    except Exception as e:
        print(f"❌ Failed to load environment variables: {e}")
        return False

    # Check for OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("✅ OPENAI_API_KEY found")
        return True
    else:
        print("⚠️ OPENAI_API_KEY not found")
        print("   Please add your OpenAI API key to the .env file")
        return False

def test_local_modules():
    """Test if local modules can be imported."""
    print("\n🔍 Testing local modules...")

    try:
        from script_generator import VideoScriptGenerator
        print("✅ script_generator imported successfully")
    except ImportError as e:
        print(f"❌ script_generator import failed: {e}")
        return False

    return True

def main():
    """Run all tests."""
    print("🚀 Testing AI Video Script Generator Setup")
    print("=" * 50)

    # Test imports
    imports_ok = test_imports()

    # Test environment
    env_ok = test_environment()

    # Test local modules
    modules_ok = test_local_modules()

    print("\n" + "=" * 50)
    print("📊 Test Results:")
    print("=" * 50)

    if imports_ok and env_ok and modules_ok:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nTo run the application:")
        print("1. Make sure your OpenAI API key is in the .env file")
        print("2. Run: streamlit run app.py")
        print("3. Or use CLI: python cli.py 'your video idea'")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        print("\nCommon solutions:")
        print("1. Install missing packages: pip install -r requirements.txt")
        print("2. Add your OpenAI API key to .env file")
        print("3. Check Python version (3.8+ recommended)")

    return imports_ok and env_ok and modules_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)