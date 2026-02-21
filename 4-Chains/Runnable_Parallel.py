from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini',
    temperature= 1
)

linkedin_post_prompt= PromptTemplate(
    template= """
        Write a LinkedIn post on the topic {topic} in less than 40 words.
    """,
    input_variables= ['topic']
)

parser= StrOutputParser()

x_post_prompt= PromptTemplate(
    template= """
        Write a X post on the topic {topic} in less than 30 words.
    """,
    input_variables= ['topic']
)

parallel_chain= RunnableParallel({
    'linkedin': linkedin_post_prompt | model | parser,
    'x': x_post_prompt | model | parser
})

result= parallel_chain.invoke({
    'topic': 'Formula 1'
})

print(result)