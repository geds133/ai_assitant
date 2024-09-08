from openai import OpenAI
import os
from backend.utils.logger import setup_logger

client = OpenAI(api_key=os.environ['open_ai_key'])

# Function to interact with the OpenAI API
def ask_llm(prompt):
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0
    )
    return response.choices[0].message.content

def main(prompt: str):
    """
    This is the main entry point for the AI assistant.

    Args:
        prompt (str): The prompt to deliver to the LLM.
    """

    # Call the function and print the result
    return ask_llm(prompt)