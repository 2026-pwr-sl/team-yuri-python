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
   

lines = sys.stdin.readlines()

DisplayLog(lines)
data = ReadLog(lines)
ShowLargestResource(data)