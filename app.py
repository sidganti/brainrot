import streamlit as st
import os
from dotenv import load_dotenv
from script_generator import VideoScriptGenerator

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Video Script Generator",
    page_icon="📝",
    layout="wide"
)

# Initialize components
@st.cache_resource
def init_script_generator():
    return VideoScriptGenerator()

def main():
    st.title("📝 AI Video Script Generator")
    st.markdown("Generate engaging video scripts from simple prompts using AI!")

    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        st.error("⚠️ Please set your OPENAI_API_KEY in the .env file")
        st.info("Copy env_example.txt to .env and add your API key")
        return

    # Initialize components
    script_generator = init_script_generator()

    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")

        # Script generation settings
        st.subheader("Script Generation")
        script_length = st.selectbox(
            "Script Length",
            ["30 seconds", "60 seconds", "90 seconds", "2 minutes"],
            index=1
        )

        script_style = st.selectbox(
            "Script Style",
            ["Educational", "Entertainment", "Professional", "Casual", "Dramatic"],
            index=0
        )

    # Main content area
    st.header("📝 Script Generation")

    # User input for script generation
    user_prompt = st.text_area(
        "Enter your video idea or topic:",
        placeholder="e.g., 'How to make the perfect cup of coffee' or 'The history of space exploration'",
        height=100
    )

    if st.button("🎯 Generate Script", type="primary"):
        if user_prompt.strip():
            with st.spinner("Generating your script..."):
                try:
                    script = script_generator.generate_script(
                        prompt=user_prompt,
                        length=script_length,
                        style=script_style
                    )

                    st.session_state['generated_script'] = script
                    st.success("✅ Script generated successfully!")

                except Exception as e:
                    st.error(f"❌ Error generating script: {str(e)}")
        else:
            st.warning("Please enter a prompt for script generation.")

    # Display generated script
    if 'generated_script' in st.session_state:
        st.subheader("📄 Generated Script")
        st.text_area(
            "Your script:",
            value=st.session_state['generated_script'],
            height=400,
            disabled=True
        )

        # Download script option
        script_bytes = st.session_state['generated_script'].encode()
        st.download_button(
            label="📥 Download Script",
            data=script_bytes,
            file_name="video_script.txt",
            mime="text/plain"
        )

    # Footer
    st.markdown("---")
    st.markdown(
        "**Powered by LangChain & OpenAI** | "
        "Create engaging video scripts from simple prompts!"
    )

if __name__ == "__main__":
    main()