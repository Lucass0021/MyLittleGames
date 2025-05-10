import random

print("\nWelcome to the Hangman Game!!\n")

stages = [
    '''
     _______
    |/      |
    |
    |
    |
    |
    |___
    ''',
    r'''
     _______
    |/      |
    |      (_)
    |
    |
    |
    |___
    ''',
    r'''
     _______
    |/      |
    |      (_)
    |       |
    |
    |
    |___
    ''',
    r'''
     _______
    |/      |
    |      (_)
    |      \|
    |
    |
    |___
    ''',
    r'''
     _______
    |/      |
    |      (_)
    |      \|/
    |
    |
    |___
    ''',
    r'''
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |
    |___
    ''',
    r'''
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \\
    |___
    '''
]

while True:
    words_list = ["python", "banana", "fiap", "cake", "ball"]
    selected_word = random.choice(words_list)
    corrects_letters = []
    incorrect_letters = []
    max_attempts = 6

    while True:
        letter = input("Type a letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Please type a single letter (A-Z).")
            continue

        if letter in corrects_letters or letter in incorrect_letters:
            print("You already tried this letter. Try another one.")
            continue

        if letter in selected_word:
            corrects_letters.append(letter)
        else:
            max_attempts -= 1
            incorrect_letters.append(letter)
            print(f"Number of attempts remaining: {max_attempts}")
            print("Incorrect letters:", " ".join(incorrect_letters))

        print(stages[len(incorrect_letters)])  # <-- Mostra a forca aqui

        display = ""
        for l in selected_word:
            display += l + " " if l in corrects_letters else "_ "
        print("Current word: ", display) 

        if all(l in corrects_letters for l in selected_word):
            print(f"Congratulations!! You win the Hangman Game. The secret word is {selected_word}")
            break

        if max_attempts == 0:
            print(f"Oh no.. You lost the game! Unfortunately the secret word was {selected_word}")
            break

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing Hangman! Goodbye.")
        break
