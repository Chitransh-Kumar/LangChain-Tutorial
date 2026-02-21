from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini'
)

prompt1= PromptTemplate(
    template= """
        Tell me a joke on the topic {topic}
    """,
    input_variables= ['topic']
)

prompt2= PromptTemplate(
    template= """
        Explain in less than 50 words about the topic {topic}
    """,
    input_variables= ['topic']
)

prompt3= PromptTemplate(
    template= """
        Give me a fact about the topic {topic}
    """,
    input_variables= ['topic']
)

parser= StrOutputParser()

joke_chain= prompt1 | model | parser
explaination_chain= prompt2 | model | parser
fact_chain= prompt3 | model | parser

branch_chain= RunnableBranch(
    (lambda x: x['type']=='Joke', joke_chain),
    (lambda x: x['type']=='Explaination', explaination_chain),
    fact_chain
)

user_topic= input("Enter topic: ")
user_type= input("Enter type: ")

result= branch_chain.invoke({
    'topic': user_topic,
    'type': user_type
})

print(result)