import json
import logging
import os


default_config = {
    "log_file" : os.path.join('src', "lab04_log.txt"),
    "ip_address" : "127.0.0.1",
    "logging_level" : "INFO",
    "lines" : 4,
    "method" : "GET"
}


try:
    with open("config.json", "r", encoding = "utf-8") as file:
        config = json.load(file)
except FileNotFoundError:
    logging.info("File not found!")
    config = default_config

except json.JSONDecodeError:
    logging.error("JSON decode error")
    exit()


try:
    logging_level = config["logging_level"]
except KeyError:
    logging.info("Missing logging level, using default...")
    logging_level = default_config["logging_level"]


try:
    lines = config["lines"]
except KeyError:
    logging.info("Missing lines, using default...")
    lines = default_config["lines"]


try:
    log_file = config["log_file"]
except KeyError:
    logging.info("missing log file")
    log_file = default_config["log_file"]


try:
    ip_address = config["ip_address"]
except KeyError:
    logging.info("Missing IP address, setting default...")
    ip_address = default_config["ip_address"]


try:
    method = config["method"]
except KeyError:
    logging.info("Wrong method used, using default...")
    method = default_config["method"]


config["logging_level"] = logging_level
config["lines"] = lines
config["log_file"] = log_file
config["ip_address"] = ip_address
config["method"] = method


with open("config.json", "w", encoding="utf-8") as file:
    json.dump(config, file, indent=4)



log_level = getattr(logging, str(logging_level).upper(), logging.INFO)

logging.basicConfig(
    level=log_level,
    format="%(levelname)s: %(message)s"
)

logging.info("Logging level set to %s", logging.getLevelName(log_level))

# helps detect invalid line values during debugging
assert lines > 0, "lines must be greater than 0"


def read_log(filename):
    log_dict = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.split()

                ip = parts[0]
                method = parts[4].replace('"', "")
                path = parts[5]
                request = method + " " + path
                status = int(parts[7])

                entry = {"request": request, "status": status}

                if ip not in log_dict:
                    log_dict[ip] = []

                log_dict[ip].append(entry)

    except FileNotFoundError:
        logging.error("Log file does not exist: %s", filename)
        print("Error: log file '" + filename + "' does not exist.")
        print("Please check the log_file value in config.json.")
        exit()

    return log_dict


def ip_request_number(ip_address, data):
    if ip_address in data:
        return len(data[ip_address])



def print_requests_from_ip(ip_address, data):
    logging.info("Printing requests from IP address: %s", ip_address)

    if ip_address not in data:
        print("No requests found from", ip_address)
        return

    print("Requests from", ip_address + ":")

    for entry in data[ip_address]:
        print(entry["request"], "status:", entry["status"])


def ip_find(data, most_active=True):
    count = {}
    for ip in data:
        count[ip] = len(data[ip])

    if most_active:
        value = max(count.values())
    else:
        value = min(count.values())

    result = []
    for ip in count:
        if count[ip] == value:
            result.append(ip)
    return result


def longest_request(data):
    longest = ""
    longest_ip = ""

    for ip in data:
        for entry in data[ip]:
            request = entry["request"]

            if len(request) > len(longest):
                longest = request
                longest_ip = ip

    return longest_ip, longest


def non_existent(data):
    result = []

    for ip in data:
        for entry in data[ip]:
            if entry["status"] == 404:
                request = entry["request"]

                if request not in result:
                    result.append(request)

    return result

def print_requests_by_method(data, method, lines):
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    print('\nfiltering requests by method...')
    count = 0
    for ip in data:
        for entry in data[ip]:
            request = entry["request"]
            if request.startswith(method):
                print(ip, request, "status:", entry["status"])
                count += 1
                if count % lines == 0:
                    input("Press Enter to continue...")
                    clear()

def run():
    data = read_log(log_file)

    print("Requests from", ip_address + ":", len(data.get(ip_address, [])))
    print_requests_from_ip(ip_address, data)

    MostActiveIP = ip_find(data)
    LeastActiveIP = ip_find(data, False)

    print("Most active IPs:")
    for ip in MostActiveIP:
        print(ip)

    print("Least active IPs:")
    for ip in LeastActiveIP:
        print(ip)

    longest_ip, request = longest_request(data)
    print("Longest request:")
    print(longest_ip, request)

    print("Non-existent resources:")
    for request in non_existent(data):
        print(request)
    print_requests_by_method(data, method, lines)

if __name__ == "__main__":
    run()
