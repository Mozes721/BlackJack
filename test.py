import random
import os 
from constants import *

class Card:
    def __init__(self, suit, value):
        if (suit in SUITS) and (value in RANKS):
            self.suit = suit
            self.value = value 
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, value)

    def __str__(self):
        return self.suit + self.value

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.value

    def __repr__(self):
        return " of ".join((self.value, self.value))

class Deck:
    def __init__(self):
        self.cards = [Card(s,v) for s in SUITS for v in RANKS]

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0 
    
    def add_card(self, card):
        self.cards.append(card)

    def calc_hand(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10 
    

    def get_value(self):
        self.calc_hand()
        return self.value 

    def display(self):
        if self.dealer:
            print(self.cards[0])
            print("?")
        else:
            for card in self.cards:
                print(card)

class Game:
    
    def __init__(self):
        pass
    
    def play(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("Your hand is:")
            self.player_hand(self.deck.draw())
            print()
            print("Dealer's hand is:")
            self.dealer_hand.display()

            game_over = True

            while game_over:
                player_with_blackjack, dealer_with_blackjack = self.check_if_blackjack()
                if player_with_blackjack or dealer_with_blackjack:
                    game_over = False
                    self.show_blackjack_results(
                        player_with_blackjack, dealer_with_blackjack)
                    continue

                if self.dealer_is_over():
                    print("Dealer busted you won!")
                    game_over = False

                hit_stand = input(
                    "What would you like to do:\n [1] Hit or [2] Stand?")
                if hit_stand == '1':
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You have busted dealer won")
                        game_over = False

                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    print("Final Results:")
                    print("Your hand:", player_hand_value)
                    print("Dealer's hand:", dealer_hand_value)

                    if player_hand_value > dealer_hand_value:
                        print("You Win!")
                    elif player_hand_value == dealer_hand_value:
                        print("Tie")
                    else:
                        print("Dealer Wins!")
                    game_over = False

            again = input("Play again? [Y/N]")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == 'n':
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False

    def player_is_over(self):
        return self.player_hand.get_value() > 21

    def dealer_is_over(self):
        return self.dealer_hand.get_value() > 21

    def check_if_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_with_blackjack, dealer_with_blackjack):
        if player_with_blackjack and dealer_with_blackjack:
            print("Both players have blackjack! Draw!")
        elif player_with_blackjack:
            print("You have blackjack! You win!")
        elif dealer_with_blackjack:
            print("Dealer has blackjack! Dealer wins!")
