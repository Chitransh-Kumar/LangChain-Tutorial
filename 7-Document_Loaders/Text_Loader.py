from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini'
)

prompt= PromptTemplate(
    template="""
        Write a summary for the following poem in 50 words
        {poem}
    """,
    input_variables= ['poem']
)

parser= StrOutputParser()

loader= TextLoader('cricket.txt', encoding= 'utf-8')

docs= loader.load()

chain= prompt | model | parser

result= chain.invoke({
    'poem': docs[0].page_content
})

print(result)