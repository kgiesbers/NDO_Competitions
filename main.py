from data_access.database.database_interactors.create_db import create_database_framework
from data_access.database.database_interactors.does_db_exist import does_db_exist
from data_access.database.database_interactors.fetch_db import fetch_all_data
from data_access.database.database_interactors.populate_db import populate_database
from data_layer.utils.create_competition_data import create_competition_data


if not does_db_exist():
    create_database_framework()

fetch_all_data()
