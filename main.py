import os
import sys
import json

from scraper.competition_information import get_competition_information


print(json.dumps(get_competition_information(), indent=4, ensure_ascii=False))
