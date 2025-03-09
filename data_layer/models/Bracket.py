import re

class Bracket:
    def __init__(self, name, url, listing):
        self.name = name
        self.url = url
        self.listing = listing

    def add_listing(self, listing):
        self.listing.append(listing)

    def get_listing(self, listing):
        return self.listing
