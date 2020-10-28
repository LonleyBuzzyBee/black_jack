from random import randint

# this function generates a random card between 1 and 13
def getCard():
  card = randint(1, 13)
  return card

# this function assigns which card you drew out of the card deck as a string
def displayCard(card):
  cards = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")

  suit_generator = randint(0, 4)
  if suit_generator == 0:
    suit = "Spades"
  elif suit_generator == 1:
    suit = "Diamonds"
  elif suit_generator == 2:
    suit = "Clubs"
  else:
    suit = "Hearts"
  
  your_card = cards[card - 1]
  return your_card + " of " + suit

# this function gets the card value
def cardScore(card):
  if card >= 2 or card <= 10:
    card_score = card
  elif card == 1:
    card_score = 11
  elif card > 10:
    card_score = 10
  
  return card_score
  
# def dealCard():
# def deal():
# def playHand():
# def results():


print("Welcome to Mai & Lana's Blackjack Game! 🐥")

playing_game = input("Would you like to play black jack? enter Y or N: ")

while playing_game.upper() == "Y":

  player_score = 0 
  dealer_score = 0

  # player first card
  player_card = getCard()
  print("PLAYER was dealt: ", displayCard(player_card))
  player_score += cardScore(player_card)

  # dealer first card
  dealer_card = getCard()
  print("DEALER was dealt: ", displayCard(dealer_card))
  dealer_score += cardScore(dealer_card)

  # player second card
  player_card = getCard()
  print("PLAYER was dealt: ", displayCard(player_card))
  player_score += cardScore(player_card)

  # dealer second card
  dealer_card = getCard()
  print("DEALER was dealt: ", displayCard(dealer_card))
  dealer_score += cardScore(dealer_card)

  print(f"PLAYER score = {player_score}")
  print(f"DEALER score = {dealer_score}")


  playing_game = input("Would you like to play again? enter Y or N: ")

print("Okay, thanks for playing. See ya later!")