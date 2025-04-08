from data_access.database.database_config import database_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_access.schemas.Listing import Listing
from data_access.schemas.Competition import Competition
from data_access.schemas.Bracket import Bracket


def competition_competitor(competitor):
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    competitions = (
        session.query(Competition.name, Competition.url, Bracket.name, Bracket.url, Listing)
        .join(Competition.brackets)
        .join(Bracket.listings)
        .filter(Listing.couple.contains(competitor))
        .distinct()
        .all()
    )

    return competitions
