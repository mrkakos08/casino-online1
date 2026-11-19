class Player:
    def __init__(self, fname, age, credits):
        self.fname= fname
        self.age= age
        self.credits= credits
    def add_credits(self, new_credits):
        self.credits+= new_credits
    def substract_credits(self, bet_credits):
        self.credits-= bet_credits

import random
class Blackjack:
    def __init__(self, player):
        self.player= player
        self.player_hand=[]
        self.dealer_hand=[]
        self.deck= [('A','♥️'), (2,'♥️'), (3,'♥️'), (4,'♥️'), (5,'♥️'), (6,'♥️'), (7,'♥️'), (8,'♥️'), (9,'♥️'), (10,'♥️'), ('J','♥️'), ('Q','♥️'), ('K','♥️'), ('A','♦️'), (2,'♦️'), (3,'♦️'), (4,'♦️'), (5,'♦️'), (6,'♦️'), (7,'♦️'), (8,'♦️'), (9,'♦️'), (10,'♦️'), ('J','♦️'), ('Q','♦️'), ('K','♦️'), ('A','♠️'), (2,'♠️'), (3,'♠️'), (4,'♠️'), (5,'♠️'), (6,'♠️'), (7,'♠️'), (8,'♠️'), (9,'♠️'), (10,'♠️'), ('J','♠️'), ('Q','♠️'), ('K','♠️'), ('A','♣️'), (2,'♣️'), (3,'♣️'), (4,'♣️'), (5,'♣️'), (6,'♣️'), (7,'♣️'), (8,'♣️'), (9,'♣️'), (10,'♣️'), ('J','♣️'), ('Q','♣️'), ('K','♣️')]
        while True:
            self.bet = int(input("How many credits would you like to bet? "))
            if 0 < self.bet <= self.player.credits:
                break
            print("Enter a valid bet")
        self.player.substract_credits(self.bet)
        random.shuffle(self.deck)
        for x in range(2):
            card=self.deck.pop()         
            self.player_hand.append(card)
        card = self.deck.pop()
        self.dealer_hand.append(card)
        print("Player cards:")
        for card in self.player_hand:
            print(card[0], card[1])
        print("Dealer cards:")
        for card in self.dealer_hand:
            print(card[0], card[1])
    def card_value(self, hand):
        total=0
        aces=0
        for card in hand:
            rank = card[0]
            if rank in ['J', 'Q', 'K']:
                value= 10
            elif rank == 'A':
                value=11
                aces+=1
            else:
                value= rank
            total+=value
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total
    def player_turn(self):
        playerpoints= self.card_value(self.player_hand) 
        if playerpoints ==21:
            print("Blackjack!")
            self.player.add_credits(2.5*self.bet)
        else: 
            while playerpoints<21:
                player_action= input("Do you want to hit, stay or double? ")
                if player_action.lower() == 'hit':
                    card= self.deck.pop()
                    self.player_hand.append(card)
                    print('Your new card:')
                    print(card[0],card[1])
                    playerpoints=self.card_value(self.player_hand)
                elif player_action.lower()== "stay":
                    playerpoints=self.card_value(self.player_hand)
                    break
                elif player_action.lower()== "double":
                    if self.player.credits >= self.bet:
                        card=self.deck.pop()
                        self.player_hand.append(card)
                        print(card[0],card[1])
                        playerpoints=self.card_value(self.player_hand)
                        self.player.substract_credits(self.bet)
                        break
                    else:
                        print("You don't have enough credits")
    def dealer_turn(self):
        playerpoints= self.card_value(self.player_hand)       
        dealerpoints=self.card_value(self.dealer_hand)
        if playerpoints>21:
            print("You lost")
            print("Your balance is now:", self.player.credits, "credits")
            input("Press enter to play again: ")
            game=Blackjack(self.player)
            game.player_turn()
            game.dealer_turn()
        else:
            while playerpoints <21 and dealerpoints <=16:
                card=self.deck.pop()
                self.dealer_hand.append(card)
                dealerpoints = self.card_value(self.dealer_hand)
                print("Dealer's new card:")
                print(card[0],card[1])
                if dealerpoints<=16:
                    input("Press enter to check his next card: ")
            if dealerpoints>21:
                self.player.add_credits(2*self.bet)
                print("Congratulations, you won!")
                print("Your balance is now:", self.player.credits, "credits")
                input('Press enter to play again: ')
                game=Blackjack(self.player)
                game.player_turn()
                game.dealer_turn()
            elif playerpoints > dealerpoints:
                self.player.add_credits(2*self.bet)
                print("Congratulations, you won!")
                print("Your balance is now:", self.player.credits, "credits")
                input("Press enter to play again: ")
                game=Blackjack(self.player)
                game.player_turn()
                game.dealer_turn()
            elif playerpoints < dealerpoints:
                print("You lost")
                print("Your balance is now:", self.player.credits , "credits")
                input("Press enter to play again: ")
                game=Blackjack(self.player)
                game.player_turn()
                game.dealer_turn()
            elif dealerpoints == playerpoints:
                self.player.add_credits(self.bet)
                print("There is a tie")
                print("Your balance is now:", self.player.credits, "credits")
                input('Press enter to play again: ')
                game=Blackjack(self.player)
                game.player_turn()
                game.dealer_turn()
                    
print('==============================================================================================')
print('|                         🎰                       ♠️                              💰         |')
print('|         🍉               Hello, Welcome to Online casino MiniGames!    🍉           🍒     |')
print('|                  ♦️                            ♥️                            💰              |')
print('|  ♠️    We have a huge variety of games, such as Blackjack, Roulette and Slot Machine  ♦️     |')
print('|                🍋                          ♣️                            🍇                 |')
print('|                                                                                            |', end='\r')
fname = input('|                                   Enter your first name: ')
print('|     🍒                           🎰                             🍋                  ♥️      |')
print('|                                                                                            |', end='\r')
age = int(input('|                                      Enter your age: '))
if age >=21:
    print('|                🍇                         💰                            ♠️                  |')
    print('|                                                                                            |', end='\r')
    game_selected = input('|                          Which game do you want to play today? ')
    print('|    ♣️                   🎰                       🍒                         ♦️               |')
    print('==============================================================================================')
    if game_selected.lower() == "blackjack":
        credits=int(input('\nHow many credits would you like to start with? '))
        player1=Player(fname,age,credits)
        game=Blackjack(player1)
        game.player_turn()
        game.dealer_turn()
    else:
        print("\nno")
else:
    print('==============================================================================================')
    print("\nSorry, you are under 21, you can not play.")
