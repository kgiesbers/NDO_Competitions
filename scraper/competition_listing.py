import requests
import re
from bs4 import BeautifulSoup


def get_bracket_listing(bracket_url):
    """Scrapes the place, number and names of all competitors of a given bracket_url"""

    new_url = bracket_url.replace("index.htm", "erg.htm")
    page = requests.get(new_url)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find("table", class_="tab1")
    if not table:
        return "table not found"

    listings = []

    for row in table.find_all("tr")[2:]:
        place = row.find("td", class_="td3c")
        number = row.find("td", class_="td2c")
        names = row.find("td", class_="td5")

        if place and number and names:
            place_text = place.get_text(strip=True).rstrip(".")
            if place_text.isdigit():
                result = {
                    "place": place_text,
                    "number": number.get_text(strip=True),
                    "couple": names.get_text(strip=True)
                }
            else:
                continue
            listings.append(result)
        else:
            cells = row.find_all("td")
            if len(cells) >= 2:
                place = cells[0].get_text(strip=True).rstrip(".")
                name_field = cells[1].get_text(strip=True)

                names, number = extract_number_and_name(name_field)
                if place.isdigit():
                    result = {
                        "place": place,
                        "number": number,
                        "couple": names
                    }
                else:
                    continue
                listings.append(result)
    return listings if listings else "no results found"


def extract_number_and_name(text):
    """splits number and name from 'John doe / Jane doe (123)' and returns both"""

    match = re.match(r"^(.*)\s+\((\d+)\)$", text)
    if match:
        names = match.group(1).strip()
        number = match.group(2)
    else:
        names = text
        number = ""
    return names, number
