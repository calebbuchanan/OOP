import random


class Insect:
    def __init__(self):
        self.wings = "2"
        self.legs = "4"
        self.flightlength = "0"

    def flight(self):
        random.randint(1, 10)
        return self.flightlength

    def get_flight(self):
        return self.wings
        return self.legs
