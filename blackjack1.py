# importing random, generates a random int
from random import randint

# this class is for defining the individual card
class Card:
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

# repr method that prints the props as strings when the class Card is returned 
  def __repr__(self):
    return f"{self.value} of {self.suit}"

# this class defines the instance of deck (which is composed of cards from the Card class)
class Deck:
  def __init__(self):
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    # creates a list of all 52 possible card combinations
    self.cards = [Card(value, suit) for suit in suits for value in values]
  
  # counts all cards in the deck
  def count(self):
    return len(self.cards)
  
  # repr method that prints the amount of cards in the instance of class Deck
  def __repr__(self):
    return f"Deck of {self.count()} cards."
	
  # deals one card randomly from the deck
  def deal_card(self):
    index = randint(0, self.count() - 1)
    return self.cards[index]
    
# Player class defines the player and stores the score of said player
class Player:
  def __init__(self):
    self.name = "PLAYER"
    self.score = 0
   
  # adds whatever card dealt to the score
  def calc_score(self, card):
    if card.value == "A":
      self.score += 1
      return card
    elif card.value == "J" or card.value == "Q" or card.value == "K":
      self.score += 10
      return card
    else:
      self.score += int(card.value)
      return card

  # repr method prints the player's name and the player's score
  def __repr__(self):
    return f"{self.name} score: {self.score}"
    
# the Dealer class is a child class that inherits from the Player class, this is used for the dealer in the game
class Dealer(Player):
  # uses the same props as the Player class, name and score
  def __init__(self):
    self.name = "DEALER"
    self.score = 0
  
# Game class contains all the blackjack specific gameplay methods, including what happens each turn, and how the winner and loser is defined
class Game:
  p1 = Player()
  d = Dealer()
  
  def __init__(self):
    self.deck = Deck()

  # method to be called whenever the player takes a turn, it deals a card to the player and updates the player score
  def player_turn(self):
    draw_card_p1 = self.deck.deal_card()
    return Game.p1.calc_score(draw_card_p1)

  # method to be called whenever the dealer takes a turn, it deals a card to the dealer and updates the dealer score
  def dealer_turn(self):
    draw_card_d = self.deck.deal_card()
    return Game.d.calc_score(draw_card_d)
  
  # method executes the first turn in blackjack whereby both the player and the dealer are dealt cards
  def first_turn(self):
    return f"PLAYER dealt: {self.player_turn()}\n{self.p1}\nDEALER dealt: {self.dealer_turn()}\n{self.d}"
    
  # this method returns the players second card drawn, and their updated score. However the dealer_turn method doesn't get called here, to represent that the dealers hand and score are hidden per rules of blackjack 
  def second_turn(self):
    return f"PLAYER dealt: {self.player_turn()}\n{self.p1}\nDEALER'S HAND WAS HIDDEN"

  # this method is called only if the player does not bust and chooses to "Stay". It contains the scenarios for which the player wins, dealer wins, or both tie.
  def win_or_lose(self):
    # player wins if player score is greater than dealer score, but player does not "Bust" i.e. score is 21 or below
    if self.p1.score <= 21 and self.p1.score > self.d.score:
      print(f"PLAYER wins!")
      return True
    # dealer wins if dealer score is greater than player score, but dealer does not "Bust" i.e. score is 21 or below
    elif self.d.score <= 21 and self.d.score > self.p1.score:
      print(f"DEALER wins!")
      return False
    # only remaining option is if both player and dealer have equal score, then a tie is declared
    else:
      print(f"IT'S A TIE YO")
      return None

  # this method is called within rest_of_game to run all of the player's future turns after the second turn (after second_turn() method gets called)
  def players_game(self):
    # repeatedly prompts player to "Hit" or "Stay", as long as player does not "Bust" by exceeding a score of 21
    while self.p1.score < 21:
      player_decision = input("PLAYER: Hit('H') or Stay('S'): ")
      # if player "Hit", the player_turn method is executed and the player is dealt a card
      if player_decision.upper() == 'H':
        print(f"PLAYER dealt: {self.player_turn()}\n{self.p1}")
      # if player "Stay", then the player turn ends and the dealers_game method is executed
      elif player_decision.upper() == 'S':
        return "PLAYER stays. DEALER turn."
        break
      else:
        player_decision = input("PLAYER: Hit('H') or Stay('S'): ")
    
    # returns True if player did not "Bust". This allows the rest_of_game method to execute the win_or_lose method
    if self.p1.score > 21:
      return False
    else:
      return True
  
  # this method is called within rest_of_game to run all of the dealer's future turns after the second turn (after second_turn() method gets called)
  def dealers_game(self):
  # runs dealer_turn which runs the dealer's second turn, and returns the the hidden score and card.
    print(f"DEALER hidden card is {self.dealer_turn()}\n{self.d}")
    # Then the while statement represents the turn the dealer may take if the score is below 21(dealer doesn't bust)
    while self.d.score < 21:
      # if the score is greater than or equal to 17 the dealer stays.
      if self.d.score >= 17:
        return f"DEALER stays."
        break
      else:
        # Otherwise the dealer hits, and their new score and card are printed.
        print(f"DEALER dealt: {self.dealer_turn()}\n{self.d}")
    if self.d.score > 21:
      # If the dealer's score is greater than 21 then dealers_game() returns false (represents a bust)
      return False
    else:
      # If the dealer's score is less than 21 then dealers_game() continues until the dealer busts or wins
      return True

  # this method runs after the second_turn() method. It calls to players_game and dealers_game. If neither the player nor dealer "Bust", this method will run the win_or_lose() method to declare a winner, loser, or tie.
  def rest_of_game(self):
    # returns True if player doesn't "Bust"
    if self.players_game():
      # returns True if dealer doesn't "Bust"
      if self.dealers_game():
        return self.win_or_lose()
      else:
        # if dealers_game() returns a false
        return "DEALER bust. PLAYER wins!"
    else:
      # if players_game() returns a false
      return "PLAYER bust. DEALER wins."
      

