from team import *
from utils import *

team_name = "Team Yuri"

def member_greeting(team_name):
    return f"Hello from {team_name}! Welcome!"


if __name__ == "__main__":
    greet("Team Yuri")
    display_team(people)
    print(member_greeting(team_name))
    print_yuri()
