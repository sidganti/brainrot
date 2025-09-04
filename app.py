import streamlit as st
import os
from dotenv import load_dotenv
from topic_generator import TopicGenerator

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Brainrot AI Slop Generator",
    page_icon="",
    layout="wide"
)

# Initialize components
@st.cache_resource
def init_topic_generator():
    return TopicGenerator()

def main():
    st.title("🤖 Brainrot AI Slop Generator")
    st.markdown("Create Brainrot videos using AI Agents and LLMs!")

    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        st.error("⚠️ Please set your OPENAI_API_KEY in the .env file")
        st.info("Copy env_example.txt to .env and add your API key")
        return

    # Initialize components
    topic_generator = init_topic_generator()

    # Main content area
    st.header("📝 Topics Generation")

    # User input for topics generation
    niche = st.selectbox(
        "Select a niche",
        ["POV-History"],
        index=0,
        placeholder="Select a niche..."
    )

    number_of_topics = st.number_input(
        "Enter the number of topics",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )

    if st.button("🎯 Generate Topics", type="primary"):
        with st.spinner("Generating your script..."):
            try:
                topics = topic_generator.generate_topics(
                    niche=niche,
                    number_of_topics=number_of_topics
                )

                st.session_state['generated_topics'] = topics
                st.success("✅ Topics generated successfully!")
            except Exception as e:
                st.error(f"❌ Error generating topics: {str(e)}")

    # Display generated topics
    if 'generated_topics' in st.session_state:
        st.subheader("📄 Generated Topics")
        # Try to split the generated_topics string into a list and display as a numbered list
        topics = st.session_state['generated_topics']

        st.text_area(
            "Your topics:",
            value=topics,
            height=100,
            disabled=True
        )

    # Footer
    st.markdown("---")
    st.markdown(
        "**Powered by LangChain & OpenAI** | "
        "Create engaging video scripts from simple prompts!"
    )

if __name__ == "__main__":
    main()