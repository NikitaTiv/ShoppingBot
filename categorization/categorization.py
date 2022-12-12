import json, io


def add_categories_to_file(input_category: io.TextIOWrapper, input_check: io.TextIOWrapper) -> None:
    with open(input_category, "r", encoding='utf-8') as read_file:
        categories = json.load(read_file)
    with open(input_check, "r", encoding='utf-8') as read_file:
        check_verified = json.load(read_file)
    for number, good in enumerate(check_verified): #нумерация и перебор словарей в чеке от Саши
        key_name = good.get("name", "пусто").replace(".", " ").replace(",", " ").replace("/", " ")
        good_as_list = key_name.lower().split()
        for category in categories:
            for word in good_as_list:
                if word in categories[category]:
                    check_verified[number]["category"] = category
    with open("verified_check_with_categories.json", "w", encoding='utf-8') as write_file:
        json.dump(check_verified, write_file, sort_keys=False, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    add_categories_to_file("category.json", "verified_check.json")