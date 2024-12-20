import chromadb

def store_embeddings(chunks, embeddings):
    """Stores embeddings in a vector database."""
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="rag_content")

    # Add chunks and embeddings to the collection
    collection.add(
        embeddings=embeddings.tolist(),
        documents=chunks,
        ids=[str(i) for i in range(len(chunks))]
    )
    print("Embeddings stored in ChromaDB.")

def query_vector_db(query_text, model_name="all-MiniLM-L6-v2"):
    """Queries the vector database for relevant chunks."""
    from sentence_transformers import SentenceTransformer

    # Load embedding model
    model = SentenceTransformer(model_name)
    query_embedding = model.encode([query_text])

    # Query ChromaDB
    client = chromadb.Client()
    collection = client.get_collection(name="rag_content")
    results = collection.query(query_embeddings=query_embedding.tolist(), n_results=5)

    return results["documents"]

# Example usage
if __name__ == "__main__":
    chunks, embeddings = chunk_and_embed("data/scraped_content.txt")
    store_embeddings(chunks, embeddings)
    
    query = "What is this website about?"
    relevant_docs = query_vector_db(query)
    print("Relevant Chunks:", relevant_docs)
