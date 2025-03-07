import requests
from bs4 import BeautifulSoup

def get_bracket_links(competition_url):
    """scrapes all urls from brackets given a competition url"""

    url_page = requests.get(competition_url)
    url_soup = BeautifulSoup(url_page.content, "html.parser")
    bracket_links = {}


    for url in url_soup.find_all("a", href=True):

        if url["href"].startswith("http://www.TopTurnier.de"):
            continue

        bracket_url = competition_url + url["href"]
        name_url = bracket_url.replace("index.htm", "menu.htm")
        name_page = requests.get(name_url)
        name_soup = BeautifulSoup(name_page.content, "html.parser")

        # filter out edge case where scrape_data is inconsistent
        if bracket_url == competition_url + "index.htm":
            continue

        div = name_soup.find("div", class_="eventhead")
        if div:
            td = div.find("td")
            if td:
                bracket_name = td.get_text(strip=True)
                bracket_name = bracket_name.split(" - ")[0]
        else:
            name_page = requests.get(bracket_url)
            name_soup = BeautifulSoup(name_page.content, "html.parser")
            bracket_name = name_soup.title.get_text(strip=True)
            bracket_name = str(bracket_name).strip()

        bracket_links[bracket_name] = bracket_url

    return bracket_links


