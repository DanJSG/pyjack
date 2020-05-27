class Card:
    def __init__(self, raw_value):
        if raw_value > 51:
            raise Exception("Raw value cannot be greater than 51")
        self.raw_value = raw_value
        self.number = (raw_value % 13) + 1
        self.suit = self._determine_suit()
        self.value = self._determine_value()
        self.type = self._determine_type()

    def _determine_type(self):
        if self.number == 1:
            return "ace"
        elif self.number == 11:
            return "jack"
        elif self.number == 12:
            return "queen"
        elif self.number == 13:
            return "king"
        else:
            return None

    def _determine_value(self):
        if self.number > 10:
            return 10
        else:
            return self.number

    def _determine_suit(self):
        if self.raw_value < 13:
            return "clubs"
        elif self.raw_value < 26:
            return "diamonds"
        elif self.raw_value < 39:
            return "hearts"
        else:
            return "spades"
    