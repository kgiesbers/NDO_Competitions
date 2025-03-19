from data_access.database.config import database_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def fetch_all_data():
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
