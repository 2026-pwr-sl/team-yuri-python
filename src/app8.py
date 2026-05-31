import sys
import os
import csv


def validate_file(filename):

    # csv extension check
    if not filename.endswith(".csv"):
        print("ERROR: File must be CSV")
        sys.exit(1)

    # file exists check
    if not os.path.exists(filename):
        print("ERROR: File not found")
        sys.exit(1)


def read_dataset(filename):

    data = []

    with open(filename, mode="r", encoding="utf-8") as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            data.append(row)

    return data


def main():

    # argument check
    if len(sys.argv) < 2:
        print("Usage: python app8.py dataset.csv")
        sys.exit(1)

    filename = sys.argv[1]

    validate_file(filename)

    dataset = read_dataset(filename)

    print("Dataset is valid!")
    print(f"Loaded {len(dataset)} rows")


if __name__ == "__main__":
    main()
