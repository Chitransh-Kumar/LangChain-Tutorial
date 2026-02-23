from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader= PyPDFLoader('document.pdf')

docs= loader.load()

splitter= CharacterTextSplitter(
    chunk_size= 500,
    chunk_overlap= 0,
    separator= ''
)

result= splitter.split_documents(docs)

print("Total chunks: ", len(result))

print("Example: ", result[8].page_content)