import logging
import sys

log_level_name = "INFO"

if len(sys.argv) > 1:
    log_level_name = sys.argv[1].upper()

log_level = getattr(logging, log_level_name, logging.INFO)
logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")


def display_log(data):
    logging.debug("Displaying %d log entries", len(data))
    for item in data:
        path = item[0]
        status = item[1]
        if status == 404:
            print("!" + path)
        else:
            print(path)

def read_log():
    lines = sys.stdin.readlines()
    logging.debug("Read %d lines from standard input", len(lines))

    result = []

    for line in lines:
        if line.strip() == "":
            continue

        parts = line.strip().split()

        path = parts[0]
        status_code = int(parts[1])
        bytes_sent = int(parts[2])
        processing_time = int(parts[3])

        entry = (path, status_code, bytes_sent, processing_time)
        result.append(entry)

    logging.debug("Created %d log entries", len(result))
    return result


def successful_reads(data):
    result = []

    for entry in data:
        status_code = entry[1]
        if 200 <= status_code < 300:
            result.append(entry)

    logging.info("Successful reads count: %d", len(result))
    return result



def show_largest_resource(data):
    bytes_list = []
    paths = []
    processing_times = []
    for item in data:
        path = item[0]
        bytes_sent = item[2]
        processing_time = item[3]

        paths.append(path)
        bytes_list.append(bytes_sent)
        processing_times.append(processing_time)

        logging.debug(
            "Largest resource candidate -> path=%s bytes=%d time=%d",
            path,
            bytes_sent,
            processing_time,
        )
    max_bytes = max(bytes_list)
    index = bytes_list.index(max_bytes)
    logging.debug("Largest resource index: %d", index)
    print("Largest resource:", paths[index], processing_times[index], "ms")


def count_failed(data):
    failed = 0
    for item in data:
        status = item[1]
        if status == 404:
            failed += 1
            logging.debug("Failed request found: %s", item[0])
    print("Failed requests:", failed)


def total_bytes(data):
    total = 0
    for item in data:
        bytes_sent = item[2]
        total += bytes_sent
        logging.debug("Added %d bytes, total now %d", bytes_sent, total)
    print("Total bytes sent:", total)
    return total


def total_kilobytes(total_bytes):
    kilobytes = total_bytes / 1000  # 1000 for KB, 1024 for KiB
    logging.debug("Converted %d bytes to %f KB", total_bytes, kilobytes)
    print("Total kilobytes sent:", kilobytes)


def average_time(data):
    total_time = 0
    for item in data:
        processing_time = int(item[3])
        total_time += processing_time
        logging.debug("Added %d ms, total time now %d", processing_time, total_time)
    avg = total_time / len(data)
    logging.debug("Average processing time: %f", avg)
    print("Average processing time:", avg, "ms")

def run():
    logging.info("Start")
    logging.info("Logging level: %s", log_level_name)

    data = read_log()

    display_log(data)
    show_largest_resource(data)
    count_failed(data)
    total_kilobytes(total_bytes(data))
    average_time(data)

    success_data = successful_reads(data)
    failed_data = failed_read(data)
    html_data = html_entry(data)
    logging.debug("Successful entries: %s", success_data)
    logging.debug("Failed reads: %s", failed_data)
    logging.debug("HTML entries: %s", html_data)


    logging.info("Finished")

def failed_read(data):
    list4xx = []
    list5xx = []

    for entry in data:
        status_code = entry[1]
        if 400 <= status_code < 500:
            list4xx.append(entry)
        elif 500 <= status_code < 600:
            list5xx.append(entry)
    logging.info("4xx errors count: %d", len(list4xx))
    logging.info("5xx errors count: %d", len(list5xx))

    return list4xx + list5xx


def html_entry(data):
    result = []

    for entry in data:
        path = entry[0]
        status_code = entry[1]
        if path.endswith(".html") and 200 <= status_code < 300:
            result.append(entry)
    return result


if __name__ == "__main__":
    run()
