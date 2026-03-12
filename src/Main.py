class TeamMember:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


people = [
    TeamMember("Berke Mamal", 1),
    TeamMember("Metin Kaan Kulga", 2),
    TeamMember("Elif Karakas", 3),
    TeamMember("Urban Porocnik", 4)
]


def greet(name):
    print(f"Hello {name}, Welcome!")

def member_greeting(team_name):
    return f"Hello from {team_name}! Welcome!"


def count_members(people):
    return len(people)


def display_team(people):
    print("TEAM yuri")
    print("=====================")
    print("Members:")
    for i, person in enumerate(people, start=1):
        print(f"    {i}) {person.name}")
    print("=====================")
    print(f"Total Members: {count_members(people)}")


if __name__ == '__main__':
    team_name = "Team Yuri" 
    greet("Team Yuri")
    display_team(people)
    print(member_greeting(team_name))

