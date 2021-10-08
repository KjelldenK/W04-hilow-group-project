
import random
from Player import player

class dealer():
    def __init__(self):
        self.deck = []
        self.discard = []
        self.player = player()
        self.card1 = int
        self.card2 = int
        

    def game(self):
        while self.player.keep_playing == True:

            self.make_Deck()
            self.get_Card1()
            self.get_Input()
            self.get_Card2()
            self.get_Points()
            self.get_Output()

            
    def make_Deck(self):
        for i in range(1, 13):
            for n in range (0,4):
                self.deck.append(i)

    def get_Card1(self):
        self.card1 = random.choice(self.deck)
        print(f"\nThe card is {self.card1}")
        self.deck.remove(self.card1)
        self.discard.append(self.card1)

    def get_Card2(self):
        self.card2 = random.choice(self.deck)
        print(f"The card is {self.card2}")
        self.deck.remove(self.card2)
        self.discard.append(self.card2)

    def get_Input(self):
        self.player.high_low()

    def get_Points(self):
        if self.player.input == "h":
            if self.card1 <= self.card2:
                self.player.points += 100
            else:
                self.player.points += -70
        elif self.player.input == "l":
            if self.card1 >= self.card2:
                self.player.points += 100
            else:
                self.player.points += -300
        print(self.player.points)
            

    def get_Output(self):
        print(f"Your score is {self.player.points}")
        if len(self.deck) <= 0 or self.player.points <= 0:
            self.player.keep_playing = False
            
        elif self.player.play_more():
            self.player.keep_playing = True
        else:
            self.player.keep_playing = False



dealer = dealer()
dealer.game()