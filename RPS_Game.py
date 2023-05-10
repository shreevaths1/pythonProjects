import random
import colorama
from colorama import Fore

print("Welcome to Rock , Paper , Scissors \
\nI am excited to play with you! Let's Play\n")

i = j = 0


def play():
    global i
    global j

    play_again = 'y'
    while play_again in 'yes':
        user = input(
            Fore.RESET + "\nWhat do you choose? \'r\' for Rock, \'s\' for Scissors and \'p\' for Paper: \n").lower()
        computer = random.choice(['r', 'p', 's'])
        while user == computer:
            print(Fore.BLUE + "That's a draw")
            user = input("Try Again. \'r\' for Rock, \'s\' for Scissors and \'p\' for Paper: ").lower()
            computer = random.choice(['r', 'p', 's'])

        if win(user, computer):
            print(Fore.GREEN + "You Won! Awesome!")
            i += 1
        else:
            print(Fore.RED + "Haha , you lost! Better luck next time.")
            j += 1

        play_again = input(Fore.RESET + "\nWanna try again ? (y / n): \n").lower()


def win(player, opponent):
    # r > s , s > p , p > r
    if (player == 'r' and opponent == 's') or \
            (player == 's' and opponent == 'p') or \
            (player == 'p' and opponent == 'r'):
        return True


play()
if i == j:
    print("Seems like both of us have the same brain.")
elif i < j:
    print("Looks like I am more intelligent compared to you!")
else:
    print("Looks like you are more intelligent compared to me!")
