from pinecone import Pinecone
from embeddings import generate_embedding

API_KEY = "your_api_key_here"

pc = Pinecone(api_key=API_KEY)

index = pc.Index("contract-index")

query = "termination clause"

query_embedding = generate_embedding(query)

result = index.query(
    vector=query_embedding,
    top_k=1,
    include_metadata=True
)

print(result)