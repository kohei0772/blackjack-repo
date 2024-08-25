import random


class Player:

    first_player_cards = []
    total = 0
    for i in range(2):
        first_player_cards.append(random.randint(1, 13))

    def __init__(self, tip, hands=first_player_cards):
        self.tip = tip
        self.hands = hands

    def __repr__(self):
        print(f"You have the following cards now: {self.hands}")
        print(f"Your current total tip is ${self.tip}.")

    def player_hit(self):
        self.hands.append(random.randint(1, 13))

    def player_stay(self):
        return self.hands


# Ready for the Game (Set up the initial tip amount, odds)
casino_player = Player(2000)
dealer_odds = 2

# Game Start (Dealer VS Player)
tip_amount = input("Welcome to Black Jack! How much would you like to bet?: $")
if tip_amount > casino_player.tip():
    print("The amount you bet is more than what you have!")
else:
    print(f"You bet ${tip_amount} for this game")
# Dealer's Hand
dealer_hands = []
for d in range(2):
    dealer_hands.append(random.randint(1, 13))
print("Dealer's hand: " + str(dealer_hands[0]) + ", ??")