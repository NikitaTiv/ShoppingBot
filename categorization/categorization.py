import json, io


def read_from_json(input_file: io.TextIOWrapper) -> str:
    with open(input_file, "r", encoding='utf-8') as read_file:
        return json.load(read_file)


def write_to_json(output_file: str, data_to_write: str) -> None:
    with open(output_file, "w", encoding='utf-8') as write_file:
        json.dump(data_to_write, write_file, sort_keys=False, indent=4, ensure_ascii=False)


def add_categories_to_file(input_categories: str, check: str) -> str:
    for number, good in enumerate(check):
        if "name" in good:
            result_category = "не определена"
            key_name = good["name"].replace(".", " ").replace(",", " ").replace("/", " ")
            good_as_list = key_name.lower().split()
            for category in input_categories: 
                for word in good_as_list:
                    if word in input_categories[category]:
                        result_category = category
                        break
            check[number]["category"] = result_category
    return check


if __name__ == "__main__":
    categories = read_from_json("categories.json")
    input_check = read_from_json("verified_check.json")
    str_with_categories = add_categories_to_file(categories, input_check)
    write_to_json("verified_check_with_categories.json", str_with_categories)