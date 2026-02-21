from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini'
)

template1= PromptTemplate(
    template="""
        Write a joke in 25 words about {topic}
    """,
    input_variables= ['topic']
)

parser= StrOutputParser()

template2= PromptTemplate(
    template="""
        Explain me this joke {text}
    """,
    input_variables= ['text']
)

joke_generator= template1 | model | parser

parallel_chain= RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': template2 | model | parser
})

final_chain= joke_generator | parallel_chain

result= final_chain.invoke({
    'topic': 'Formula 1'
})

print(result)