import os
import sys
import json

from data_layer.models.Bracket import Bracket
from scraper.competition_information import get_competition_information
from scraper.competition_listing import extract_number_and_name

print(json.dumps(get_competition_information(), indent=4, ensure_ascii=False))
# print(extract_number_and_name.__doc__)

# listing = {
#                         "place": "1",
#                         "number": "22",
#                         "names": "Marcel Landman  /  Linda Landman"
#                     }



# b1 = Bracket("Senioren 35+ Ballroom", "https://scrutineering.org/NDO/20250209/2-senioren35pballroom/index.htm", listing)
# print(b1.name, b1.url, b1,listing)