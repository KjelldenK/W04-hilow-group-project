from player import Player

def make_Deck():
    deck = []
    for i in range(1,13):
        for n in range(1,5):
            deck.append(int(i))
    return deck

deck = make_Deck()
print(deck)    

deck.remove(12)
print(deck)



class Dealer():
    def __init__(self):
        self.deck = make_Deck()
        self.points = 300
        self.player = Player()

    def start_game(self):
        self.get_Input()

    def get_Input(self):
        if self.player.guesses == 0:
            print('yes')


Dealer = Dealer()
Dealer.start_game()