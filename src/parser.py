from datetime import datetime


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
