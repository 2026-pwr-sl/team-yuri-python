from datetime import datetime
from log_entry import LogEntry


def parse_timestamp(timestamp_str):
    month_names = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }

    parts = timestamp_str.split(":")
    date_part = parts[0]
    hour = parts[1]
    minute = parts[2]
    second = parts[3]

    date_parts = date_part.split("/")
    day = int(date_parts[0])
    month_str = date_parts[1]
    year = int(date_parts[2])

    month = month_names[month_str]

    return datetime(year, month, day, int(hour), int(minute), int(second))


def parse_log_line(line):
    parts = line.split('"')

    left_part = parts[0].strip()
    request_part = parts[1].strip()
    right_part = parts[2].strip()

    left_parts = left_part.split()
    ip_address = left_parts[0]

    timestamp_str = left_parts[3]
    timestamp_str = timestamp_str[1:-1]   # remove [

    timestamp = parse_timestamp(timestamp_str)

    request_parts = request_part.split()
    method = request_parts[0]
    path = request_parts[1]
    protocol = request_parts[2]

    right_parts = right_part.split()
    status_code = int(right_parts[0])
    bytes_sent = int(right_parts[1])

    return LogEntry(ip_address, timestamp, method, path, protocol, status_code, bytes_sent)