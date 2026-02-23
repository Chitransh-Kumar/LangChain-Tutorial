# Text Splitter:

Text splitting is the process of breaking large pieces of text into smaller pieces that the LLM can handle effeciently.

**Why is Text Splitting important?**:

1. Overcoming maximum input size constraints.

2. Improves almost every LLM task.

3. Optimizing computational resources.

---

**Types of Text Splitters**:

1. Length based.

2. Text Structure based.

3. Document Structure based.

4. Semantic meaning based.

---

## Length based Text-Splitter:

This splitting is based on the count of characters in the document. If the count of character reaches the mentioned value (here 500), then split is done.

```
from langchain_text_splitters import CharacterTextSplitter

splitter= CharacterTextSplitter(
    chunk_size= 500,
    chunk_overlap= 0,
    separator= ''
)
```

## Text Structure based Text-Splitter:

This splitting is based on the structure of the sentence. The sentence hierarchy is as follows:

- Paragraph

- Sentences

- Words

- Letters (individual characters).

Thus, splitting is also on the basis of this hierarchy only. First th text is split on the basis of `Paragraph` and if the count of characters in each `Paragraph` is greater than the mentioned number in splitter() function, then splitting is again done on the basis of `Sentences`, and so on.

```
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter= RecursiveCharacterTextSplitter(
    chunk_size= 500,
    chunk_overlap= 0
)
```

## Document Structure based Text-Splitter:

This is a special kind of text splitting which uses same technique as Text Structure based `RecursiveCharacterTextSplitter` but here it is for codes and markup languages.

```
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter= RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,
    chunk_size= 200,
    chunk_overlap= 0
)

chunks= splitter.split_text(text)
```
