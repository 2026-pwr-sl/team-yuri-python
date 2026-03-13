# To run this test you need to move this test script the same path as Main.py
from Main import *

people = [
    TeamMember("asd", 1),
    TeamMember("asd", 1),
    TeamMember("asd", 1),
    TeamMember("asd", 1),
    TeamMember("asd", 1),
    TeamMember("asd", 1),
]

greet(people[0].name)
print(count_members(people))
display_team(people)

print_yuri()
