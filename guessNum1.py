import random


def guessN(x):
    rand_num = random.randint(1, x)
    guess = 0
    i = 1
    while guess != rand_num:
        if i == 1:
            guess = int(input(f"Guess a number between 1 and {x}: "))
        else:
            guess = int(input(f"Guess Again: "))
        i += 1

        if guess < rand_num:
            print("Ooooh! Your guess is low!")
        elif guess > rand_num:
            print("Ooooh! Your guess is high!")
    print(f"Yay, congrats! You have guessed the number {rand_num} correctly!")


response = input("Are you ready to play a guessing game? ")
if response in "yes":
    print("Great! Let's go!")
    guessN(int(input("Enter a numeric range within which you wanna guess: ")))
else:
    print("Oh. That's okay. Farewell.")
