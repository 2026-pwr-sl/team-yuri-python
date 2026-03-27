import sys


def DisplayLog(lines):
   
   for line in lines:
      print(line.strip())
   

def ReadLog(lines):
    result = []
    for line in lines:
     part = line.strip().split()
     result.append(part)
    return result


def ShowLargestResource(data):
    bytes_list = []
    paths = []
    times = []

    for item in data:
         path = item[0]
         bytes_sent = int(item[2])
         time = int(item[3])

         paths.append(path)
         bytes_list.append(bytes_sent)
         times.append(time)
    max_bytes = max(bytes_list)
    index = bytes_list.index(max_bytes)
    print("Largest:", paths[index], times[index])



def CountFailed(data):
    failed = 0

    for item in data:
        status = int(item[1])
        if status != 200:
            failed += 1

    print("Failed:", failed)


def TotalBytes(data):
    total = 0

    for item in data:
        bytes_sent = int(item[2])
        total += bytes_sent

    print("Total bytes:", total)


def AverageTime(data):
    total_time = 0

    for item in data:
        time = int(item[3])
        total_time += time

    avg = total_time / len(data)

    print("Average time:", avg)
   

lines = sys.stdin.readlines()

DisplayLog(lines)
data = ReadLog(lines)
ShowLargestResource(data)
CountFailed(data)
