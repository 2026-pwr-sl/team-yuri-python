import argparse
import utils
import team

parser = argparse.ArgumentParser()
parser.add_argument("--show-team", action="store_true")
parser.add_argument("--count", action="store_true")
parser.add_argument("--greet")  # gets name
try:
    args = parser.parse_args()
except:
    print("unrecognized arguments, rtfm (read the FRIENDLY manual)")

people = utils.load_team_data()

if args.show_team:
    utils.display_team(people)
    quit()
if args.count:
    count = utils.count_members(people)
    print("count:", count)
    quit()
if not args.greet == None:
    print("Hello {}.".format(args.greet))
    quit()


team_name = "Team Yuri"  # todo: add this to json


def team_greeting(team_name):
    return "Hello from {}! Welcome!".format(team_name)


if __name__ == "__main__":
    utils.greet("Team Yuri")
    utils.display_team(people)
    print(team_greeting(team_name))
    team.print_yuri()
