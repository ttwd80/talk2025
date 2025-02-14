import requests
from bs4 import BeautifulSoup

def get_hyperlinks(url="http://example.com"):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = [a["href"] for a in soup.find_all("a", href=True)]
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []