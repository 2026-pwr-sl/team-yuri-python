class TeamMembers:
    def __init__(self, name, id):
        self.name = name
        self.id = id

people = [
    TeamMembers("Berke Mamal", 1),
    TeamMembers("Metin Kaan Kulga", 2),
    TeamMembers("Elif Karakas", 3),
    TeamMembers("Urban Porocnik", 4)
]

def teamMembers():
    count = 0
    for person in people:
        count = count + 1

    print("Theres currently " + str(count) + " people in the team")
    return count
def greeting(name):
    print("Hello " + str(name) + ", Welcome!")

def displayTeam(people):
    print("TEAM: TEAM yuri")
    print("=====================")
    print("Members:")
    for i,  person in enumerate(people, start = 1):

        print(str(i) + "." + person.name)

    print("=====================")
    print("Total Members: " + str(len(people)))



teamMembers()
greeting("Person")
displayTeam(people)






