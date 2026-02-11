from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model= ChatOpenAI(
    model= 'gpt-4o-mini'
)

str_parser= StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(
        description= "Give the sentiment of the feedback"
    )

pydantic_parser= PydanticOutputParser(pydantic_object= Feedback)

prompt1= PromptTemplate(
    template= """
    Classify the sentiment of the following feedback into positive or negative 
    {text}
    {format_inst}
    """,
    input_variables= ['text'],
    partial_variables= {
        'format_inst': pydantic_parser.get_format_instructions()
    }
)

classifier_chain= prompt1 | model | pydantic_parser

prompt2= PromptTemplate(
    template= """
    Write an appropriate response to this positive feedback 
    {feedback}
    """,
    input_variables= ['feedback']
)

prompt3= PromptTemplate(
    template= """
    Write an appropriate response to this negative feedback 
    {feedback}
    """,
    input_variables= ['feedback']
)

branch_chain= RunnableBranch(
    # Format-> (condition, if condition is True then which chain) : Just like if-elif
    (lambda x: x.sentiment=='positive', prompt2 | model | str_parser),
    (lambda x: x.sentiment=='negative', prompt3 | model | str_parser),
    # (Default chain) : Just like final else
    RunnableLambda(lambda x: "Could not find sentiment")
)

merged_chain= classifier_chain | branch_chain

result= merged_chain.invoke({
    'text': "This is a terrible phone"
})

print(result)