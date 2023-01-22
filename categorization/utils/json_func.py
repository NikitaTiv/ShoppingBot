import json


def read(input_filepath: str) -> dict:
    with open(input_filepath, "r", encoding='utf-8') as read_file:
        return json.load(read_file)


if __name__ == "__main__":
    read("verified_receipt.json")
