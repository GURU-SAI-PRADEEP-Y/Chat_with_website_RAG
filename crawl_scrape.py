import requests
from bs4 import BeautifulSoup

def crawl_and_scrape(url_list, output_file):
    """Crawls websites and extracts textual content."""
    all_text = ""
    for url in url_list:
        print(f"Crawling: {url}")
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract text from <p> and <h> tags
            paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            page_text = "\n".join([para.get_text() for para in paragraphs])
            
            all_text += f"\n\nURL: {url}\n{page_text}"
        except Exception as e:
            print(f"Failed to crawl {url}: {e}")
    
    # Save content to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(all_text)
    print(f"Content saved to {output_file}")

# Example usage
if __name__ == "__main__":
    urls = ["https://example.com", "https://www.wikipedia.org/"]
    crawl_and_scrape(urls, "data/scraped_content.txt")