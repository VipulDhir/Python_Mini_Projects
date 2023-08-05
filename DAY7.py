# HANGMAN GAME

# Step 1 
# word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# import random
# choosen_word= random.choice(word_list)
# print(choosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input ("guess a word").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# for letter in word_list:
#     if letter ==guess:
#         print("right")
#     else:
#         print("wrong")

lives = 6


word_list = ["aardvark", "baboon", "camel"]

import random
chosen_word= random.choice(word_list)
print(chosen_word)


display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input ("guess a word").lower()

    for position in range(len(chosen_word)):
        if chosen_word[position]==guess:
            display[position]=chosen_word[position]

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    if "_" not in display:
        end_of_game = True
        print("You win.")