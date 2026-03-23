class TeamMember:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


people = [
    TeamMember("Berke Mamal", 1),
    TeamMember("Metin Kaan Kulga", 2),
    TeamMember("Elif Karakas", 3),
    TeamMember("Urban Porocnik", 4),
]


def print_yuri():
    print(
        """
        YURI
/--------------------\\
|⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⡀⠀⠀⠀⠀⠀⠀⠀|
|⠀⠀⠀⠀⡀⣐⣤⢷⣲⣟⡿⣶⢾⡴⡠⡀⠀⠀⠀⠀|
|⠀⠀⢀⣪⣼⣻⢞⣯⢷⣫⡽⣞⣯⣽⣻⣬⡀⠀⠀⠀|
|⠀⣀⠀⠨⡗⠯⣟⡾⣏⣷⣻⡽⢾⣵⢻⣾⣛⣠⠀⠀|
|⠐⣠⣀⠳⠀⠘⡀⡐⠠⠬⣡⣙⣫⣶⣟⣷⣻⡇⠀⠀|
|⠈⣿⣟⡿⡛⠿⠸⡿⣿⡏⠙⠿⣽⣞⣯⢿⣿⡇⠀⠀|
|⠘⠛⣽⢾⣇⣤⡤⠙⠷⢳⠀⣤⡬⢙⡾⣯⣿⢹⠀⠀|
|⠀⠘⠋⢫⣇⠃⠑⠀⠀⠈⠂⠀⠛⢨⢿⣽⡟⡄⠀⠀|
|⠀⠀⠈⡿⣿⡇⡀⠀⠀⠀⠀⠀⣀⣿⣻⣾⡇⠁⠀⠀|
|⠀⠀⢀⢳⣯⣟⣿⡿⢿⠍⢻⣿⣿⣟⣷⢿⣇⢆⠀⠀|
|⢀⢀⣴⣟⣾⣽⣾⣿⢻⣉⣬⣿⣿⣿⣾⣟⣾⣷⣄⠀|
|⠀⢾⣿⣾⣿⣿⣿⣦⣿⣴⡾⣿⣿⣿⣿⣿⣾⣿⣿⠆|
|⠀⡋⢿⣿⡿⣿⡿⡟⠿⠚⣿⣿⣿⡟⣿⠟⣿⠿⡛⠃|
|⠀⠀⠈⠘⠁⠪⠱⡉⠀⠀⠤⠵⠙⠈⠓⠀⠀⠉⠀⠀|
|⠀⠀⠀⠀⠀⠀⠀⠀⣚⠦⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀|
\\--------------------/
    """.strip("\n")
    )
