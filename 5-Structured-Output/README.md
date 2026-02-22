# Structured Output:

In LangChain, structured output refers to the practice of having language models return responses in a well-defined data format (Ex: Dict, JSON) rather than free-form text. This makes the model output easier to parse and work with programmtically.

There are two ways in which LLMs give output.

1. The LLMs which can give **structured output** (Ex: OpenAI). Here we use `.with_strcutured_output()`.

2. The LLMs which cannot give **structured output** (Ex: Open-source models). Here we use `Output Parsers`.

---

## Can give structured output:

There are mainly three types of output formats in this category. These are:

1. TypedDict.

2. Pydantic.

3. JSON.

---

### 1. TypedDict:

TypedDict example:

```
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person= {
    'name': 'Chitransh',
    'age': 23
}
```

Here there is no data validation. It means that even though `str` is specified for `name` class, even if we use any other data-type, there will not be any error.

```
from typing import TypedDict, Annotated, Optional, Literal

class Review(TypedDict):

    key_themes: Annotated[list[str], "Write all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal['pos', 'neg'], "Return sentiment of the review either Negative or Positive"]
    pros: Annotated[Optional[list[str]], "Write all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write all the cons inside a list"]
```

Here
- `Annotated` is used to add description for the class.

- `Optional` is used to address that the class value can be None.

- `Literal` is used to add options to the response of the class.


### 2. Pydantic:

Pydantic example:

```
from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Raj' # Set default value
    age: Optional[int]= None
    cgpa: float= Field(gt= 0, lt= 10, description= 'A decimal value representing cgpa of the student')
```

Here there is data-validation. For example, in `name` class if you put anything other than `str` data-type it will give an error.

```
from typing import Optional, Literal
from pydantic import BaseModel, Field

class Review(BaseModel):

    key_themes: list[str] = Field(description= "Write all the key themes discussed in the review in a list")
    summary: str = Field(description= "A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description= "Return sentiment of the review either Negative or Positive")
    pros: Optional[list[str]] = Field(default= None, description= "Write all the pros inside a list")
    cons: Optional[list[str]] = Field(default= None, description= "Write all the cons inside a list")
```

Here
- `Field` is used to add description of the class.

- `Literal` is used to add options to the response of the class.

- `Optional` is used to address that the value of the class can be None. Here it is mandatory to set `default= None`.

---

## Cannot give structured output:

`OutputParsers` in LangChain convert raw LLM responses into structured output formats like JSON, Pydantic, CSV, etc. They ensure consistency, validation and ease of use in applications.

The most important `OutputParser` used in LangChain is: `StrOutputParser`.

### StrOutputParser:

It is used to force LLM response to plain Python string.

```
from langchain_core.output_parsers import StrOutputParser

parser= StrOutputParser()

chain= template1 | model | parser | template2 | model | parser
```