from data_access.database.config import *


def populate_database(data):

    for competition_data in data:

        # Check if competition exists, otherwise create it
        competition = session.query(Competition).filter_by(
            name=competition_data.name
        ).first()

        if not competition:
            competition = Competition(
                name=competition_data.name,
                url=competition_data.url
            )
            session.add(competition)
            session.flush()

        for bracket_data in competition_data.brackets:

            # Check if bracket exists, otherwise create it
            bracket = session.query(Bracket).filter_by(
                name=bracket_data.name,
                competition_id=competition.id
            ).first()

            if not bracket:
                bracket = Bracket(
                    name=bracket_data.name,
                    url=bracket_data.url,
                    competition_id=competition.id
                )
                session.add(bracket)
                session.flush()

            for listing_data in bracket_data.listing:

                # Check if listing exists, otherwise create it
                listing = session.query(Listing).filter_by(
                    place=listing_data.place,
                    number=listing_data.number,
                    couple=listing_data.couple,
                    bracket_id=bracket.id
                ).first()

                if not listing:
                    listing = Listing(
                        place=listing_data.place,
                        number=listing_data.number,
                        couple=listing_data.couple,
                        bracket_id=bracket.id
                    )
                    session.add(listing)
                    session.flush()

    session.commit()