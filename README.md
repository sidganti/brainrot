# 📝 AI Video Script Generator

A LangChain-powered application that generates engaging video scripts from simple prompts using AI.

## Features

- **📝 Script Generation**: Create engaging video scripts from simple prompts
- **🎨 Multiple Styles**: Choose from various script styles (Educational, Entertainment, Professional, etc.)
- **⚙️ Customizable**: Adjust length and style preferences
- **💾 Download Support**: Save scripts locally
- **🌐 Web Interface**: Beautiful Streamlit web application
- **💻 Command Line**: CLI for automation and batch processing

## Quick Start

### 1. Setup Environment

```bash
# Clone the repository
git clone <your-repo-url>
cd brainrot

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

Copy the environment example file and add your API key:

```bash
cp env_example.txt .env
```

Edit `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Run the Application

```bash
# Web interface
streamlit run app.py

# Or command line
python cli.py "How to make the perfect cup of coffee"
```

The web application will open in your browser at `http://localhost:8501`

## Usage

### Web Interface

1. **Enter your video idea** in the text area
   - Example: "How to make the perfect cup of coffee"
   - Example: "The history of space exploration"

2. **Configure settings** in the sidebar:
   - **Script Length**: 30 seconds to 2 minutes
   - **Script Style**: Educational, Entertainment, Professional, etc.

3. **Generate script** by clicking the "Generate Script" button

4. **Download** the generated script as a text file

### Command Line

```bash
# Basic usage
python cli.py "How to make coffee"

# With options
python cli.py "Space exploration history" --length "90 seconds" --style "Educational"

# Save to specific directory
python cli.py "Cooking tutorial" --output-dir "./my_scripts"
```

## Project Structure

```
brainrot/
├── app.py                 # Main Streamlit application
├── script_generator.py    # LangChain script generation
├── cli.py                # Command-line interface
├── requirements.txt       # Python dependencies
├── env_example.txt       # Environment variables template
└── README.md            # This file
```

## Architecture

### Script Generation (`script_generator.py`)

- Uses **LangChain** with **OpenAI GPT-4** for script generation
- Implements structured prompts for consistent output
- Supports multiple script styles and lengths
- Includes script enhancement and variation features

### Web Interface (`app.py`)

- **Streamlit** web application
- **Real-time** script generation
- **Download** functionality for generated content
- **Configuration** options in sidebar

### Command Line (`cli.py`)

- **CLI** for automation and batch processing
- **File output** with customizable directory
- **Command-line options** for all settings

## Dependencies

- **LangChain**: AI/LLM framework
- **OpenAI**: GPT-4 for script generation
- **Streamlit**: Web application framework
- **Python-dotenv**: Environment variable management

## Script Styles

### Available Styles:

- **Educational**: Informative, fact-based content
- **Entertainment**: Engaging, fun, and entertaining
- **Professional**: Business-appropriate, formal tone
- **Casual**: Relaxed, conversational style
- **Dramatic**: Emotional, impactful storytelling

### Script Lengths:

- **30 seconds**: Quick, concise content
- **60 seconds**: Standard short-form content
- **90 seconds**: Extended short-form content
- **2 minutes**: Longer, detailed content

## Advanced Features

### Script Enhancement

The application can enhance existing scripts with:
- Better engagement hooks
- Improved transitions
- Enhanced storytelling elements

### Script Variations

Generate multiple variations of the same topic:
- Different angles and perspectives
- Alternative hooks and conclusions
- Various storytelling approaches

## Customization

### Adding New Script Styles

Edit `script_generator.py` and add new styles to the prompt template:

```python
script_style = st.selectbox(
    "Script Style",
    ["Educational", "Entertainment", "Professional", "Casual", "Dramatic", "Your New Style"],
    index=0
)
```

### Modifying Script Lengths

Update the length options in both `app.py` and `cli.py`:

```python
script_length = st.selectbox(
    "Script Length",
    ["30 seconds", "60 seconds", "90 seconds", "2 minutes", "5 minutes"],
    index=1
)
```

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your OpenAI API key is set in `.env`
   - Check that the key is valid and has sufficient credits

2. **Import Errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Check your Python version (3.8+ recommended)

3. **Generation Fails**
   - Check your internet connection
   - Verify API rate limits
   - Ensure your prompt is clear and specific

### Performance Tips

- Keep prompts clear and specific for better results
- Use appropriate script lengths for your content
- Choose the right style for your target audience

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Check the troubleshooting section above
- Review the LangChain documentation
- Check OpenAI API documentation

---

**Powered by LangChain & OpenAI** 🚀