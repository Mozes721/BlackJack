import random
import os 
from constants import *
import pygame
import numpy as np
import itertools

# class Card:
#     def __init__(self, suit, value):
#         if (suit in SUITS) and (value in RANKS):
#             self.suit = suit  
#             self.value = value  
#         else:
#             self.suit = None
#             self.rank = None
#             print("Invalid card: ", suit, value)
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.cards.append((value, suit))
  
    def shuffle(self):
        random.shuffle(self.cards)
        

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()
    
    # def get_suit(self):
    #     return self.suit

    # def get_value(self):
    #     return self.value

    # def __str__(self):
    #     return " ".join( [ str(card) for card in self.cards ] )


class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.value = 0 

    def add_card(self, card):
        self.cards.append(card)

    def calc_hand(self):

        first_card_index = [a_card[0] for a_card in self.cards]
        non_aces = [c for c in first_card_index if c != 'A']
        aces = [c for c in first_card_index if c == 'A']

        for card in non_aces:
            if card in 'JQK':
                self.value += 10
            else:
                self.value += int(card)

        for card in aces:
            if self.value <= 10:
                self.value += 11
            else:
                self.value += 1

    def get_value(self):
        self.calc_hand()
        print(self.value)

        
    def display_cards(self):
        for card in self.cards:
            dealer_cards = "".join((card[0], card[1]))
            if dealer_cards not in self.card_img:
                self.card_img.append(dealer_cards)
            
    # def dealer_display(self):
    #     for card in self.cards:
    #         dealer_cards = "".join((card[0], card[1]))
    #         self.card_img.append(dealer_cards)
     
        

class Game(Hand):
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
            self.player_hand.player_display()
            print()
            print("Dealer's hand is:")
            self.dealer_hand.dealer_display()

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

                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You have busted dealer won")
                        game_over = False

                else:
                    player_hand_rank = self.player_hand.get_value()
                    dealer_hand_rank = self.dealer_hand.get_value()

                    print("Final Results:")
                    print("Your hand:", player_hand_rank)
                    print("Dealer's hand:", dealer_hand_rank)

                    if player_hand_rank > dealer_hand_rank:
                        print("You Win!")
                    elif player_hand_rank == dealer_hand_rank:
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