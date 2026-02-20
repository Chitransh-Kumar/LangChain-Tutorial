from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini',
    max_completion_tokens= 50
)

messages= [
    SystemMessage(content= "You are a helpful assisstant"),
    HumanMessage(content= "Tell me about Formula 1")
]

result= model.invoke(messages)

messages.append(AIMessage(content= result.content))

print(messages)