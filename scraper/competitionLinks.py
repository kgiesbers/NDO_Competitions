import requests
from bs4 import BeautifulSoup


def getCompetitionLinks():
    mainURL = "https://scrutineering.org/NDO/"
    page = requests.get(mainURL)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.findAll("a")
    competitionlinks = []
    for i in result:
        URL = mainURL
        URL = URL + i.get("href")
        competitionlinks.append(URL)
    return competitionlinks
