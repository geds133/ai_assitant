from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PDFMinerLoader
from dotenv import load_dotenv

load_dotenv('.env')


def ask_llm(subject: str) -> str:
    chat = ChatOpenAI(model="gpt-4o")
    memory = ConversationBufferMemory(
        chat_memory=FileChatMessageHistory("cleo_memory.json"),
        return_messages=True)

    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, separators='\n\n')

    # Initialize the loader with the path to your PDF
    pdf_loader = PDFMinerLoader('src/document_database/house/Homebuyers Report.pdf')

    # Load the text content from the PDF
    documents = pdf_loader.load()

    # Split the loaded PDF documents into chunks
    chunked_docs = text_splitter.split_documents(documents)


    db = Chroma.from_documents(
        chunked_docs,
        embedding=embeddings,
        persist_directory="src/emb"
    )

    results = db.similarity_search_with_score("What is the most concerning damaged area?", k=1)

    for result in results:
        print("\n")
        print(result[1])
        print(result[0].page_content)


    # Now you can use `documents` with other LangChain components (e.g., summarization, question answering)
    for document in documents:
        print(document.page_content)


    # Function to interact with the OpenAI API
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a personal assistant who will help with automating life tasks and providing information. Generally try to keep answers as concise as possible.",
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

if __name__ == '__main__':

    ask_llm(subject='Gaza')
