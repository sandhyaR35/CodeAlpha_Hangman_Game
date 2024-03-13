import random
import stages
import words
lives = 6
chosen_word = random.choice(words.words)
#print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter:")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        print("you lost a life and remaining lives will be",lives)
        if lives == 0:
            game_over = True
            print("You lose")
    if '_' not in display:
        game_over = True
        print("You Won! you have guessed the word:",chosen_word)
    print("Here is your Hangman:")
    print(stages.stages[lives])


