#!/usr/bin/env python3
"""
Debug script to test OpenAI API connection
"""

import os
import requests
from dotenv import load_dotenv

def test_api_key():
    """Test if the API key is valid and working."""
    print("🔍 Testing OpenAI API Key...")

    # Load environment variables
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("❌ No API key found in environment variables")
        print("   Make sure you have a .env file with OPENAI_API_KEY=your_key_here")
        return False

    if not api_key.startswith("sk-"):
        print("❌ API key format looks incorrect")
        print("   OpenAI API keys should start with 'sk-'")
        return False

    print(f"✅ API key found: {api_key[:10]}...{api_key[-4:]}")

    # Test API connection
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Test with a simple completion request
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hello"}],
        "max_tokens": 10
    }

    try:
        print("🌐 Testing API connection...")
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        print(f"📊 Response Status: {response.status_code}")

        if response.status_code == 200:
            print("✅ API connection successful!")
            result = response.json()
            print(f"📝 Response: {result['choices'][0]['message']['content']}")
            return True
        else:
            print(f"❌ API request failed with status {response.status_code}")
            print(f"📄 Response: {response.text}")

            if response.status_code == 401:
                print("🔑 Authentication failed - check your API key")
            elif response.status_code == 429:
                print("⏰ Rate limit exceeded or quota exceeded")
            elif response.status_code == 402:
                print("💳 Payment required - check your billing")
            elif response.status_code == 403:
                print("🚫 Access forbidden - check your API key permissions")

            return False

    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_environment():
    """Test environment setup."""
    print("\n🔍 Testing Environment...")

    # Check if .env file exists
    if os.path.exists(".env"):
        print("✅ .env file found")
    else:
        print("❌ .env file not found")
        print("   Create .env file with: OPENAI_API_KEY=your_key_here")
        return False

    # Check Python version
    import sys
    python_version = sys.version_info
    print(f"✅ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")

    # Check required packages
    try:
        import requests
        print("✅ requests package available")
    except ImportError:
        print("❌ requests package not available")
        return False

    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv package available")
    except ImportError:
        print("❌ python-dotenv package not available")
        return False

    return True

def main():
    """Run all tests."""
    print("🚀 OpenAI API Debug Tool")
    print("=" * 50)

    # Test environment
    env_ok = test_environment()

    if not env_ok:
        print("\n❌ Environment issues found. Please fix them first.")
        return

    # Test API key
    api_ok = test_api_key()

    print("\n" + "=" * 50)
    print("📊 Debug Results:")
    print("=" * 50)

    if api_ok:
        print("🎉 API connection is working!")
        print("\nIf you're still not seeing requests in the dashboard:")
        print("1. Check if you're looking at the right account")
        print("2. Try refreshing the dashboard")
        print("3. Check if there's a delay in the dashboard updates")
        print("4. Verify you're using the correct API key")
    else:
        print("❌ API connection failed")
        print("\nCommon solutions:")
        print("1. Check your OpenAI account billing")
        print("2. Verify your API key is correct")
        print("3. Make sure you have sufficient credits")
        print("4. Check your network connection")

if __name__ == "__main__":
    main()