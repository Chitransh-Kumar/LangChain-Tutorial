from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader('document.pdf')

for doc in loader.lazy_load():
    print(doc.page_content)