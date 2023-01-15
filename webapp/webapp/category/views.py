from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, logout_user
from sqlalchemy.exc import ProgrammingError

from webapp.db_functions import create_user_choice
from webapp.category.models import Category

blueprint = Blueprint('category', __name__)

@blueprint.route('/category', methods=['GET', 'POST'])
def index():
    page_title = 'Бот покупок'
    category_list = Category.query.all()
    if "marker" in request.form:
        select_category = request.form.getlist("category")
        try:
            create_user_choice(select_category, current_user.email)
            logout_user()
            flash('Ваш выбор сохранен.Вы можете вернуться к телеграм-боту.')
        except (ProgrammingError, AttributeError):
            flash('Сначала заполните форму входа.')
            return redirect(url_for('user.registration'))
    return render_template(
        'category/index.html', title=page_title, categories=category_list,
        )