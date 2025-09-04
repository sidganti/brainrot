import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

class TopicsResponseModel(BaseModel):
    """
    A model that represents the response from the topic generator.
    """
    topics: list[str] = Field(description="A list of topics for the niche")

class TopicGenerator:
    """
    A class that generates topics for AI niche videos.
    """

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.7,
            api_key=os.getenv("GEMINI_API_KEY")
        )

        # Create structured output LLM
        self.structured_llm = self.llm.with_structured_output(TopicsResponseModel)

        self.topic_prompt_template = ChatPromptTemplate.from_template(
            """You are a content creator that specializes in making short AI generated videos for social media.

            You will be given a niche and a number of topics to generate.

            Your task:
            - Generate a list of {number_of_topics} engaging, relevant topics for the "{niche}" niche.
            - Each topic should be short, catchy, and suitable as a video idea.
            - Do not include any explanations or extra text, just the list.
            """
        )

    def generate_topics(self, niche: str, number_of_topics: int) -> str:
        """
        Generate a list of topics based on the niche and number of topics.
        Returns:
            str: Formatted string with numbered topics.
        """
        prompt = self.topic_prompt_template.format(
            niche=niche,
            number_of_topics=number_of_topics
        )
        response = self.llm.invoke(prompt)

        # Format the response to match the desired output format
        topics_text = response.content.strip()
        formatted_topics = []

        # Split by lines and format each topic
        lines = topics_text.split('\n')
        topic_count = 1
        for line in lines:
            line = line.strip()
            if line and not line.startswith('Topic'):
                formatted_topics.append(f"Topic {topic_count}: {line}")
                topic_count += 1
            elif line.startswith('Topic'):
                formatted_topics.append(line)
                topic_count += 1

        return '\n'.join(formatted_topics)