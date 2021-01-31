import random
import os 



class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.vaule = value 

class Deck:
    def __init__(self):
        self.cards = [Card(s,v) for s in ['\u2660', '\u2661', '\u2662', '\u2663'] for v in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.sum = 0 
    
    def add_card(self, card):
        self.cards.append(card)

    def calc_hand(self):
        self.sum = 0

        self.non_aces = [c for c in self.cards if c != 'A']
        self.aces = [c for c in self.cards if c == 'A']

        for card in self.non_aces:
            if card in 'JQK':
                self.sum += 10
            else:
                self.sum += int(card)

        for card in self.aces:
            if self.sum <= 10:
                self.sum += 11 
            else:
                self.sum += 1 
    

    def get_value(self):
        self.calc_hand()
        return self.sum 

    def display(self):
        if self.dealer:
            print(self.cards[0].value)
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
            self.player_hand.display
            print()
            print("Dealer's hand is:")
            self.dealer_hand.display()

            game_over = False 

            while not game_over:
                player_with_blackjack, dealer_with_blackjack = self.check_if_blackjack()
                if player_with_blackjack or dealer_with_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_with_blackjack, dealer_with_blackjack)
                    continue
                if self.dealer_is_over():
                    print("Dealer busted you won!")
                    game_over = True

                hit_stand = input("'What would you like to do:\n [1] Hit or [2] Stand?")
                if hit_stand == '1':
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You have busted dealer won")
                        game_over = True
                elif hit_stand == '2':
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    if player_hand_value > dealer_hand_value:
                        print("You won")
                    elif player_hand_value == dealer_hand_value:
                        print("Tie")
                    else:
                        print("Dealer won")

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

    def show_blackjack_results(self,player_with_blackjack, dealer_with_blackjack):
        if player_with_blackjack and dealer_with_blackjack:
            print("Both players have blackjack! Draw!")
        elif player_with_blackjack:
            print("You have blackjack! You win!")
        elif dealer_with_blackjack:
            print("Dealer has blackjack! Dealer wins!")

if __name__ == "__main__":
    game = Game()
    game.play()