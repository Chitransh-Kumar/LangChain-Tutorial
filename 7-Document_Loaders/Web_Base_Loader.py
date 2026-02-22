from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini'
)

prompt= PromptTemplate(
    template="""
        Answer the following question
        {question} from the following text
        {text}
    """,
    input_variables= ['question', 'text']
)

parser= StrOutputParser()

url= 'https://en.wikipedia.org/wiki/Attention_Is_All_You_Need#:~:text=%22Attention%20Is%20All%20You%20Need,eight%20scientists%20working%20at%20Google.'

loader= WebBaseLoader(url)

docs= loader.load()

chain= prompt | model | parser

question= input("Enter the question here: ")

result= chain.invoke({
    'question': question,
    'text': docs[0].page_content
})

print(result)