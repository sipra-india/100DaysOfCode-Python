stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    
word_list = [
    "monkey", "flower", "pirate", "castle", "turtle", "rocket", "window",
    "school", "guitar", "forest", "dragon", "planet", "circus", "tunnel",
    "basket", "donkey", "puppet", "castle", "ladder", "puzzle", "camera",
    "ticket", "summer", "basket", "winter", "anchor", "banana", "cherry",
    "bubble", "engine", "muffin", "pillow", "planet", "ladder", "parrot",
    "circle", "ticket", "winter", "circus", "laptop", "mouse", "wagon",
    "apple", "grape", "mango", "apple", "cherry", "train", "robot", "radio",
    "party", "honey", "tiger", "lemon", "comet", "ocean", "river", "pizza",
    "smile", "dream", "arrow", "cloud", "color", "candy", "heart", "piano",
    "beach", "mouse", "email", "smile", "shirt", "chair", "lamp", "clock",
    "plant", "shoes", "socks", "watch", "chair", "brush", "paint", "bridge",
    "mouse", "eagle", "horse", "chair", "phone", "glass", "ruler", "table",
    "snake", "chair", "paper", "spoon", "fork", "knife", "plate", "olive",
    "chair", "chair"
]

import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(logo)
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(
            f"You guessed {guess}, but it's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
