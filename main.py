# imports all the backend code implemented in blackjack1.py
from blackjack1 import Game

if __name__ == '__main__':

  # gives the player a friendly greeting/ introduction
  print("Welcome to Mai & Lana's Blackjack Game! 🐥")

  # prompts player to play and stores answer in playing_game variable
  playing_game = input("Would you like to play? enter Y or N: ")

  # create a new instance of blackjack game
  newGame = Game()

  # ----NEW CODE------
  player_overall_score = 0
  dealer_overall_score = 0
  games_played = 0
  # ----NEW CODE------

  # repeatedly runs the game as long as the player responds "Y" to play again
  while playing_game.upper() == "Y":
    # set the player score to 0 for the start of a new game
    newGame.p1.score = 0
    # set the dealer score to 0 for the start of a new game
    newGame.d.score = 0
    
    # runs method for the first turn of the game
    print(newGame.first_turn())
    # runs method for the second turn of the game
    print(newGame.second_turn())
    # runs method for the rest of the game, also checks for winners
    print(newGame.rest_of_game())
    games_played += 1
    if newGame.win_or_lose() == "PLAYER wins!":
      player_overall_score += 1
    elif newGame.win_or_lose() == "DEALER wins!":
      dealer_overall_score += 1

    print(f"PLAYER overall score: {player_overall_score} out of {games_played}\nDEALER overall score: {dealer_overall_score} out of {games_played}")

    # check if player wants to play again
    playing_game = input("Would you like to play again? enter Y or N: ")
  # outro for game once the player says 'N'
  print("Okay, thanks for playing. See ya later!")