import json


def ConfigParam():
    config = {}

    config["log_file"] = input("Insert file name: ")
    config["ip_address"] = input("Insert IP address: ")
    config["logging_level"] = input("Logging level of application: ")
    try:
        config["lines"] = int(input("Number of Lines: "))
    except ValueError:
        print("Invalid number. Using default value 4.")
        config["lines"] = 4
    config["method"] = input("HTTP method: ")


    with open("config.json", "w", encoding="utf-8") as file:
     json.dump(config, file, indent=4)
    print("configuration saved.")

if __name__ == "__main__":
   ConfigParam()