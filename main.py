import os
import sys
import json

import data_access.database.scraped_file
from data_layer.models.Bracket import Bracket
from scraper.competition_information import get_competition_information
from scraper.competition_listing import extract_number_and_name
from data_access.database.scraped_file import data
from data_layer.utils.create_competition_list import create_competition_data

scraped_data = data
# print(json.dumps(scraped_data, indent=4))
competition_object_list = create_competition_data(scraped_data)

for competition in competition_object_list:
    print(competition)
