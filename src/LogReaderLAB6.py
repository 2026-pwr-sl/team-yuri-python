def read_log(filename):
    log_dict = {}

    with open(filename, "r") as file:
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

    return log_dict


def ip_request_number(ip_address, data):
    if ip_address in data:
        return len(data(ip_address))


def ip_find(data, most_active=True):
    count = {}
    for ip in data:
        count[ip] = len(data[ip])

    if most_active:
        value = max(count.values())
    if not most_active:
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


def run():
    data = read_log("lab04_log.txt")

    example_ip = "192.168.1.10"
    print("Requests from", example_ip + ":", len(data.get(example_ip, [])))

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


if __name__ == "__main__":
    run()
