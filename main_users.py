from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    # проверяем, первый раз ли коннектимся к БД db/mars_explorer.db
    db_session.global_init("db/mars_explorer.db")
    # Открываем сессию, чтобы можно было брать данные из БД или изменять их
    session = db_session.create_session()

    # Создаем новую строчку (нового пользователя
    # 1
    capitan = User()
    # Заполняем все ее характеристики (столбцы из БД)
    capitan.surname = "Scott"
    capitan.name = "Ridley"
    capitan.age = 21
    capitan.position = "captain"
    capitan.speciality = "research engineer"
    capitan.address = "module_1"
    capitan.email = "scott_chief@mars.org"
    # Это конкретно пароль пользователя, который он вводит при регистрации
    capitan.hashed_password = "cap"
    # Этот метод преобразует введенный ранее пароль в шифрованный вид и запишет его в переменную hashed_password
    capitan.set_password(capitan.hashed_password)
    # Говорим сессии, что будем добавлять эту строку в БД
    session.add(capitan)

    # Аналогично добавляем еще несколько пользователей
    # 2
    user = User()
    user.surname = "Поваляев"
    user.name = "Дмитрий"
    user.age = 15
    user.position = "научный сотрудник"
    user.speciality = "геолог"
    user.address = "module_1"
    user.email = "dmitrij.povalyaev@mail.ru"
    user.hashed_password = "sci"
    user.set_password(user.hashed_password)
    session.add(user)

    # 3
    user = User()
    user.surname = "Савин"
    user.name = "Олег"
    user.age = 15
    user.position = "ученый"
    user.speciality = "биолог"
    user.address = "module_2"
    user.email = "Savinoleg2007yan@yandex.ru"
    user.hashed_password = "bio"
    user.set_password(user.hashed_password)
    session.add(user)

    # 4
    user = User()
    user.surname = "Маликова"
    user.name = "Юлия"
    user.age = 15
    user.position = "пилот"
    user.speciality = "пилот, навигатор"
    user.address = "module_2"
    user.email = "juliamalikova31@yandex.ru"
    user.hashed_password = "pilot"
    user.set_password(user.hashed_password)
    session.add(user)

    # 5
    user = User()
    user.surname = "Лукашова"
    user.name = "Ульяна"
    user.age = 27
    user.position = "программист"
    user.speciality = "IT специалист"
    user.address = "module_2"
    user.email = "lukashovauv@yandexlyceum.ru"
    user.hashed_password = "comp"
    user.set_password(user.hashed_password)
    session.add(user)

    # 6
    user = User()
    user.surname = "Бин"
    user.name = "Шон"
    user.age = 63
    user.position = "старший инженер"
    user.speciality = "конструктор"
    user.address = "module_1"
    user.email = "bean@mars.org"
    user.hashed_password = "build"
    user.set_password(user.hashed_password)
    session.add(user)
    # В самом конце, запоминаем все изменения, которые мы сделали в БД
    session.commit()


if __name__ == '__main__':
    main()
