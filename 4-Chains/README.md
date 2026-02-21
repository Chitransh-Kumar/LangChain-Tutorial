# Runnables:

There are five types of runnables in LangChain. These are:

1. Runnable Sequence.

2. Runnable Parallel.

3. Runnable Passthrough.

4. Runnable Lambda.

5. Runnable Branch.

## Runnable Sequence:

This is the most common form of runnable. It is the simplest linear form of forming chains.

```
from langchain_core.runnables import RunnableSequence
```

Alternative way:

```
chain1= prompt1 | model | parser
```

## Runnable Parallel:

This is used to form parallel chains. When we need to perform two or more tasks simultaneously.

```
from langchain_core.runnables import RunnableParallel

parallel_chain= RunnableParallel({
    'linkedin': linkedin_post_prompt | model | parser,
    'x': x_post_prompt | model | parser
})

```

## Runnable Passthrough:

Whatever is given to it as input, same is given as output of the chain.

```
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

joke_generator= template1 | model | parser

parallel_chain= RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': template2 | model | parser
})

final_chain= joke_generator | parallel_chain
```

## Runnable Lambda:

This is used to implement custom functions in LangChain.

```
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough

joke_generator= template1 | model | parser

def length_calculator(text):
    return len(text.split())

parallel_chain= RunnableParallel({
    'joke': RunnablePassthrough(),
    'length_count': RunnableLambda(length_calculator)
})

final_chain= joke_generator | parallel_chain
```

## Runnable Branch:

This is used to check for conditions. If one condition is True, then implement that branch, otherwise implement another branch.

**Syntax**:

(condition1, branch1),
(condition2, branch2),
(default branch)

```
from langchain_core.runnables import RunnableBranch

joke_chain= prompt1 | model | parser
explaination_chain= prompt2 | model | parser
fact_chain= prompt3 | model | parser

branch_chain= RunnableBranch(
    (lambda x: x['type']=='Joke', joke_chain),
    (lambda x: x['type']=='Explaination', explaination_chain),
    fact_chain
)
```