def count_members(people):
    return len(people)


def display_team(people):
    print("TEAM yuri")
    print("=====================")
    print("Members:")
    for i, person in enumerate(people, start=1):
        print("    {}) {}".format(i, person.name))
    print("=====================")
    print(f"Total Members: {count_members(people)}")
