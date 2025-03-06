import requests
from bs4 import BeautifulSoup
from config import base_url


def get_competition_links():
    comp_page = requests.get(base_url)
    comp_soup = BeautifulSoup(comp_page.content, "html.parser")
    competitions = {}

    for url in comp_soup.find_all("a", href=True):

        full_url = base_url + url["href"] + "/"

        # get name from bracket page
        name_page = requests.get(full_url)
        name_soup = BeautifulSoup(name_page.content, "html.parser")

        div = name_soup.find("div", class_="eventhead")
        if div:
            td = div.find("td")
            if td:
                name = td.get_text(strip=True)
        else:
            name = name_soup.find("p", class_="t1").get_text()
            name = str(name).strip()

        name = name + " " + url["href"]

        competitions[name] = full_url

    return competitions
