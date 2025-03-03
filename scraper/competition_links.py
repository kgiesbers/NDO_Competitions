import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import BASE_URL


def get_competition_links():
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, "html.parser")
    competition_links = []

    for link in soup.find_all("a", href=True):
        full_url = urljoin(BASE_URL, link["href"])
        competition_links.append(full_url)

    return competition_links
