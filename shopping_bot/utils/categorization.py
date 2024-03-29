def define_category(categories_corpus: dict, good: dict) -> str | None:
    result_category = None
    good_without_separator = good["name"].replace(".", " ").replace(",", " ").replace("/", " ")
    good_as_list = good_without_separator.lower().split()
    for category_name, category_words in categories_corpus.items(): 
        category_set = set(category_words)
        if category_set.intersection(good_as_list):
            result_category = category_name
            break
    return result_category


def add_categories_to_receipt(categories_corpus: dict, receipt: dict) -> dict:
    for good in receipt["positions"]:
        good["category"] = define_category(categories_corpus, good)
    return receipt
