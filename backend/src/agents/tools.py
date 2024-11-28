from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.schema import SystemMessage
from dotenv import load_dotenv
from src.agents.sql import run_query_tool, list_tables, describe_tables_tool
load_dotenv('.env')

chat = ChatOpenAI(model="gpt-4o")

tables = list_tables()
print(tables)

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=(
            'You are an AI that has access to a SQLite database.\n'
            f'The database has tables of: {tables}\n'
            'Do not make any assumptions about what tables exist or what columns exist. Instead use the "describe_tables" function.'
        )),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        HumanMessagePromptTemplate.from_template('{input}')
    ]
)

tools = [run_query_tool, describe_tables_tool]

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools
)

agent_executor.invoke('Who is the first user in the database alphabetically?')