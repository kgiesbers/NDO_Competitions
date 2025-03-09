import os
import sys
import json

from scraper.competition_information import get_competition_information
from scraper.competition_listing import extract_number_and_name

print(json.dumps(get_competition_information(), indent=4, ensure_ascii=False))
# print(extract_number_and_name.__doc__)