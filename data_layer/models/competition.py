class Competition:
    def __init__(self, name, url, brackets):
        self.name = name
        self.url = url
        self.brackets = brackets

    def add_bracket(self, bracket):
        self.brackets[bracket.bracket_id] = bracket

    def get_bracket(self, bracket_id):
        return self.brackets.get(bracket_id, None)

