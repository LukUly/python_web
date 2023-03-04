# Подробнее об этом в уроке wtf. Здесь создается форма для регистрации
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired


# Как и в PyQt наследуемся от формы
class RegisterForm(FlaskForm):
    # Создаем поле для ввода email - для него есть специальный тип EmailField, который проверяет, что введен именно email, а не номер телефона или тарабарщина
    email = EmailField('Login / email', validators=[DataRequired()])
    # Специальное поле для пароля. Все, что введен - будет отоюражаться звездочками
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    # Обычные поля для ввода текста
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    # Кнопка
    submit = SubmitField('Submit')
