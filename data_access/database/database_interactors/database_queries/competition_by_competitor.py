from data_access.database.database_config import database_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_access.schemas.Listing import Listing
from data_access.schemas.Competition import Competition
from data_access.schemas.Bracket import Bracket


def competition_by_competitor(competitor):
    """Queries the database bases on provided name"""
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    competitions = (
        session.query(Competition, Bracket, Listing)
        .join(Competition.brackets)
        .join(Bracket.listings)
        .filter(Listing.couple.contains(competitor))
        .distinct()
        .all()
    )

    competitions_dict = []
    for competition, bracket, listing in competitions:
        competitions_dict.append({
            "competition": competition.to_dict(),
            "bracket": bracket.to_dict(),
            "listing": listing.to_dict()
        })

    return competitions_dict
