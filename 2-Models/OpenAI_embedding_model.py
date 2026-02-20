from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings= OpenAIEmbeddings(
    model= 'text-embedding-3-small',
    dimensions= 32
)

vector= embeddings.embed_query("Max Verstappen is the best F1 driver")

print(vector)