import re


class Bracket:
    def __init__(self, name, url, listing):
        self.name = name
        self.url = url
        self.listing = listing
        self.validate()

    def add_listing(self, listing):
        self.listing.append(listing)

    def get_listing(self, listing):
        return self.listing

    def validate(self):
        """Validates fields of object. name should be string, url should be valid and listing should be valid"""
        # Validate bracket_name: should be a non-empty string
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Invalid bracket_name: must be a non-empty string.")

        # Validate bracket_url: should be a valid URL (basic regex check)
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        if not isinstance(self.url, str) or not re.match(url_pattern, self.url):
            raise ValueError(f"Invalid bracket_url: {self.url} is not a valid URL.")

        # Validate bracket_listing: should be a list of dictionaries with specific keys
        if not isinstance(self.listing, dict):
            raise ValueError("Invalid bracket_listing: must be a list of listings.")

        return True  # If all checks pass
