import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


# Модель Марсиане
# Мы наследуемся от нашей абстрактной БД, которую мы создавали в файле db_session
# это нужно, чтобы табличка создалась именно в той базе
class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    # Название бд. По умолчанию, если не указать этот параметр, назовет так же, как называется класс
    __tablename__ = 'users'

    # описание всех столбцов таблицы users
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modifed_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    # Эта строчка говорит, что существует отношение (связь) между двумя таблицами.
    # Мы оставляем ссылку на таблицу jobs в этом классе, чтобы в запросах можно было к ней обращаться. Аналогично в Job
    jobs = orm.relationship("Jobs", back_populates='user')

    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'

    # шифрует пароль пользователя, чтобы он не хранился в первоначальном виде в БД
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    # При проверке пароля в момент входа в систему, будет зашифровывать введенный пароль по такому же алгоритму и
    # проверять, совпадает ли новая зашифрованная строчка с той, что хранится в БД.
    # По сути, то же самое, что сравнить пароль на одинаковость.
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
