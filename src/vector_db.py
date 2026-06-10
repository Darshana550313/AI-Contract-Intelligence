from pinecone import Pinecone
from embeddings import generate_embedding

API_KEY = "your_api_key_here"

pc = Pinecone(api_key=API_KEY)

index = pc.Index("contract-index")

text = "This agreement may be terminated by either party."

embedding = generate_embedding(text)

index.upsert(
    vectors=[
        {
            "id": "contract1",
            "values": embedding,
            "metadata": {"text": text}
        }
    ]
)

print("Vector stored successfully!")