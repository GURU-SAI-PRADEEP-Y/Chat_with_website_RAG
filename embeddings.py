from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

def chunk_and_embed(input_file, model_name="all-MiniLM-L6-v2"):
    """Reads content, splits into chunks, and generates embeddings."""
    # Load the embedding model
    model = SentenceTransformer(model_name) 

    # Read content
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Split content into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(content)
    print(f"Split into {len(chunks)} chunks.")

    # Generate embeddings
    embeddings = model.encode(chunks)
    return chunks, embeddings

# Example usage
if __name__ == "__main__":
    chunks, embeddings = chunk_and_embed("data/scraped_content.txt")
    print("Generated embeddings for chunks.")
