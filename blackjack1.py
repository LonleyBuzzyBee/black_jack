from random import randint


class Card:
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

  def __repr__(self):
    return f"{self.value} of {self.suit}"

class Deck:
  def __init__(self):
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    self.cards = [Card(value, suit) for suit in suits for value in values]

  def count(self):
    return len(self.cards)

  def __repr__(self):
    return f"Deck of {self.count()} cards."
	
  def deal_card(self):
    index = randint(0, self.count() - 1)
    return self.cards[index]
    
# leave this for rn

class Player:
  def __init__(self):
    self.name = "PLAYER"
    self.score = 0
   
  #  adds whatever is passed in to the score
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

  
  def __repr__(self):
    return f"{self.name} score: {self.score}"
  
class Dealer(Player):
  def __init__(self):
    self.name = "DEALER"
    self.score = 0
  
class Game:
  p1 = Player()
  d = Dealer()
  
  def __init__(self):
    self.deck = Deck()

  def player_turn(self):
    draw_card_p1 = self.deck.deal_card()
    return Game.p1.calc_score(draw_card_p1)

  def dealer_turn(self):
    draw_card_d = self.deck.deal_card()
    return Game.d.calc_score(draw_card_d)
  
  def first_turn(self):
    return f"PLAYER dealt: {self.player_turn()}\n{self.p1}\nDEALER dealt: {self.dealer_turn()}\n{self.d}"
  
  def second_turn(self):
    return f"PLAYER dealt: {self.player_turn()}\n{self.p1}\nDEALER'S HAND WAS HIDDEN"

  def win_or_lose(self):
    if self.p1.score <= 21 and self.p1.score > self.d.score:
      return f"PLAYER wins!"
    elif self.d.score <= 21 and self.d.score > self.p1.score:
      return f"DEALER wins!"
    else:
      return f"IT'S A TIE YO"

  
  def players_game(self):
    while self.p1.score < 21:
      player_decision = input("PLAYER: Hit('H') or Stay('S'): ")
      if player_decision.upper() == 'H':
        print(f"PLAYER dealt: {self.player_turn()}\n{self.p1}")
      elif player_decision.upper() == 'S':
        return "PLAYER stays. DEALER turn."
        break
      else:
        player_decision = input("PLAYER: Hit('H') or Stay('S'): ")
    if self.p1.score > 21:
      return False
    else:
      return True
    

  def dealers_game(self):
    print(f"DEALER hidden card is {self.dealer_turn()}\n{self.d}")
    while self.d.score < 21:
      if self.d.score >= 17:
        return f"DEALER stays."
        break
      else:
        print(f"DEALER dealt: {self.dealer_turn()}\n{self.d}")
    if self.d.score > 21:
      return False
    else:
      return True

  def rest_of_game(self):
    if self.players_game():
      if self.dealers_game():
        return self.win_or_lose()
      else:
        return "DEALER bust. PLAYER wins!"
    else:
      return "PLAYER bust. DEALER wins."
      
  
print("Welcome to Mai & Lana's Blackjack Game! 🐥")
playing_game = input("Would you like to play? enter Y or N: ")
newGame = Game()
while playing_game.upper() == "Y":
  newGame.p1.score = 0
  newGame.d.score = 0
  print(newGame.first_turn())
  print(newGame.second_turn())
  print(newGame.rest_of_game())
  playing_game = input("Would you like to play again? enter Y or N: ")
print("Okay, thanks for playing. See ya later!")

