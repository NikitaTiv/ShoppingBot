import sys
sys.path.append("../utils/")
import json_func


def define_category(input_categories: dict, good: dict) -> str | None:
    result_category = None
    good_without_separator = good["name"].replace(".", " ").replace(",", " ").replace("/", " ")
    good_as_list = good_without_separator.lower().split()
    tuple_categories = input_categories.items() 
    for category in tuple_categories: 
        category_set = set(category[1])
        if category_set.intersection(good_as_list):
            result_category = category[0]
            break
    return result_category


def add_categories_to_receipt(input_categories: dict, receipt: list) -> list:
    for good in receipt:
        if 'name' not in good: 
            continue
        good["category"] = define_category(input_categories, good)
    return receipt


if __name__ == "__main__":
    categories = json_func.read("categories.json")
    input_receipt = json_func.read("verified_receipt.json")
    str_with_categories = add_categories_to_receipt(categories, input_receipt)
    json_func.write("verified_receipt_with_categories.json", str_with_categories)