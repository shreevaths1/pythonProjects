import random
import colorama
from colorama import Fore


def comp_guess(x):
    name = input("My name is : ")
    low = 1
    high = x
    feedback = ''
    try:
        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low
            print(f"tuxpad guessed {guess}")
            feedback = input("Is my guess high(H/h), low(L/l) or correct(C/c) ? ").lower()
            if feedback == 'l':
                low = guess + 1
            elif feedback == 'h':
                high = guess - 1
    except Exception as e:
        print('\n' + Fore.RED + f'You are cheating, {name}!' + '\n')
    else:
        print(f"Yay tuxpad! You guesses the number {guess} correctly. Cool!")

x = 10
print(f"\nHey tuxpad, lets play a guessing game.\
\nGive me any number between 1 and {x} and I will give you a hint each time \
\nso that you can guess correctly the next time. \
\nOkay! Give me any number: ")
comp_guess(x)
