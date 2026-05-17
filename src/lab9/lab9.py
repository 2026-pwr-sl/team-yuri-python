from dataclasses import dataclass
import ipaddress
import logging
import os
import re
import sys


DEFAULT_DISPLAY_SETTINGS = {
    "lines_per_page": "10",
    "separator": ":",
    "browser": "Firefox",
}

DEFAULT_LOG_FILENAME = "log_timestamped.txt"

DEFAULT_CONFIG_SETTINGS = {
    "log_level": "INFO",
    "log_file": "processing_log.txt",
    "log_format": "%(asctime)s - %(levelname)s - %(message)s",
}

DEFAULT_FILTER_SETTINGS = {
    "request_type": "GET",
}

STUDENT_INDEX = 224538
SUBNET_IP = "185.23.0.0"

@dataclass
class LogEntry:
    """Single parsed log entry."""
    ip_address: str
    timestamp: str
    request_header: str
    status_code: int
    response_size: int
    browser: str

def configure_logging(config_settings):
    """Configure application logging based on config settings."""
    log_level_name = config_settings.get("log_level", "INFO")
    log_file = config_settings.get("log_file", "processing_log.txt")
    log_format = config_settings.get(
        "log_format",
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    log_level = getattr(logging, log_level_name.upper(), logging.INFO)

    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format=log_format
    )


def read_config(config_path):
    """Read configuration file using regular expressions."""
    if not os.path.exists(config_path):
        print(f"Config file '{config_path}' not found. Exiting.")
        sys.exit(1)

    display_settings = DEFAULT_DISPLAY_SETTINGS.copy()
    config_settings = DEFAULT_CONFIG_SETTINGS.copy()
    filter_settings = DEFAULT_FILTER_SETTINGS.copy()
    log_filename = DEFAULT_LOG_FILENAME

    current_section = None

    section_regex = re.compile(r"^\s*\[([A-Za-z]+)\]\s*$")
    parameter_regex = re.compile(r"^\s*([^=]+?)\s*=\s*(.*?)\s*$")

    with open(config_path, "r", encoding="utf-8") as config_file:
        for line_number, line in enumerate(config_file, start=1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            section_match = section_regex.match(line)
            if section_match:
                current_section = section_match.group(1)
                continue

            parameter_match = parameter_regex.match(line)
            if parameter_match:
                key = parameter_match.group(1).strip()
                value = parameter_match.group(2).strip()

                if current_section == "Display":
                    display_settings[key] = value
                elif current_section == "LogFile":
                    if key == "filename":
                        log_filename = value
                elif current_section == "Config":
                    config_settings[key] = value
                elif current_section == "Filter":
                    filter_settings[key] = value
                else:
                    logging.warning(
                        "Unknown section at line %s: %s",
                        line_number,
                        current_section
                    )
            else:
                logging.warning("Invalid config line %s: %s", line_number, line)

    configure_logging(config_settings)

    return display_settings, log_filename, filter_settings

def read_log_file(log_filename):
    """Read log file content into memory."""
    if not os.path.exists(log_filename):
        print(f"Log file '{log_filename}' not found. Exiting.")
        sys.exit(1)

    with open(log_filename, "r", encoding="utf-8") as log_file:
        log_lines = log_file.readlines()

    return log_lines

def parse_log_line(line):
    """Parse a single log line using regular expressions."""
    
    log_regex = re.compile(
        r"^(\d{1,3}(?:\.\d{1,3}){3}) "
        r"- - "
        r"\[([^\]]+)\] "
        r'"([^"]+)" '
        r"(\d{3}) "
        r"(\d+) "
        r'"([^"]+)"$'
    )

    match = log_regex.match(line.strip())

    if not match:
        logging.warning("Could not parse log line: %s", line.strip())
        return None

    ip_address = match.group(1)
    timestamp = match.group(2)
    request_header = match.group(3)
    status_code = int(match.group(4))
    response_size = int(match.group(5))
    browser = match.group(6)

    return LogEntry(
        ip_address=ip_address,
        timestamp=timestamp,
        request_header=request_header,
        status_code=status_code,
        response_size=response_size,
        browser=browser
    )

def parse_all_log_lines(log_lines):
    """Parse all log lines and return a list of LogEntry objects."""
    log_entries = []

    for line in log_lines:
        entry = parse_log_line(line)

        if entry is not None:
            log_entries.append(entry)

    return log_entries

def get_mask_length(student_index):
    """Calculate IP mask length from student index."""
    return student_index % 16 + 8


def ip_belongs_to_subnet(ip_address, subnet_ip, mask_length):
    """Check if an IP address belongs to a subnet."""
    subnet = ipaddress.ip_network(f"{subnet_ip}/{mask_length}", strict=False)
    ip = ipaddress.ip_address(ip_address)

    return ip in subnet


def print_requests_from_subnet(log_entries, display_settings):
    """Print requests sent from the chosen IP subnet."""
    mask_length = get_mask_length(STUDENT_INDEX)
    lines_per_page = int(display_settings.get("lines_per_page", 10))

    print(f"Chosen subnet: {SUBNET_IP}/{mask_length}")
    print("Requests from this subnet:")

    displayed_count = 0
    matched_count = 0

    for entry in log_entries:
        if ip_belongs_to_subnet(entry.ip_address, SUBNET_IP, mask_length):
            print(entry)
            displayed_count += 1
            matched_count += 1

            if displayed_count == lines_per_page:
                input("Press Enter to display more...")
                displayed_count = 0

    print(f"Total matching requests: {matched_count}")


def print_requests_from_browser(log_entries, display_settings):

    browser_name = display_settings.get("browser", "Firefox")

    pattern = re.compile(browser_name, re.IGNORECASE)

    print(f"Requests from browser: {browser_name}")

    for entry in log_entries:

        if pattern.search(entry.browser):

            print(entry)


def print_total_bytes_by_request_type(log_entries, filter_settings, display_settings):

    request_type = filter_settings.get("request_type", "GET")

    separator = display_settings.get("separator", "|")

    total_bytes = 0

    request_regex = re.compile(
        r"^(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS|CONNECT)"
    )

    for entry in log_entries:

        match = request_regex.search(entry.request_header)

        if match:

            current_request_type = match.group(1)

            if current_request_type == request_type:

                total_bytes += entry.response_size

    print(f"{request_type}{separator}{total_bytes}")


def main():
    display_settings, log_filename, filter_settings = read_config("9.config")

    print("Config loaded successfully.")
    print(f"Display settings: {display_settings}")
    print(f"Log filename: {log_filename}")
    print(f"Filter settings: {filter_settings}")

    log_lines = read_log_file(log_filename)

    print("Log file loaded successfully.")
    print(f"Number of raw lines loaded: {len(log_lines)}")

    log_entries = parse_all_log_lines(log_lines)

    print("All log lines parsed.")
    print(f"Number of parsed log entries: {len(log_entries)}")

    print_requests_from_subnet(log_entries, display_settings)

    logging.info("Subnet filtering completed successfully.")


    print_total_bytes_by_request_type(log_entries,filter_settings,display_settings)
    print_requests_from_browser(log_entries, display_settings)

if __name__ == "__main__":
    main()