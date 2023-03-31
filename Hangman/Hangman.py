import random
from hangman_list import words

word_list = words
choosen = random.choice(word_list).lower()
print(f"word is {choosen}")
blank = []
for _ in range(len(choosen)):
    blank.append("_")

print(blank)
lives = 6
from hangman_art import logo

print(logo)
end_of_game = False
while not end_of_game:
    guess = (input("guess a letter : "))

    if guess in blank:
        print(f"You've already guessed {guess}")
    for pos in range(len(choosen)):
        if choosen[pos] == guess:
            blank[pos] = guess

    if guess not in choosen:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
    print(blank)
    if "_" not in blank:
        end_of_game = True
        print("you won!!")
    from hangman_list import HANGMANPICS
    p = len(HANGMANPICS)
    print(HANGMANPICS[p - lives])