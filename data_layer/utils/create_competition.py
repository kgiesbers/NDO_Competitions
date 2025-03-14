from data_layer.models.Competition import Competition


def create_competition(name, url, brackets):

    competition_object = Competition(
        name=name,
        url=url,
        brackets=brackets
    )
    return competition_object
