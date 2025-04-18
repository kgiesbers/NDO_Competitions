from data_access.database.database_config import database_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_access.schemas.Competition import Competition
# These are actually used
from data_access.schemas.Bracket import Bracket
from data_access.schemas.Listing import Listing
# These are actually used


def fetch_all_data():
    """Queries all data from the database"""
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    competitions = session.query(Competition).all()
    print("\n=== Competitions ===")
    for comp in competitions:
        print(f"ID: {comp.id}, Name: {comp.name}, URL: {comp.url}")

        for bracket in comp.brackets:
            print(f"  ├── Bracket: {bracket.name}, URL: {bracket.url}")

            for listing in bracket.listings:
                print(f"      ├── Place: {listing.place}, Number: {listing.number}, Names: {listing.couple}")

    session.close()
