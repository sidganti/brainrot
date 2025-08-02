#!/usr/bin/env python3
"""
Command-line interface for the AI Video Script Generator
"""

import os
import argparse
from dotenv import load_dotenv
from script_generator import VideoScriptGenerator

# Load environment variables
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="AI Video Script Generator CLI")
    parser.add_argument("prompt", help="Your video idea or topic")
    parser.add_argument("--length", default="60 seconds",
                       choices=["30 seconds", "60 seconds", "90 seconds", "2 minutes"],
                       help="Script length")
    parser.add_argument("--style", default="Educational",
                       choices=["Educational", "Entertainment", "Professional", "Casual", "Dramatic"],
                       help="Script style")
    parser.add_argument("--output-dir", default="./output",
                       help="Output directory for generated files")

    args = parser.parse_args()

    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please set your OpenAI API key in the .env file")
        return

    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)

    try:
        # Initialize components
        print("🚀 Initializing AI Video Script Generator...")
        script_generator = VideoScriptGenerator()

        # Generate script
        print(f"📝 Generating script for: {args.prompt}")
        print(f"   Length: {args.length}")
        print(f"   Style: {args.style}")

        script = script_generator.generate_script(
            prompt=args.prompt,
            length=args.length,
            style=args.style
        )

        # Save script to file
        script_filename = f"script_{args.prompt.replace(' ', '_')[:30]}.txt"
        script_path = os.path.join(args.output_dir, script_filename)

        with open(script_path, 'w') as f:
            f.write(script)

        print(f"✅ Script generated and saved to: {script_path}")
        print("\n" + "="*50)
        print("GENERATED SCRIPT:")
        print("="*50)
        print(script)
        print("="*50)

        print("📄 Script generation complete!")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()