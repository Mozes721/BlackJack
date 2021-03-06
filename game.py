from cards import *

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

            # print("Your hand is:")
            # self.player_hand.display()
            # print()
            # print("Dealer's hand is:")
            # self.dealer_hand.display()

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
