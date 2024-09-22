from langchain.prompts import PromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv('.env')

chat = ChatOpenAI(model="gpt-4o")
memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    return_messages=True)


if __name__ == '__main__':

    while True:
        subject = input('>> ')
        # Function to interact with the OpenAI API
        prompt = ChatPromptTemplate.from_messages(
            [
            (
                "system",
                "You're an assistant who's good at but {content}. Respond in 20 words or fewer",
            ),
            MessagesPlaceholder(variable_name='history'),
            HumanMessagePromptTemplate.from_template('{content}')
            ]
        )

        chain = prompt | chat

        # Load the previous conversation from memory, or start fresh if empty
        memory_vars = memory.load_memory_variables({})
        messages = memory_vars.get('history', [])

        result = chain.invoke({'content': subject,
                               'history': messages})

        memory.save_context(
            {"content": subject},  # What was asked (input)
            {"content": result.content}  # What was responded (output)
        )

        print(result.content)