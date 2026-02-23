from langchain_text_splitters import RecursiveCharacterTextSplitter

text= """
"Attention Is All You Need" is a 2017 research paper in machine learning authored by eight scientists working at Google. The paper introduced a new deep learning architecture known as the transformer, based on the attention mechanism proposed in 2014 by Bahdanau et al. The transformer approach it describes has become the main architecture of a wide variety of AI, such as large language models. At the time, the focus of the research was on improving Seq2seq techniques for machine translation, but the authors go further in the paper, foreseeing the technique's potential for other tasks like question answering and what is now known as multimodal generative AI.

Some early examples that the team tried their Transformer architecture on included English-to-German translation, generating Wikipedia articles on "The Transformer", and parsing. These convinced the team that the Transformer is a general-purpose language model, and not just good for translation.

As of 2025, the paper has been cited more than 173,000 times, placing it among the top ten most-cited papers of the 21st century. After the paper was published by Google, each of the authors left the company to join other companies or to found startups.
"""

splitter= RecursiveCharacterTextSplitter(
    chunk_size= 500,
    chunk_overlap= 0
)

result= splitter.split_text(text)

print("Total chunks: ", len(result))

print("Example: ", result[2])