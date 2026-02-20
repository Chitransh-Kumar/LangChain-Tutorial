# Components of LangChain:

There are total 6 components in LangChain. These are:

-  Models.
-  Prompts.
-  Chains.
-  Memory.
-  Indexes.
-  Agents.

## 1. Models:

Models are the interfaces through which the user interact with AI models.

There are two types of Models:

- 1. `Language Model (LLM)`: Here input is text and output is text.

- 2. `Embedding Models`: Here input is text and output is vectors.


## 2. Prompts:

Prompts are the inputs provided to the LLMs.

## 3. Chains:

Chains decide the pipeline/workflow of a task for LLM. It converts output of one task to input of another task.

## 4. Indexes:

Indexes connect your application to external knowledge such as PDFs, websites or databases.

Components: Document loader, Text splitter, vector stores, Retreivers.

## 5. Memory:

Types of memory:

-  Conversation buffer memory.
-  Conversation buffer window memory.
-  Summarization-based memory.
-  Custom memory.
