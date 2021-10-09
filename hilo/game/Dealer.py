
import random
from game.Player import player
 
# The Dealer class takes care of things that the deal would handle in a real card game. 
# It will take care of keeping track of the deck and whats in the discord. 
# He will also handle grabing card 1 and card 2


class dealer():
    def __init__(self):
        self.deck = []
        self.discard = []
        self.player = player()
        self.card1 = int
        self.card2 = int
        
# basic game loop will tell the dealer to make the deck and then grab the cards and ask the player if it will be high or low then throw out the outputs.
    def game(self):
        self.make_Deck()
        while self.player.keep_playing == True:
            self.get_Card1()
            self.get_Input()
            self.get_Card2()
            self.get_Points()
            self.get_Output()

# This will make the deck
    def make_Deck(self):
        for i in range(1, 13):
            for n in range (0,4):
                self.deck.append(i)
# This will grab a card from the deck and till then place it in the discard.
    def get_Card1(self):
        self.card1 = random.choice(self.deck)
        print(f"\nThe card is {self.card1}")
        self.deck.remove(self.card1)
        self.discard.append(self.card1)
# grabs the card that will be compared to card 1
    def get_Card2(self):
        self.card2 = random.choice(self.deck)
        print(f"The card is {self.card2}")
        self.deck.remove(self.card2)
        self.discard.append(self.card2)
# calls player class to answer if the player thinks the next card will be high or low.
    def get_Input(self):
        self.player.high_low()
# adds or takes away points depending on the answer from the player.
    def get_Points(self):
        if self.player.input == "h":
            if self.card1 <= self.card2:
                self.player.points += 100
            else:
                self.player.points += -75
        elif self.player.input == "l":
            if self.card1 >= self.card2:
                self.player.points += 100
            else:
                self.player.points += -75
        print(self.player.points)
            
# displays the outputs such as points and if the player wants to keep playing.
    def get_Output(self):
        print(f"Your score is {self.player.points}")
        if len(self.deck) <= 0 or self.player.points <= 0:
            self.player.keep_playing = False
            
        elif self.player.play_more():
            self.player.keep_playing = True
        else:
            self.player.keep_playing = False



