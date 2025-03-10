from data_layer.models.Competition import Competition


def create_competition(competition_data, brackets):
    competitions = ()

    for competition_name, data in competition_data.items():
        competition_object = Competition(
            name=competition_name,
            url=competition_data["url"],
            brackets=brackets
        )
        competitions.append(competition_object)

    return competitions
