import requests
from bs4 import BeautifulSoup

def get_class_links(competition_url):
    page = requests.get(competition_url)
    soup = BeautifulSoup(page.content, "html.parser")
    class_links = {}

    for link in soup.find_all("a", href=True):
        if link["href"].startswith("http://www.TopTurnier.de"):
            continue
        full_url = competition_url + link["href"]
        class_links[full_url] = {}

    return class_links


