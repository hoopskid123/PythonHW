import random

class Card():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.val = value
        
    def __str__(self):
        return self.face + " of " + self.suit + ", value: " + str(self.val)


class DeckOfCards():
    def __init__(self):
        self.deck = []
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.play_idx = 0
        
        for suit in self.suits:
            i = 0
            for i in range(len(self.faces)):
                self.deck.append(Card(suit, self.faces[i], self.values[i]))
                
                
    def shuffle_deck(self):
        random.shuffle(self.deck)
        
    def print_deck(self):
        for card in self.deck:
            print(card.face, "of", card.suit, end=", ")
        print("---")

    def get_card(self):
        self.play_idx += 1
        return self.deck[self.play_idx - 1]


class Player():
  def __init__(self):
      self.score = 0
      self.hit_again = False
      self.is_bust = False
      self.stay = False
      self.play_again = True
      self.hand = []
      

  def set_score(self, score1, score2):
    self.score = score1 + score2

  def add_score(self, newscore):
    self.score += newscore

  def reset_player(self):
    self.score = 0
    # self.hitAgain = False
    # self.isBust = False
    # self.stay = False
    # self.playAgain = True
    self.is_bust = False
    self.hand = []

  def add_to_hand(self, card1, card2=0):
    self.hand.append(card1)
    self.hand.append(card2)

  def bust(self):
    self.is_bust = True