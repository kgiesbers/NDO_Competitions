from backend.data_access.database.database_config import database_url
from backend.data_access.schemas.Competition import Competition
from backend.data_access.schemas.Bracket import Bracket
from backend.data_access.schemas.Listing import Listing
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def populate_database(data):
    """Populates the database with provided data from scraper"""
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    for competition_name, competition_data in reversed(data.items()):

        # Check if competition exists, otherwise create it
        competition = session.query(Competition).filter_by(
            name=competition_name
        ).first()

        if not competition:
            competition = Competition(
                name=competition_name,
                url=competition_data["url"]
            )
        session.add(competition)

        for bracket_name, bracket_data in competition_data["brackets"].items():

            # Check if listing is valid BEFORE adding bracket
            if isinstance(bracket_data["listing"], dict):

                # Check if bracket exists, otherwise create it
                bracket = session.query(Bracket).filter_by(
                    name=bracket_name,
                    competition_id=competition.id
                ).first()

                if not bracket:
                    bracket = Bracket(
                        name=bracket_name,
                        url=bracket_data["url"],
                        competition_id=competition.id
                    )
                session.add(bracket)

            # If listing is not valid, continue to next
            else:
                continue

            for listing_place, listing_data in bracket_data["listing"].items():

                # Check if listing exists, otherwise create it
                listing = session.query(Listing).filter_by(
                    place=listing_place,
                    number=listing_data["number"],
                    couple=listing_data["couple"],
                    bracket_id=bracket.id
                ).first()

                if not listing:
                    listing = Listing(
                        place=listing_place,
                        number=listing_data["number"],
                        couple=listing_data["couple"],
                        bracket_id=bracket.id
                    )
                session.add(listing)
                session.flush()

    session.commit()
    session.close()
