from scraper.competition_links import get_competition_links
from scraper.class_links import get_class_links
from scraper.competition_listing import get_competition_listing

def get_competition_information():
    competitions_with_classes = {}
    competitions_links = get_competition_links()

    for competition_url in competitions_links:

        class_links = get_class_links(competition_url)

        competitions_with_classes[competition_url] = {}

        for class_url in class_links:
            class_listing = get_competition_listing(class_url)

            competitions_with_classes[competition_url][class_url] = class_listing

    return competitions_with_classes

    # for i, competition_url in enumerate(competitions_links):
    #     if i >= 1:
    #         break
    #
    #     class_links = get_class_links(competition_url)
    #
    #     competitions_with_classes[competition_url] = {}
    #
    #     for class_url in class_links:
    #         class_listing = get_competition_listing(class_url)
    #
    #         competitions_with_classes[competition_url][class_url] = class_listing
    #
    # return competitions_with_classes
