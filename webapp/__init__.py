from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        page_title = 'Бот покупок'
        category_list =[
            "Алкоголь", "Мясо", "Сладкое (вода в т.ч.)", "Овощи",
            "Хлеб(пицца...)", "Молочка", "Хоз. товары", "Фрукты",
            "Чипсы, орехи, попкорн и проч.", "Безалк. напитки (включая воду)",
            "Чай/кофе", "Соусы", "Сыр/колбаса", "Салаты", "Рыба",
        ]
        return render_template(
            'index.html', title=page_title, categories=category_list,
            )

    return app