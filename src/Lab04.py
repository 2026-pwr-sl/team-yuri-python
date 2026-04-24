
from datetime import datetime
from parser import parse_log_line


def read_log_file(filename):
    entries = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            entry = parse_log_line(line)
            entries.append(entry)

    return entries


def display_requests_between(entries, start_time, end_time):
    if end_time < start_time:
        print("Warning: end time is earlier than start time.")
        return

    for entry in entries:
        if start_time <= entry.timestamp <= end_time:
            print(entry)


if __name__ == "__main__":
    entries = read_log_file("lab04_log.txt")
    print("Loaded entries:", len(entries))

    start_time = datetime(2020, 10, 18, 1, 32, 0)
    end_time = datetime(2020, 10, 18, 1, 50, 0)

    print("Requests in range:")
    display_requests_between(entries, start_time, end_time)