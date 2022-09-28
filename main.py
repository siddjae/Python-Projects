import random
from art import logo
from replit import clear

#defining the possibilities of the deck
deck = [11,2,3,4,5,6,7,8,9,10,10,10]
user_cards = []
dealer_cards = []


#dealing the cards at the beginning of the game
def deal_cards():
  for cards in range(0,2):
    chosen_user_card = random.choice(deck)
    chosen_dealer_card = random.choice(deck)
    user_cards.append(chosen_user_card)
    dealer_cards.append(chosen_dealer_card)

#function for if a user chooses to hit
def hit(player):
  chosen_player_card = random.choice(deck)
  player.append(chosen_player_card)

#calculating the score of a person's dealt cards
def calculate_score(hand):
  """function that takes the players hand returns the score of that hand"""
  score = 0
  for card in range(0,len(hand)):
    score = score + hand[card]
  if score > 21:
    if 11 in hand:
      score = 0
      index = hand.index(11)
      hand[index] = 1
      for card in range(0,len(hand)):
        score = score + hand[card]  
  return score

#function for determining winner
def determine_winner():
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)
  print(f"Dealers final hand: {dealer_cards}. Dealers final score: {dealer_score}")
  print(f"Your final hand: {user_cards}. Your final score: {user_score}\n")
  if user_score > 21: 
    print("You bust and lose!")
  elif dealer_score <= 21:
    if dealer_score == user_score:
      print("It's a draw. You Push!")
    elif dealer_score == 21:
      print("Dealer gets Blackjack! You lose :(")
    elif user_score == 21:
      print("Blackjack!! You win!!")
    elif dealer_score > user_score:
      print("Dealer wins!")
    else:
      print("You win!!")
  elif dealer_score > 21:
    if user_score < 21:
      print("Dealer busts. You win!")
    elif user_score == 21:
      print("You got Blackjack!! You win!")
  
#initial user input 
user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
to_play = True
if user_choice == "y":
  to_play = True

#begin game
while to_play == True:
  #initial actions
  user_cards = []
  dealer_cards = []
  print(logo)
  deal_cards()
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)
  #keep hitting dealer until above 21 
  while dealer_score < 17:
    hit(dealer_cards)
    dealer_score = calculate_score(dealer_cards)
    
  #print user score and dealer first card
  print(f"Your cards {user_cards}. Your current score: {user_score}")
  print(f"Dealer's first card: {dealer_cards[0]}")

  # #user decision to hit or not
  # hit_or_not = input("Type 'y' to get another card or type 'n' to pass: ")
  # #logical calculations based on user decision
  # if hit_or_not == "y":
  #   hit(user_cards)
  #   print(user_cards)
    
    #if user score is less than 21, ask if you want the user to keep hitting
  if user_score <= 20:
    keep_hitting = True
    while keep_hitting == True and user_score <=20:
      hit_or_not = input("Type 'y' to get another card or type 'n' to pass: ")
      
      if user_score <= 20 and hit_or_not == "y":
        hit(user_cards)
      user_score = calculate_score(user_cards)
      print(f"Your hand: {user_cards}")
      print(f"Your score: {user_score}")
      if hit_or_not == "n":
        keep_hitting = False
    determine_winner()
  else:
    determine_winner()     

  keep_playing = input("\nDo you want to play another game of blackjack? Type 'y' or 'n': ")
  
  if keep_playing == "n":
    to_play = False
  clear()
  

