from crawl_scrape import crawl_and_scrape
from embeddings import chunk_and_embed
from vector_store import store_embeddings, query_vector_db
from llm_response import generate_response
import requests
from bs4 import BeautifulSoup
import openai

openai.api_key = open_api


def crawl_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    paragraphs = soup.find_all('p')
    content = ' '.join([para.get_text() for para in paragraphs])

    return content

# Function to generate response using OpenAI API
def generate_response(content, query):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Content: {content}\n\nQuestion: {query}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Main code execution (dynamic input for URL and question)
def main():
    # Ask for the URL to scrape content from
    url = input("Enter a URL to scrape content from (e.g., a Wikipedia page): ")

    # Crawl the content from the URL
    content = crawl_url(url)

    # Loop to ask questions repeatedly
    while True:
        # Ask for a relevant question about the content
        print("Ask a question related to the content you just scraped.")
        query = input("Ask a question: ")

        # If the user types 'exit', break out of the loop and stop the program
        if query.lower() == 'exit':
            print("Exiting the program.")
            break

        # Generate the response based on the scraped content and question
        response = generate_response(content, query)
        print(f"Response: {response}")

if __name__ == "__main__":
    main()
