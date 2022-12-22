from API_FNS.nalog_ru import NalogRuPython
import json
from typing import Any


def treat_receipt(data: dict[str, Any]) -> dict[str, Any]:
    """Обрабатываем данные чека"""
    data_receipt = {}
    data_products = data['ticket']['document']['receipt']['items']
    select_data_receipt = {
        'operation': data['operation']['date'],
        'seller': data['seller'].get('name'),
        'id': data['id']
    }
    for head_receipt in data:
        if head_receipt in select_data_receipt:
            data_receipt[f'{head_receipt}'] = select_data_receipt[f'{head_receipt}']
        elif head_receipt == 'ticket':
            data_receipt['positions'] = treat_products(data_products)
    return data_receipt


def treat_products(data_product: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Обрабатываем позиции продукта в чеке"""
    list_products = []
    for positions in data_product:
        product = {}
        product['name'] = positions['name']
        product['price'] = positions['price'] / 100
        product['quantity'] = positions['quantity']
        product['sum'] = positions['sum'] / 100
        list_products.append(product)
    return list_products


if __name__ == '__main__':
    client = NalogRuPython()
    qr_code = \
        't=20221210T2003&s=1529.93&fn=9960440502976281&i=756&fp=2190851534&n=1'
    receipt = client.get_ticket(qr_code)
    client.refresh_token_function()
    processed_receipt = treat_receipt(receipt)
    with open('verified_receipt.json', 'w', encoding='utf-8') as w_file:
        w_file.write(json.dumps(processed_receipt, indent=4, ensure_ascii=False))
