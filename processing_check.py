import json
from nalog_ru import NalogRuPython


def get_processed_list(processed_data: dict) -> list: 
    list_of_dicts = []
    right_keys = ['name', 'price', 'quantity', 'sum']
    date_purchase = ticket['operation']['date']
    list_items = ticket['ticket']['document']['receipt']['items']
    seller = ticket['seller']['name']
    for key in ticket:
        sort_dict = {}
        if key == 'operation':
            sort_dict['date'] = date_purchase.replace('T', ' ').replace('-', '.')
            list_of_dicts.append(sort_dict)
        elif key == 'ticket':
            count_dict = 0
            for dict_items in list_items:
                sort_dict = {}
                for key_row in dict_items:
                    if key_row in right_keys:
                        sort_dict[key_row] = list_items[count_dict][key_row]
                        if key_row == 'sum' or key_row == 'price':
                            sort_dict[key_row] = sort_dict[key_row] / 100
                list_of_dicts.append(sort_dict)
                count_dict += 1
        elif key == 'seller':
            sort_dict['seller'] = seller
            if sort_dict['seller'].count('Лента'):
                sort_dict['seller'] = sort_dict['seller'].lstrip().replace('\"', '')
            list_of_dicts.append(sort_dict)
    return list_of_dicts


if __name__ == '__main__':
    client = NalogRuPython()
    qr_code = "t=20221210T2003&s=1529.93&fn=9960440502976281&i=756&fp=2190851534&n=1"
    ticket = client.get_ticket(qr_code)
    process_list = get_processed_list(ticket)
    with open('verified_check.json', 'w', encoding='utf-8') as write_file:
        write_file.write(json.dumps(process_list, indent=4, ensure_ascii=False))
