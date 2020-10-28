from random import randint

def getCard():
  card = randint(1, 13)
  return card

def displayCard():
  card = getCard()
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

  
# def cardScore():
# def dealCard():
# def deal():
# def playHand():
# def results():



print("Welcome to Mai & Lana's Blackjack Game! 🐥")

playing_game = input("Would you like to play black jack? enter Y or N: ")

while playing_game.upper() == "Y":
  print("here is your card: ", displayCard())
  playing_game = input("Would you like to play again? enter Y or N: ")

print("Okay, thanks for playing. See ya later!")