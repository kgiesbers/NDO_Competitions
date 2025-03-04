import os
import sys
import json

from scraper.competition_links import get_competition_links
from scraper.class_links import get_class_links
from scraper.competition_listing import get_competition_listing
from scraper.competition_information import get_competition_information

print(json.dumps(get_competition_information(), indent=4, ensure_ascii=False))