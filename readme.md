# _Black Jack_

#### _Program for the card game black jack, Version 1.0_

#### By _**Lana and Mai**_


## Description

_This is a python program writen to entertain the user, and allow the player_

## Project Specifications

| Behavior | Input | Output |
|---|---|---|
|The program prints introduction and gives the player an option to play blackjack | terminal command: python3 main.py | Welcome to Mai & Lana's Blackjack Game! 🐥, Would you like to play? enter Y or N: |
| Option 1: The player decides not to play, the program ends  |terminal command: N  | Okay, thanks for playing. See ya later!  |
|  Option 2: The player decides to play, the program runs two turns. First it deals the player one card and displays the player score and it deals the dealer one card and displays the dealer score. Then it deals the player another card and updates the score, but this time the it hides what card the dealer was dealt and the dealer updated score. Then program asks the player whether they want to Hit and receive another card, or Stay and end their turn for the rest of the game, maintaining their score. | terminal command: Y  |  PLAYER dealt: 2 of Diamonds
PLAYER score: 2
DEALER dealt: 10 of Clubs
DEALER score: 10
PLAYER dealt: 8 of Diamonds
PLAYER score: 10
DEALER'S HAND WAS HIDDEN
PLAYER: Hit('H') or Stay('S'):  |
| Option 1: The player chose "Hit" and receives another card and the updated score is shown. As long as the player score does not exceed 21 therby being "Bust", the player will be asked to "Hit" or "Stay" again.| terminal command: H   | PLAYER dealt: J of Spades
PLAYER score: 20
PLAYER: Hit('H') or Stay('S'):|
| Option 2: The player chose "Stay", the player turn ends and the dealer turn begins. The dealer is automatically dealt cards until the dealer reaches a score of 17, at which point the dealer automatically chooses to "Stay". If the dealer score exceeds 21 then the dealer has gone "Bust" and the player wins. If the dealer does not "Bust" then the winner is chosen based on the highest score. A tie is declared if both player and dealer have the same score. The overall game score is displayed and the player is prompted to play again. |  terminal command: S  |  DEALER hidden card is 5 of Diamonds
DEALER score: 13
DEALER dealt: 4 of Hearts
DEALER score: 17
PLAYER wins!
PLAYER overall score: 1 out of 1
DEALER overall score: 0 out of 1
Would you like to play again? enter Y or N:  |

## Setup/Installation Requirements

_In Terminal:_

* Navigate to where you want this application to be saved, i.e.:
```cd desktop```
* Clone the file from GitHub with HTTPS
```git clone https://github.com/LonleyBuzzyBee/black_jack.git```
* Open file in your preferred text editor
* On Mac: ```open -a {your text editor} black_jack```
* On Windows: ```{your text editor} black_jack```
* ternaminal command to run file: python3 main.py or python main.py

_To Download Manually:_

* Navigate to https://github.com/LonleyBuzzyBee/black_jack.
* Click green "Clone or Download" button.
* Click "Download ZIP".
* Click downloaded file to unzip.
* Open folder called "black-jack-master".


## Known Bugs

_No known bugs at this time._

## Support and contact details

_Have a bug or an issue with this application? [Open a new issue](https://github.com/LonleyBuzzyBee/black_jack/issues) here on GitHub._

## Technologies Used

* _Python3_
* _random library_


### License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2020 **_Mai and Lana_**