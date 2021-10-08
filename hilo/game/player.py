

class player():
    def __init__(self):
        self.points = 300
        self.keep_playing = True
        self.input = str
        self.player_input = str

    def high_low(self):
        self.input = input("Higher or Lower? [h/l] ")
        return
    
    def play_more(self):
        self.player_input = input("Keepd playing? [y/n] ")
        return (self.player_input == "y")

    