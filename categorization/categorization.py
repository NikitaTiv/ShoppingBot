import json_func
from typing import Union


def category_definition(input_categories: str, good: str) -> Union[str, None]:
    result_category = None
    good_without_separator = good["name"].replace(".", " ").replace(",", " ").replace("/", " ")
    good_as_list = good_without_separator.lower().split()
    for category in input_categories: 
        category_set = set(input_categories[category])
        if category_set.intersection(good_as_list):
            result_category = category
            break
    return result_category


def add_categories_to_receipt(input_categories: str, receipt: str) -> str:
    for good in receipt:
        if 'name' not in good: continue
        good["category"] = category_definition(input_categories, good)
    return receipt


if __name__ == "__main__":
    categories = json_func.read("categories.json")
    input_receipt = json_func.read("verified_receipt.json")
    str_with_categories = add_categories_to_receipt(categories, input_receipt)
    json_func.write("verified_receipt_with_categories.json", str_with_categories)