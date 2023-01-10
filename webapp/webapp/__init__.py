from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_user

from webapp.db_functions import save_user
from webapp.forms import UserForm
from webapp.model import db, Category,User

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/category')
    def index():
        page_title = 'Бот покупок'
        category_list = Category.query.all()
        return render_template(
            'index.html', title=page_title, categories=category_list,
            )

    @app.route('/')
    def login():
        login_form = UserForm()
        return render_template('login.html', form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = UserForm()

        if form.validate_on_submit:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            save_user(first_name,last_name)
            return redirect(url_for('index'))

    return app
