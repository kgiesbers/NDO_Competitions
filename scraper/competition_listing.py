import requests
import re
from bs4 import BeautifulSoup


def get_competition_listing(class_url):
    new_url = class_url.replace("index.htm", "erg.htm")
    page = requests.get(new_url)
    soup = BeautifulSoup(page.content, "html.parser")
    ranking_div = soup.find("div", id="t3")
    table = soup.find("table", class_="tab1")
    if not table:
        return "table not found"

    listings = []

    for row in table.find_all("tr")[2:]:
        place = row.find("td", class_="td3c")
        number = row.find("td", class_="td2c")
        names = row.find("td", class_="td5")

        if place and number and names:
            result = {
                "place": place.get_text(strip=True),
                "number": number.get_text(strip=True),
                "names": names.get_text(strip=True)
            }
            listings.append(result)
        else:
            cells = row.find_all("td")
            if len(cells) >= 2:
                place = cells[0].get_text(strip=True)
                name_field = cells[1].get_text(strip=True)

                names, number = extract_number_and_name(name_field)

                result = {
                    "place": place,
                    "number": number,
                    "names": names
                }
                listings.append(result)
    return listings if listings else "no results found"

def extract_number_and_name(text):
    match = re.match(r"^(.*)\s+\((\d+)\)$", text)
    if match:
        names = match.group(1).strip()
        number = match.group(2)
    else:
        names = text
        number = ""
    return names, number
