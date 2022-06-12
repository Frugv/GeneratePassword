from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class FormPass1(FlaskForm):
    length_Specsimbol = IntegerField('Количество спецсимволов: ', validators=[DataRequired()])
    length_Bigletters = IntegerField('Количество больших букв: ', validators=[DataRequired()])
    length_Litletters = IntegerField('Количество маленьких букв: ', validators=[DataRequired()])
    length_Number = IntegerField('Количество чисел: ', validators=[DataRequired()])

    button = SubmitField('Сгенерировать')