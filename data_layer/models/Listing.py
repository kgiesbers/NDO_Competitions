class Listing:
    def __init__(self, place, number, couple):
        self.place = place
        self.number = number
        self.couple = couple
        self.validate()

    def validate(self):
        if not isinstance(self.place, (int, str)) or not str(self.place).isdigit():
            raise ValueError("place must be a non-empty numeric value.")
        if not isinstance(self.number, (int, str)) or not str(self.number).isdigit():
            raise ValueError("number must be a non-empty numeric value.")
        if not isinstance(self.couple, str) or not self.couple.strip():
            raise ValueError("couple must be a non-empty string.")