Team Yuri Project Documentation
Project Structure

The project is organized into three main directories with clear separation of concerns:
Directory	Purpose	Contents
src/	Source code	Main application files (main.py, team.py, utils.py) and team_data.json
tests/	Test suite	Unit tests in test_main.py
docs/	Documentation	Project notes and references

The data/ directory exists but is currently empty and available for future use.
Modules Overview
main.py — Entry Point

This is the command-line interface for the application. It handles argument parsing and orchestrates the program flow.

Key responsibilities:

    Parses command-line arguments
    Loads team data from JSON
    Routes to appropriate functions based on user input
    Displays a welcome message and team info on standard execution

team.py — Data Model

This module defines the TeamMember class and displays team branding.

Key components:

    TeamMember(name, student_id) — A simple class representing a team member with a name and student ID
    print_yuri() — Displays ASCII art of the character Yuri (decorative output)

utils.py — Utility Functions

This module contains all data manipulation and display logic.

Key functions:

    load_team_data() — Reads team_data.json and converts it to TeamMember objects
    display_team(people) — Prints a formatted list of all team members
    count_members(people) — Returns the total number of members
    search_member(people, name=None, student_id=None) — Finds members by exact or partial name/ID match
    add_to_team_data(people, member) — Adds a new member and writes to JSON
    write_team_data(people) — Persists team data back to JSON
    greet(name) — Prints a simple greeting message

CLI Usage
Basic Commands
Command	Description	Example
python main.py	Displays default output: greeting, team list, and ASCII art	python main.py
python main.py --show-team	Displays the team member list and exits	python main.py --show-team
python main.py --count	Shows the total number of team members	python main.py --count
python main.py --greet <name>	Greets a specific person by name	python main.py --greet Alice
Error Handling

If you provide unrecognized arguments, the program displays a friendly error message:

unrecognized arguments, rtfm (read the FRIENDLY manual)

Data File Requirement

The program requires a team_data.json file in the src/ directory. If missing, the program exits with an error message.

Expected JSON format:
json

[
    {"name": "Alice", "id": "001"},
    {"name": "Bob", "id": "002"}
]

Key Design Notes

Current limitations:

    The team name ("Team Yuri") is hardcoded in main.py with a TODO comment to move it to the JSON configuration
    The search_member() function exists in utils.py but is not exposed via CLI — it can only be called programmatically
    No input validation for adding new members to the team

Strengths:

    Clear separation between data models (team.py), utilities (utils.py), and CLI logic (main.py)
    JSON-based persistence allows easy team data management
    Flexible search function supports both exact and partial matching
