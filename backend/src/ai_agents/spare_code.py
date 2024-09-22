import argparse


# Creating a parser
#parser = argparse.ArgumentParser()
#parser.add_argument("--subject", default="the weather")
#args = parser.parse_args()
#args.subject

# Prompt template for initial message and
# llm = OpenAI(api_key=os.environ['open_ai_key'])
# news_article_prompt = PromptTemplate(
#    template="Give me the latest news on {subject} and give me an as_of_date and the news sources",
#    input_variables=['subject'])
# news_summary_prompt = PromptTemplate(
#    template="Write me a short paragraph based on the news stories received about {subject} and assess the news sources credibility.",
#    input_variables=['subject'])
# news_article_chain = news_article_prompt | llm
# news_summary_chain = news_summary_prompt | llm
# news_chain = news_article_chain | news_summary_chain
# result = news_chain.invoke({"subject": subject})