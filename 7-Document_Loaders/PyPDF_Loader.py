from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader('document.pdf')

docs= loader.load()

print("Total no. of pages: ", len(docs))

print("First page: ", docs[0].page_content)