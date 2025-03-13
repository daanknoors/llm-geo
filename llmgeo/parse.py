import requests
from bs4 import BeautifulSoup

def fetch_website(url, max_redirects=None):
    session = requests.Session()

    # increase the redirect count to avoid limit 
    if max_redirects:
        session.max_redirects = max_redirects
    response = session.get(url)

    response.raise_for_status()
    return response

def parse_html(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
