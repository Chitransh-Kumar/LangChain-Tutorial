# Document Loaders:

These are component in LangChain used to load data from various sources into a standardized format (Document object), which can be used for chunking, embedding, retrieval and generation.

There are various document loaders in LangChain. Some of the most important ones are:

- TextLoader

- PyPDFLoader

- WebBaseLoader

- CSVLoader

---

There are two components in `Document` object in LangChain. These are:

- `page_content`

- `metadata`

---

## TextLoader:

It reads plain text files (.txt) and converts them into LangChain document objects.

```
from langchain_community.document_loaders import TextLoader

loader= TextLoader('cricket.txt', encoding= 'utf-8')
docs= loader.load()

print("Content: ", docs[0].page_content)
print("Metadata: ", docs[0].metadata)
```

## PyPDFLoader:

It is a document loader in LangChain used to load content from PDF files and converts each page into document object. If a PDF file has 20 pages, then PyPDF loader makes 20 `Document` objects for each page.


```
from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader('document.pdf')

docs= loader.load()
```

There are two ways in which documents are loaded in the RAM. 

- `load()`: It loads all the documents (pages) at once. It is recommended when the no. of pages in the document is small. It returns `Document` object.

- `lazy_load()`: It loads documents (pages) on demand. It is recommended when the no. of pages in the document is very large. It returns `generator` of `Document` object.


## WebBaseLoader:

It is a document loader in LangChain used to extract and load content from web pages (URLs). It uses BeautifulSoup to extract content.

```
from langchain_community.document_loaders import WebBaseLoader

url= 'https://en.wikipedia.org/wiki/Attention_Is_All_You_Need#:~:text=%22Attention%20Is%20All%20You%20Need,eight%20scientists%20working%20at%20Google.'

loader= WebBaseLoader(url)

docs= loader.load()
```

## CSVLoader:

It is a document loader in LangChain used to load CSV files into LangChain document objects - one per row (default).

```
from langchain_community.document_loaders import CSVLoader

loader= CSVLoader('Social_Network_Ads.csv')

for doc in loader.lazy_load():
    print(doc.page_content)
```