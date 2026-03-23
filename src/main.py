import argparse

from team import *
from utils import *

parser = argparse.ArgumentParser(description="Example program")
parser.add_argument("--show-team", action="store_true")
parser.add_argument("--count", action="store_true")
parser.add_argument("--greet")  # gets name
args = parser.parse_args()

if args.show_team:
    display_team(people)
    quit()
if args.count:
    count = count_members(people)
    print("count:", count)
    quit()
if not args.greet == None:
    print("Hello {}.".format(args.greet))
    quit()

    
team_name = "Team Yuri"

def member_greeting(team_name):
    return f"Hello from {team_name}! Welcome!"


if __name__ == "__main__":
    greet("Team Yuri")
    display_team(people)
    print(member_greeting(team_name))
    print_yuri()


