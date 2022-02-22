from DeckofCards import *

print("Welcome to BlackJack!")


player1 = Player()

while player1.play_again:
  deck1 = DeckOfCards()
  player1.reset_player

  print("Before shuffle -------------")
  deck1.print_deck()
  deck1.shuffle_deck()
  print("After shuffle -------------")
  deck1.print_deck()

  # Draw 2 cards

  top_card = deck1.get_card()
  second_card = deck1.get_card()

  player1.add_to_hand(top_card, second_card)
  player1.set_score(top_card.val, second_card.val)


  print("Your first card is " + str(player1.hand[0]))
  print("Your second card is " + str(player1.hand[1]))
  print("Your total is:", player1.score)

  user_input = input("Would you lke to hit (y/n) ")

  if user_input == "y" or user_input == "yes":
    player1.hit_again = True

  while player1.hit_again:
    next_card = deck1.get_card()
    player1.add_to_hand(next_card)
    player1.add_score(next_card.val)
    print("Your total is:", player1.score)
    if player1.score > 21:
      player1.hit_again = False
      player1.bust()
      break
    keepHitting = input("Would you like to hit again? (y/n) ")
    if keepHitting == "n" or keepHitting == "no":
      player1.hit_again = False
    
  dealer_score = random.randint(17, 23)
  print("The dealers score is:", dealer_score)
  if player1.is_bust:
    print('Bust! You are a buster! Better luck next time buddy')
  elif dealer_score > 21 and player1.score <= 21:
    print("You win! The dealer busted and you didn't! Good job!")
  elif dealer_score > player1.score and player1.score <= 21:
    print("You lose! The dealer had a high score than you! Better luck next time!")
  elif player1.score > dealer_score and player1.score <= 21:
    print("You win! You score is higher than the dealer!")
  elif player1.score == dealer_score and player1.score <= 21:
    print("Tie! That means you are the winner! You both had the same score")

  play_again = input("Do you want to play again? (y/n)")
  if play_again == "n":
    player1.play_again = False
