import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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


word_list = ["apple", "banana", "mango"]

chosen_word = random.choice(word_list)

print("HEY WELCOME TO REDDY'S HANGMAN PROJECT.....!")
display = ""
for i in range(len(chosen_word)):
    display += "_"

print(display)

guessed_letters = []

lives = 6
game_over = False

while not game_over:

    guessed_letter = input("Guess a letter man : ").lower()

    correct_letters = ""

    for letter in chosen_word:

        if letter == guessed_letter:
            correct_letters += guessed_letter
            guessed_letters.append(letter)

        elif letter in guessed_letters:
            correct_letters += letter

        else:
            correct_letters += "_"
    display=correct_letters
    print(display)
    
    

    if guessed_letter not in chosen_word:
        lives -= 1
        print("❌ Wrong guess")
        print("Lives left:", lives)
        print(stages[lives])

    if "_" not in correct_letters:
        game_over = True
        print("🎉 Hey! You won")
        print("The word is:", chosen_word)

    if lives == 0:
        game_over = True
        print("💀 OOPS! You Lost")
        print("The word was:", chosen_word)