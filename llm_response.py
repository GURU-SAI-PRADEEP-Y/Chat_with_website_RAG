import openai
from itertools import chain

def generate_response(context_chunks, query):
    """
    Generate a response using the LLM (e.g., gpt-4o-mini).
    :param context_chunks: Retrieved relevant context chunks.
    :param query: User's query.
    :return: Response string.
    """
    
    
    # Flatten the list of chunks
    flat_chunks = list(chain(*context_chunks))  # Flatten nested lists
    
    # Join the flattened chunks
    context = "\n".join(flat_chunks)
    
    # Construct the prompt
    prompt = f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"
    
    # Call OpenAI's ChatCompletion API (updated method)
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on context."},
            {"role": "user", "content": prompt}
        ],
        # max_tokens=300,
        # temperature=0.7
    )
    
    # Extract and return the response
    return response["choices"][0]["message"]["content"].strip()
