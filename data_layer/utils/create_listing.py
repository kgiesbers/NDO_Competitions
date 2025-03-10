from data_layer.models.Listing import Listing


def create_listing(listing_data):
    listing = []

    for data in listing_data:
        listing_object = Listing(
            place=listing_data["place"],
            number=listing_data["number"],
            couple=listing_data["couple"]
        )
        listing.append(listing_object)

    return listing
