from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()], render_kw={'class': 'form-control'})
    last_name = StringField('Фамилия', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})
