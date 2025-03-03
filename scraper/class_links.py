import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from scraper.competition_links import get_competition_links


def get_class_links(competition_url):
    page = requests.get(competition_url)
    soup = BeautifulSoup(page.content, "html.parser")
    class_links = {}

    for link in soup.find_all("a", href=True):
        full_url = urljoin(competition_url, link["href"])
        if full_url.startswith("http://www.TopTurnier.de"):
            continue
        class_name = link.text.strip()
        if class_name:
            class_links[class_name] = {}

    return class_links

def get_competition_classes():
    competitions_with_classes = {}
    competitions_links = get_competition_links()

    for competition_url in competitions_links:
        class_links = get_class_links(competition_url)
        competitions_with_classes[competition_url] = class_links

    return competitions_with_classes