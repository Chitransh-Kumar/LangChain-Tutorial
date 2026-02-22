from langchain_community.document_loaders import CSVLoader

loader= CSVLoader('Social_Network_Ads.csv')

for doc in loader.lazy_load():
    print(doc.page_content)