import os
import sys
import json
from pathlib import Path

from scraper.competition_information import get_competition_information
from data_layer.utils.create_competition_data import create_competition_data
from data_access.database.fetch_db import *
from data_access.database.create_db import create_database_framework
from data_access.database.does_db_exist import does_db_exist

if not does_db_exist():
    create_database_framework()
