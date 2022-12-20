from utils import json_func
from typing import Any


def define_category(input_categories: dict, good: dict) -> str | None:
    result_category = None
    good_without_separator = good["name"].replace(".", " ").replace(",", " ").replace("/", " ")
    good_as_list = good_without_separator.lower().split()
    for category_name, category_words in input_categories.items(): 
        category_set = set(category_words)
        if category_set.intersection(good_as_list):
            result_category = category_name
            break
    return result_category


def add_categories_to_receipt(input_categories: dict, receipt: dict) -> dict:
    for good in receipt["positions"]:
        good["category"] = define_category(input_categories, good)
    return receipt


if __name__ == "__main__":
    categories = json_func.read("categories.json")
    input_receipt = json_func.read("verified_receipt.json")
    receipt_with_categories = add_categories_to_receipt(categories, input_receipt)
    json_func.write("verified_receipt_with_categories.json", receipt_with_categories)