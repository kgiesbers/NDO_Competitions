from data_access.database.database_interactors.database_helpers.populate_db import populate_database
from scraper.competition_information import get_competition_information
from data_access.database.database_interactors.database_helpers.fetch_db import fetch_all_data
from data_access.database.database_interactors.database_helpers.create_db import create_database_framework


# create_database_framework()
# # competition_data = get_competition_information()
# populate_database(competition_data)
fetch_all_data()