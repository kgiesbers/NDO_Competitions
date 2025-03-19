from data_layer.utils.create_competition import create_competition
from data_layer.utils.create_bracket import create_bracket
from data_layer.utils.create_listing import create_listing


def create_competition_data(scraped_data):
    competitions = []

    for competition_name, competition_data in scraped_data.items():

        brackets = []

        competition_name = competition_name
        competition_url = competition_data["url"]

        for bracket_name, bracket_data in competition_data["brackets"].items():

            listings = []

            bracket_name = bracket_name
            bracket_url = bracket_data["url"]

            listing_data = bracket_data.get("listing")

            if isinstance(listing_data, dict):
                for listing_place, listing_data in bracket_data.get("listing").items():

                    listing_object = create_listing(listing_place, listing_data["number"], listing_data["couple"])
                    listings.append(listing_object)
            else:
                continue

            bracket_object = create_bracket(bracket_name, bracket_url, listings)
            brackets.append(bracket_object)

        competition_object = create_competition(competition_name, competition_url, brackets)
        competitions.append(competition_object)

    return competitions
