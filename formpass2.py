from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class FormPass2(FlaskForm):
    length_bigletters = IntegerField('Количество больших букв: ', validators=[DataRequired()])
    length_litletters = IntegerField('Количество маленьких букв: ', validators=[DataRequired()])
    length_number = IntegerField('Количество чисел: ', validators=[DataRequired()])

    button = SubmitField('Сгенерировать')