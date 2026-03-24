import os

import readchar


def clear_screen():
    os.system("clear")

def display(n=0, options=[]):
    print("choose what to run (up and down):")
    for i in range(len(options)):
        if i == n:
            print("> " + options[i])
        else:
            print("  " + options[i])


options = [
    "python3 main.py",
    "python3 main.py --show-team",
    "python3 main.py --count",
    "python3 main.py --greet",
]

display(1, options)

# todo make it choosable
