import os

import readchar


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

n = 0
max_n = len(options) - 1

display(n, options)

while True:
    # readchar.readkey() waits for a single key press
    key = readchar.readkey()

    if key == readchar.key.ESC:
        exit()
    if key == readchar.key.UP:
        if n <= 0:
            n = max_n
        else:
            n -= 1
        display(n, options)

    elif key == readchar.key.DOWN:
        if n >= max_n:
            n = 0
        else:
            n += 1
        display(n, options)

    elif key == readchar.key.ENTER:
        # clear_screen()
        print("Running: {}...".format(options[n]))
        os.system(options[n])
        break
