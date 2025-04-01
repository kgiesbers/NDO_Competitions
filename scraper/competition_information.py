from scraper.competition_links import get_competition_links
from scraper.bracket_links import get_bracket_links
from scraper.bracket_listing import get_bracket_listing


def get_competition_information():
    """Returns a structured dictionary of all scraped data"""

    competitions_with_brackets = {}
    competitions_links = get_competition_links()

    for competition_name, competition_url in competitions_links.items():
        bracket_links = get_bracket_links(competition_url)

        competitions_with_brackets[competition_name] = {
            "url": competition_url,
            "brackets": {}
        }

        for bracket_name, bracket_url in bracket_links.items():
            bracket_listing = get_bracket_listing(bracket_url)

            competitions_with_brackets[competition_name]["brackets"][bracket_name] = {
                "url": bracket_url,
                "listing": bracket_listing
            }
    return competitions_with_brackets


