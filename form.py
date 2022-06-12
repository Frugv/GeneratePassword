from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    nameSN = StringField('Название соц.сети: ', validators=[DataRequired()])
    loginSN = StringField('Логин соц.сети: ', validators=[DataRequired()])
    length_password = IntegerField('Длина пароля: ', validators=[DataRequired()])
    button = SubmitField('Сгенерировать')