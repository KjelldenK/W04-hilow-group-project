
# the player keeps track of the answers they give to the dealer and there points.


class player():
    def __init__(self):
        self.points = 300
        self.keep_playing = True
        self.input = str
        self.player_input = str
# the player answers if the card is higher or lower.
    def high_low(self):
        self.input = input("Higher or Lower? [h/l] ")
        return
    # the palyer answers if they want to keep playing
    def play_more(self):
        self.player_input = input("Keepd playing? [y/n] ")
        return (self.player_input == "y")

    