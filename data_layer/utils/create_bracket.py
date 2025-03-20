from data_layer.dto.Bracket import Bracket


def create_bracket(name, url, listing):

    bracket_object = Bracket(
        name=name,
        url=url,
        listing=listing
    )
    return bracket_object
