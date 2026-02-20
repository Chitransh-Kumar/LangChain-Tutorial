from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

template= PromptTemplate(
    template="""
    Give me a 5-line summary about {topic}
""",
    input_variables= ['topic']
)

model= ChatOpenAI(
    model= 'gpt-4o-mini',
    temperature= 0.8
)

chain= template | model

result= chain.invoke({
    "topic" : "Formula 1"
})

print(result.content)