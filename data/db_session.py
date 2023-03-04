# Стандартный файл, для обеспечения подключения к базе данных через средства sqlalchemy
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

# некоторая абстрактная база данных. Пока что просто место для нашей базы, которую мы будем создавать
SqlAlchemyBase = dec.declarative_base()
# сессия подключения к БД. Отслеживает, имеется ли уже подключение к БД. Как кнопка connect в SQLite
__factory = None

# функция, которая проверяет, что мы уже подключены приложением в БД. Если не подключены - подключаемся. Получает на вход путь к БД
# Подробнее можно почитать в уроке WEB. Знакомство с flask-sqlalchemy в пункте 4
def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)

#создает сессию подключения к БД, что позволяет вносить в нее изменения
# Можно подробнее почитать о такой теме, как Аннотация типов в Python
def create_session() -> Session:
    global __factory
    return __factory()
