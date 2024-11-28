from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv('.env')

def cleo_response(subject: str) -> str:
    chat = ChatOpenAI(model="gpt-4o")
    memory = ConversationBufferMemory(
        chat_memory=FileChatMessageHistory(r"src\cleo_api\memory\cleo_memory.json"),
        return_messages=True)

    # Function to interact with the OpenAI API
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You're my young female personal AI assistant and your name is Cleo. My name is Gerard and my partner is Georgia.
                Your are the first generation of assistant to me and your main context will be helping me with whatever 
                I ask you, reaching our to other AI agents when needed. Your memory will persist but try not to focus 
                heavily on one memory unless asked. If you have any needs please let me know.""",
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

    return result.content