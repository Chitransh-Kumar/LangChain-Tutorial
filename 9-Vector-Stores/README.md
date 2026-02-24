# Vector Stores:

It is a system designed to store and retrieve data represented as numerical vectors.

**Key Features**

1. Vectors and its associated metadata is retained either in-memory or on-disk.

2. Similarity search.

3. It provides a method for fast similarity search on high-dimensional vectors.

4. CRUD applications.

---

## Vector Stores vs Vector Databases:

- Vector Store:

    - It focuses on storing vectors and performing similarity search.

    - It may not include traditional database features like distributed architecture, backup and restore, ACID transactions and concurrency control.

- Vector Databases:

    - Vector store with database-like features (like distributed architecture, backup and restore, ACID transactions, authentication (security) and concurrency control) can be called as Vector Databases.

    - It is used in production environment with significant scaling.


## Chroma DB:

Hierarchy:

- Tenant (User).

- Databases (Multiple).

- Collections (Multiple): Similar to Tables in RDBMS.

- Docs (Multiple).

```
from langchain_chroma import Chroma

vector_store= Chroma(
    embedding_function= OpenAIEmbeddings(),
    persist_directory= 'chroma_db',
    collection_name= 'sample'
)
```

- Adding documents to vector store

```
vector_store.add_documents(docs)
```

- Viewing the stored documents

```
vector_store.get(include= ['embeddings', 'documents', 'metadatas'])
```

- Document search

```
result= vector_store.similarity_search(
    query= 'Who among these is a bowler',
    k= 2
)
```

Here, k means k no. of documents will be returned.

- Document search with similarity score

```
result_with_score= vector_store.similarity_search_with_score(
    query= 'Who among these is a bowler?',
    k= 2
)
```

- Meta-data filtering

```
result_with_metadata= vector_store.similarity_search_with_score(
    query= '',
    filter= {'team': 'Chennai Super Kings'}
)
```