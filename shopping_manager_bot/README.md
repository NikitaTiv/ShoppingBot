# Проект ShoppingManagerBot (находится в разработке)

ShoppingManagerBot - телеграмм-бот, который помогает сформировать список покупок (продукты, хозтовары...)

## Установка

1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py` (сейчас он временно в папке settings)
5. Впишите в settings.py переменные:
```
API_KEY = 'API-ключ бота'
URL = 'Ссылка на базу данных'
USER_EMOJI = [":shit:", ":smile:", ":sunglasses:", ":eyes:"]
```
6. Запустите бота командой `python bot.py`