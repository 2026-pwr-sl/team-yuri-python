import sys
import logging


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def DisplayLog(data):
    for item in data:
        path = item[0]
        status = item[1]

        if status == "404":
            print("!" + path)
        else:
            print(path)


def ReadLog(lines):
    result = []
    for line in lines:
        part = line.strip().split()
        result.append(part)
    return result


def ShowLargestResource(data):
    bytes_list = []
    paths = []
    processing_times = []

    for item in data:
        path = item[0]
        bytes_sent = int(item[2])
        processing_time = int(item[3])

        paths.append(path)
        bytes_list.append(bytes_sent)
        processing_times.append(processing_time)

    max_bytes = max(bytes_list)
    index = bytes_list.index(max_bytes)
    print("Largest resource:", paths[index], processing_times[index], "ms")


def CountFailed(data):
    failed = 0

    for item in data:
        status = item[1]
        if status == "404":
            failed += 1

    print("Failed requests:", failed)


def TotalBytes(data):
    total = 0

    for item in data:
        bytes_sent = int(item[2])
        total += bytes_sent

    print("Total bytes sent:", total)
    return total


def TotalKilobytes(total_bytes):
    kilobytes = total_bytes / 1024
    print("Total kilobytes sent:", kilobytes)


def AverageTime(data):
    total_time = 0

    for item in data:
        processing_time = int(item[3])
        total_time += processing_time

    avg = total_time / len(data)

    print("Average processing time:", avg, "ms")


logging.info("Start")

lines = sys.stdin.readlines()

data = ReadLog(lines)
DisplayLog(data)
ShowLargestResource(data)
CountFailed(data)
total = TotalBytes(data)
TotalKilobytes(total)
AverageTime(data)

logging.info("Finished")
