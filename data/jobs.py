import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

# Модель Работы
# Мы наследуемся от нашей абстрактной БД, которую мы создавали в файле db_session
# это нужно, чтобы табличка создалась именно в той базе
class Jobs(SqlAlchemyBase):
    # Название бд. По умолчанию, если не указать этот параметр, назовет так же, как называется класс
    __tablename__ = 'jobs'

    # описание всех столбцов таблицы jobs
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    # здесь мы показываем, что таблица users связана с таблицей jobs через столбцы id - team_lead
    # по факту, это означает, что тимлид тоже является пользователем
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    # эта строчка говорит, что существует отношение (связь) между двумя таблицами.
    # Мы оставляем ссылку на таблицу users в этом классе, чтобы в запросах можно было к ней обращаться. Аналогично в User
    user = orm.relationship('User')

    # Если не помним, этот метод описывает, как будет выглядеть объект этого класса при печати print
    def __repr__(self):
        return f'<Job> {self.job}'
