from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini'
)

template1= PromptTemplate(
    template="""
        Write a joke in less than 30 words on the topic {topic}
    """,
    input_variables= ['topic']
)

parser= StrOutputParser()

joke_generator= template1 | model | parser

def length_calculator(text):
    return len(text.split())

parallel_chain= RunnableParallel({
    'joke': RunnablePassthrough(),
    'length_count': RunnableLambda(length_calculator)
})

final_chain= joke_generator | parallel_chain

result= final_chain.invoke({
    'topic': 'Formula 1'
})

print(result)