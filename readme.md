# blackjack game

# logic---------------------------------------

# RULES
# player and dealer each dealt card
    # player score = player first card value
    # dealer score = dealer first card value
# player dealt second card, value shown
    # player score += second card value
# dealer dealt second card, value hidden
    # dealer score += second card value
    # but as the player we don't get to see this updated score
# if player score = 21
    # player hand ends, see Winning
# else player can "hit" (take another card) or "stand" (no more cards)
# if player "hit"
    # if player score > 21
        # player score = bust
        # dealer wins
    # if player score < 21
        # can choose to "hit" or "stand"
# if player "stand" and score <= 21
    # dealer hidden card and total score revealed
# if dealer score >= 17
    # dealer must "stand"
# else if dealer score < 17
    # dealer must "hit" until dealer score > 17 or "bust"

# WINNING AND LOSING
# if player first card + second card = 21 && dealer first card + second card != 21
    # player wins
# if dealer first card + second card = 21 && player first card + second card != 21
    # dealer wins
# if both player and dealer first card + second card = 21
    # neither wins or loses
# if player "stands" && dealer "bust"
    # player wins
# if player "stands" && dealer "stands"
    # highest score wins


# funtions that need to be used --------------------------
# displayCard() - the param should be a be a val 1 - 13 from which the type of card can be determined (1 = ace, 2 = two, …, 10, == ten, 11 =jack, 12 = queen, 13 = king) card suit (clubs, diamons, hearts or spades) should be determined rand
# getCard() - returns random val between 1 - 13
# cardScore() - returns val between 2 - 11 as described in rules, Recall that the score is the card's value
# except that aces are worth 11 and face cards are worth 10. The card parameter represents the card for
# which the score is to be determined.
# deal() - handles dealing cards
# needs to loop through and give the option to play again


# how the program should work ------------------------------
# 1. Print a welcome message
# 2. Ask the user if they want to play blackjack, continue if the
# answer is 'y'; otherwise exit the program (8).
# 3. Deal two cards to the player and two to the dealer (see
# Rules 1 to 3)
# 4. Determine if the player or dealer has a score of 21. If so,
# determine who wins (see Rules, Winning and Losing 1 to
# 3), print an appropriate message and return to the main
# program at 2; otherwise continue
# 5. Deal cards to the player until she stands or goes bust (see
# Rules 5), if the player is bust, print an appropriate
# message and return to the main program at 2; otherwise
# continue
# 6. Deal cards to the dealer until their score is over 17 (see
# Rules 6 to 8)
# 7. Determine who wins (see Rules, Winning and Losing 4 and
# 5), print an appropriate message and return to the main
# program at 2
# 8. When the user decides to quit the program print a message indicating how many hands the user
# won, lost and drew  



# getCard() (used inside first func)
# dictionScores = {dealer:["2 of aces"], player:[4 of diamonds]}

# displayCard()
#  player and dealer each dealt card
    # player score = player first card value
    # dealer score = dealer first card value
# player dealt second card, value shown
    # player score += second card value
# dealer dealt second card, value hidden
    # dealer score += second card value
    # but as the player we don't get to see this updated score
    
# cardScore()
# calcScore()
# 
# compare each key value pair to determine the winner or loser
