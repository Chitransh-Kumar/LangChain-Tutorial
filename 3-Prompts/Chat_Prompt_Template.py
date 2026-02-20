from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini'
)

chat_template= ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain me about {topic} in 50 words.')
])

chain= chat_template | model

result= chain.invoke({
    'domain': 'Formula 1',
    'topic': 'Drag Reduction System'
})

print(result.content)