import random, hangman_art, hangman_words

placeholder = ''
letter_stored = []
game_over = False
lives = 6

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)

for i in range(len(chosen_word)):
    placeholder += '_'
print(placeholder)

print(hangman_art.stages[lives])

while not game_over:
    display = ''

    guess = input('Please guess a letter: ').lower()

    for letter in chosen_word:
        if letter == guess:
            display += guess
            letter_stored.append(guess)
        elif letter in letter_stored:
            display += letter
        else:
            display += '_'
    print(display)

    if guess not in chosen_word:
        lives -= 1

    if lives == 0:
        game_over = True
        print('You lose...')
    elif '_' not in display:
        game_over = True
        print('You win!')

    print(hangman_art.stages[lives])