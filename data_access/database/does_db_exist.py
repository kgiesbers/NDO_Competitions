from pathlib import Path


def does_db_exist():
    db_file = Path("data_access/database/ndocompetitions.db")
    return db_file.exists()
