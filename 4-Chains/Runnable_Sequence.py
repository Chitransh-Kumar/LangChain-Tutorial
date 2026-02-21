from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini'
)

prompt1= PromptTemplate(
    template= """
        Write a joke on the topic {topic} in 30 words
    """,
    input_variables= ['topic']
)

parser= StrOutputParser()

prompt2= PromptTemplate(
    template= """
        Explain me the joke in 30 words
        {text}
    """,
    input_variables= ['text']
)

chain= RunnableSequence(prompt1, model, parser, prompt2, model, parser)

chain1= prompt1 | model | parser

joke= chain1.invoke({
    'topic': 'Formuala 1'
})

print(joke)

result= chain.invoke({
    'topic': 'Formula 1'
})

print(result)