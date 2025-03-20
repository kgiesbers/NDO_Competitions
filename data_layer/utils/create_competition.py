from data_layer.dto.Competition import Competition


def create_competition(name, url, brackets):

    competition_object = Competition(
        name=name,
        url=url,
        brackets=brackets
    )
    return competition_object
