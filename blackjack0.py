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
def dealCard():
  cardDrawn = getCard()
  return displayCard(cardDrawn)

# def deal():
# def playHand():
# def results():


print("Welcome to Mai & Lana's Blackjack Game! 🐥")

playing_game = input("Would you like to play black jack? enter Y or N: ")

while playing_game.upper() == "Y":

  player_score = 0 
  dealer_score = 0

  # player first card
  print(f"PLAYER was dealt: {dealCard()}"
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
  
  # prompt player if they want to hit or stand
  player_move = input("Player move. Type 'H' to hit or 'S' to stand: " )
  if player_move == 'H':
    
    print(f"PLAYER was dealt: {dealCard()}")
    player_score += cardScore(player_card)
    
# win_vs_lose()
# if (cases where they would win)
#   return win as true or return string that p or d wins
# elif (cases of loses)
#   return lost
# else (neither)
#  then run player_move()

# player_move():
# prompt = input("H or S": ")
# if prompt == "H":
#   run player_turn()
# if prompt == "S":
#   run dealers_game()

# dealers_game():
# if dealer score >= 17:
#   calculate score of player and dealer and declare winner
# while dealer score < 17:
#   dealer hits


# player_move()
# win_vs_loss()
# if (win or lose)
#   then just print win_vs_lose
# elif (hit)
#  funct for player & dealer turn
# elif(stay)
#  don't do anything to score



  # if "HIT" then drawCard
  # if "STAND" then pass option to dealer
  # if "BUST" then do if statement,



  playing_game = input("Would you like to play again? enter Y or N: ")

print("Okay, thanks for playing. See ya later!")