# Prompts

These are the instructions given to a model to guide its output.

---

There are two ways in which messages are sent to LLMs.

## 1. Single Message: 

(Single stand alone query)

###  Static Message

###  Dynamic Message

Use PromptTemplate here. When we need to pass some user-input in the prompt.

```
from langchain_core.prompts import PromptTemplate
```

---

## 2. List of Messages: 

(Multi-turn conversation)

###  Static Message

Three types of Messages: `SystemMessage`, `HumanMessage` and `AIMessage`.

```
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
```

### Dynamic Message 

Similar to Dynamic Message in single message but this is used for multi-turn conversation. Use ChatPromptTemplate here.

```
from langchain_core.prompts import ChatPromptTemplate
```