import random as rd
class Player:
    def __init__(self):
        self.guesses = rd.randint(1, 13)
        self.card_of_player = 0
        self.score = 0
    
    def choosing_h_l(self, h_l):
        if self.guesses < self.card_of_player and h_l == "l":
            self.score += 100
        elif self.guesses > self.card_of_player and h_l == "h":
            self.score += 100
        elif self.guesses > self.card_of_player and h_l == "l":
            self.score-= 75
        elif self.guesses < self.card_of_player and h_l == "h":
            self.score-= 75
        else:
            self.score = 0            
        return self.score    





Player()