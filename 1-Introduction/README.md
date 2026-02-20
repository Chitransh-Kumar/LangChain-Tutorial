# Components of LangChain:

There are total 6 components in LangChain. These are:

- 1. Models.
- 2. Prompts.
- 3. Chains.
- 4. Memory.
- 5. Indexes.
- 6. Agents.

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

- 1. Conversation buffer memory.
- 2. Conversation buffer window memory.
- 3. Summarization-based memory.
- 4. Custom memory.