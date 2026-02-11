from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1= PromptTemplate(
    template= """
    Generate a detailed report on {topic}
    """,
    input_variables= ['topic']
)

prompt2= PromptTemplate(
    template= """
    Generate a 5 point summary from the given text 
    {text}
    """,
    input_variables= ['text']
)

model = ChatOpenAI(
    model= 'gpt-4o-mini'
)

parser= StrOutputParser()

chain= prompt1 | model | parser | prompt2 | model | parser

result= chain.invoke({
    'topic': 'IT Jobs in India'
})

print(result)

# To visualize the chain
chain.get_graph().print_ascii()