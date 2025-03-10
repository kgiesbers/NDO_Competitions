from data_layer.models.Bracket import Bracket


def create_bracket(bracket_data, listing):
    brackets = []

    for bracket_name, data in bracket_data.items():
        bracket_object = Bracket(
            name=bracket_name,
            url=bracket_data["url"],
            listing=listing
        )
        brackets.append(bracket_object)

    return brackets
