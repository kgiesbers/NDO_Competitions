import re


class Competition:
    def __init__(self, name, url, brackets):
        self.name = name
        self.url = url
        self.brackets = brackets
        self.validate()

    def add_bracket(self, bracket):
        self.brackets[bracket.bracket_id] = bracket

    def get_bracket(self, bracket_id):
        return self.brackets.get(bracket_id, None)

    def validate(self):
        """Validates fields of object. name should be string, url should be valid and listing should be valid"""
        # Validate competition_name: should be a non-empty string
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Invalid competition_name: must be a non-empty string.")

        # Validate bracket_url: should be a valid URL (basic regex check)
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        if not isinstance(self.url, str) or not re.match(url_pattern, self.url):
            raise ValueError(f"Invalid bracket_url: {self.url} is not a valid URL.")

        for bracket in self.brackets:
            if not isinstance(bracket, dict):
                raise ValueError("Each bracket must be a dictionary.")

        return True  # If all checks pass
