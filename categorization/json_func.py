import json


def read(input_file: str) -> str:
    with open(input_file, "r", encoding='utf-8') as read_file:
        return json.load(read_file)


def write(output_file: str, data_to_write: str) -> None:
    with open(output_file, "w", encoding='utf-8') as write_file:
        json.dump(data_to_write, write_file, sort_keys=False, indent=4, ensure_ascii=False)