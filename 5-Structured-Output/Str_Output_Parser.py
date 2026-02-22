from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini'
)

# 1st prompt -> Detailed report
template1= PromptTemplate(
    template= """
        Write a detailed about topic {topic} in less than 100 words.
    """,
    input_variables= ['topic']
)

# 2nd prompt -> Summary
template2= PromptTemplate(
    template= """
        Write a 5 line summary on the following text {text}
    """,
    input_variables= ['text']
)

parser= StrOutputParser()

chain= template1 | model | parser | template2 | model | parser

result= chain.invoke({
    'topic': 'Formula 1'
})

print(result)