import json
import os

import team


def count_members(people):
    return len(people)


def greet(name):
    print("Hello {}, Welcome!".format(name))


def display_team(people):
    print("TEAM yuri")
    print("=====================")
    print("Members:")
    for i, member in enumerate(people, start=1):
        print("    {}) {}".format(i, member.name))
    print("=====================")
    print("Total Members: {}".format(count_members(people)))


def search_member(people, name=None, student_id=None):
    found_something = False

    if (student_id == None) and (name == None):
        raise ValueError("At least one of 'name' or 'student_id' must be provided")

    if not student_id == None:
        for member in people:
            if student_id == member.student_id:
                print(
                    "exact match: name={} student_id={}".format(
                        member.name, member.student_id
                    )
                )
                found_something = True

    if not name == None:
        for member in people:
            if name.lower() == member.name.lower():
                continue
                print(
                    "exact match: name={} student_id={}".format(
                        member.name, member.student_id
                    )
                )
                found_something = True
            elif name.lower() in member.name.lower():
                print(
                    "partial match: name={} student_id={}".format(
                        member.name, member.student_id
                    )
                )
                found_something = True

    if not found_something:
        print("no match...")


def load_team_data():
    if "team_data.json" not in os.listdir("."):
        print("team_data.json not found...")
        exit(2)
    with open("team_data.json", "r") as f:
        team_data = json.loads(f.read())

    people = []
    for member in team_data:
        member_to_add = team.TeamMember(member["name"], member["id"])
        people.append(member_to_add)

    return people


def add_to_team_data(people, member):
    people.append(member)
    write_team_data(people)

    return people


def write_team_data(people):
    tmp_obj = []
    for member in people:
        tmp_obj.append({"id": member.student_id, "name": member.name})

    if "team_data.json" not in os.listdir("."):
        print("team_data.json not found...")
        exit(2)

    with open("team_data.json", "w") as f:
        f.write(json.dumps(tmp_obj, indent=4))
import json
import team
import os


def count_members(people):
    return len(people)


def greet(name):
    print("Hello {}, Welcome!".format(name))


def display_team(people):
    print("TEAM yuri")
    print("=====================")
    print("Members:")
    for i, member in enumerate(people, start=1):
        print("    {}) {}".format(i, member.name))
    print("=====================")
    print("Total Members: {}".format(count_members(people)))


def search_member(people, name=None, student_id=None):
    found_something = False

    if (student_id==None) and (name==None):
        raise ValueError("At least one of 'name' or 'student_id' must be provided")

    if not student_id==None:
        for member in people:
            if student_id == member.student_id:
                print("exact match: name={} student_id={}".format(member.name, member.student_id))
                found_something = True

    if not name==None:
        for member in people:
            if name.lower() == member.name.lower():
                print("exact match: name={} student_id={}".format(member.name, member.student_id))
                found_something = True
            elif name.lower() in member.name.lower():
                print("partial match: name={} student_id={}".format(member.name, member.student_id))
                found_something = True

    if not found_something:
        print("no match...")


def load_team_data():
    if not "team_data.json" in os.listdir('.'):
        print("team_data.json not found...")
        exit(2)
    with open("team_data.json", "r") as f:
        team_data = json.loads(f.read())

    people = []
    for member in team_data:
        member_to_add = team.TeamMember(member["name"], member["id"])
        people.append(member_to_add)

    return people


def add_to_team_data(people, member):
    people.append(member)
    write_team_data(people)

    return people



def write_team_data(people):
    tmp_obj = []
    for member in people:
        tmp_obj.append({"id": member.student_id, "name": member.name})

    if not "team_data.json" in os.listdir('.'):
        print("team_data.json not found...")
        exit(2)

    with open("team_data.json", "w") as f:
        f.write(json.dumps(tmp_obj, indent=4))
