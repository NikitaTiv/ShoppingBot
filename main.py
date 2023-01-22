from database_with_categories.db import Base, engine
from database_with_categories.CRUD import add_user, add_receipt,\
    add_category, add_triggers, add_receipt_content
from processing_qr_code import receipt
from categorization import categorization
from categorization.utils import json_func


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    receipt_new = {
    "id": "6394db6d0f8402fef53d36c1",
    "operation": {
        "date": "2022-12-10T20:03"
    },
    "ticket": {
        "document": {
            "receipt": {
                "items": [
                    {
                        "name": "1*: 78032688 СПз Берлинер мал.нач/глазур",
                        "price": 5900,
                        "quantity": 1,
                        "sum": 5900
                    },
                    {
                        "name": "2*: 78032687 СПз Берлинер нач.вк.Ман/гл.",
                        "price": 5900,
                        "quantity": 1,
                        "sum": 5900
                    },
                    {
                        "name": "3: 3014975 КАРАТ Профитроли ванильные 24",
                        "price": 19999,
                        "quantity": 1,
                        "sum": 19999
                    },
                    {
                        "name": "4*: 4010834 OLEA Мыло URBAN жидкое 500мл",
                        "price": 11499,
                        "quantity": 1,
                        "sum": 11499
                    },
                    {
                        "name": "5*: 3965705 BUSH.Кофе SENSEI мол.227г",
                        "price": 42999,
                        "quantity": 1,
                        "sum": 42999
                    },
                    {
                        "name": "6: 3267348 АРНАУТ Ватруш.дом.твор.изюм20",
                        "price": 8199,
                        "quantity": 1,
                        "sum": 8199
                    },
                    {
                        "name": "7: 3257514 КАРАВ.Ватрушка Твор.наслаж.22",
                        "price": 13999,
                        "quantity": 1,
                        "sum": 13999
                    },
                    {
                        "name": "8: 4241068 ПАМП.Печ.БЕЛЛ.нач.вк.Йог/М.65",
                        "price": 29999,
                        "quantity": 1,
                        "sum": 29999
                    },
                    {
                        "name": "9*: 4088955 МАРК.ПЕР.Яйца кур.стол.С1 20",
                        "price": 14499,
                        "quantity": 1,
                        "sum": 14499
                    }
                ],
            }
        }
    },
    "seller": {
        "name": "АО ТД Перекресток",
    }
}
    last_user_id = add_user('Александр')
    processed_check = receipt.treat_receipt(receipt_new)
    last_receipt_id = add_receipt(processed_check['seller'], last_user_id)
    list_of_ids = add_category(json_func.read('categories.json'))
    add_triggers(json_func.read('categories.json'), list_of_ids)
    add_receipt_content(categorization.add_categories_to_receipt
                        (processed_check)['positions'], last_receipt_id)
