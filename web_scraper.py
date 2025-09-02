import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Downloads and extracts all links from a given website.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]

        print(f"Successfully scraped {url}. Found {len(links)} links.")
        print("--- Extracted Links ---")
        for link in links:
            print(link)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred during scraping: {e}")

if __name__ == "__main__":
    target_url = "http://example.com"
    scrape_website(target_url)
