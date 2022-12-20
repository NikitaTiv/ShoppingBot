from API_FNS.nalog_ru import NalogRuPython
import json
from typing import Any


def treat_check(ticket_data: dict[str, Any]) -> dict[str, Any]:
    '''Обрабатываем данные чека'''
    data_check = {}
    data_products = ticket['ticket']['document']['receipt']['items']
    select_data_check = {
        'operation': ticket['operation']['date'],
        'seller': ticket['seller'].get('name'),
        'id': ticket['id']}
    for head_check in ticket_data:
        if head_check in select_data_check:
            data_check[f'{head_check}'] = select_data_check[f'{head_check}']
        elif head_check == 'ticket':
            data_check['positions'] = treat_products(data_products)
    return data_check


def treat_products(data_product: list[dict[str, Any]]) -> list[dict[str, Any]]:
    '''Обрабатываем позиции продукта в чеке'''
    list_products = []
    selected_head_product = ['name', 'price', 'quantity', 'sum']
    for _, positions in enumerate(data_product):
        product = {}
        for head_product in positions:
            if head_product in selected_head_product:
                product[head_product] = positions[head_product]
                if head_product == 'price':
                    product[head_product] = (positions[head_product]) / 100
                elif head_product == 'sum':
                    product[head_product] = (positions[head_product]) / 100
        list_products.append(product)
    return list_products


if __name__ == '__main__':
    client = NalogRuPython()
    qr_code = \
        't=20221210T2003&s=1529.93&fn=9960440502976281&i=756&fp=2190851534&n=1'
    ticket = client.get_ticket(qr_code)
    client.refresh_token_function()
    processed_check = treat_check(ticket)
    with open('verified_check.json', 'w', encoding='utf-8') as w_file:
        w_file.write(json.dumps(processed_check, indent=4, ensure_ascii=False))
