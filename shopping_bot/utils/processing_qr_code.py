import json
from typing import Any

from utils.categorization import add_categories_to_receipt
import utils.json_func


def treat_receipt(data: dict[str, Any]) -> dict[str, Any]:
    """Обрабатываем данные чека."""
    data_receipt = {}
    data_products = data['ticket']['document']['receipt']['items']
    select_data_receipt = {
        'operation': data['operation']['date'],
        'seller': data['seller'].get('name'),
        'id': data['id'],
    }
    for head_receipt in data:
        if head_receipt in select_data_receipt:
            data_receipt[f'{head_receipt}'] = select_data_receipt[f'{head_receipt}']
        elif head_receipt == 'ticket':
            data_receipt['positions'] = treat_products(data_products)
    return data_receipt


def treat_products(data_product: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Обрабатываем позиции продукта в чеке."""
    list_products = []
    for positions in data_product:
        product = {}
        product['name'] = positions['name']
        product['price'] = positions['price'] / 100
        product['quantity'] = positions['quantity']
        product['sum'] = positions['sum'] / 100
        list_products.append(product)
    return list_products


def treat_string_for_nalog(receipt: dict[Any, Any]) -> None:
    """
    Сравнивает категории в чеке со списком категорий продуктов,
    приваивая каждой позиции соответствующую категорию.
    """
    processed_receipt = treat_receipt(receipt)
    with open('verified_receipt.json', 'w', encoding='utf-8') as w_file:
        w_file.write(json.dumps(processed_receipt, indent=4, ensure_ascii=False))
    categories = utils.json_func.read('categories.ini')
    input_receipt = utils.json_func.read('verified_receipt.json')
    receipt_with_categories = add_categories_to_receipt(categories, input_receipt)
    utils.json_func.write('verified_receipt_with_categories.json', receipt_with_categories)
