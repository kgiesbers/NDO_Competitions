from data_layer.dto.Listing import Listing


def create_listing(place, number, couple):
    listing_object = Listing(
        place=place,
        number=number,
        couple=couple
    )
    return listing_object
