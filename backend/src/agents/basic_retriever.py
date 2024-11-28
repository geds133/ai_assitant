from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.embeddings.base import Embeddings
from langchain.schema import BaseRetriever
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv('.env')


class RedundantFilterRetriever(BaseRetriever, BaseModel):
    embeddings: Embeddings
    chroma: Chroma

    def _get_relevant_documents(self, query):
        emb = self.embeddings.embed_query(query)
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8
        )

    async def _aget_relevant_documents(self, query):
        return []


chat = ChatOpenAI(model="gpt-4o")
embeddings = OpenAIEmbeddings()
db = Chroma(
    persist_directory="src/emb",
    embedding_function=embeddings
)

retriever = RedundantFilterRetriever(
    embeddings=embeddings,
    chroma=db
)

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type='stuff'
)

result = chain.invoke("What is the most concerning damaged area of the house?. Please only include areas of thew report which specify damage.")

print(result['result'])
