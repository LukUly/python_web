# файл, который добавляет конкретные работы в таблицу jobs
from data.jobs import Jobs
from flask import Flask
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# Первая работа


def main():
    # проверяем, первый раз ли коннектимся к БД db/mars_explorer.db
    db_session.global_init("db/mars_explorer.db")
    # Открываем сессию, чтобы можно было брать данные из БД или изменять их
    session = db_session.create_session()

    # Создаем новую строчку (новую работу)
    job = Jobs()
    # Заполняем все ее характеристики (столбцы из БД)
    job.team_leader = 4
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    # Говорим сессии, что будем добавлять эту строку в БД
    session.add(job)

    # Аналогично добавляем еще несколько работ
    job = Jobs()
    job.team_leader = 2
    job.job = 'разведка полезных ископаемых'
    job.work_size = 15
    job.collaborators = '4, 3, 6'
    job.is_finished = True

    session.add(job)

    job = Jobs()
    job.team_leader = 5
    job.job = 'разработка системы управления'
    job.work_size = 25
    job.collaborators = '5'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 3
    job.job = 'анализ проб атмосферного воздуха'
    job.work_size = 15
    job.collaborators = '4, 5'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 5
    job.job = 'Обслуживание марсохода'
    job.work_size = 5
    job.collaborators = '4'
    job.is_finished = True

    session.add(job)

    # В самом конце, запоминаем все изменения, которые мы сделали в БД
    session.commit()


if __name__ == '__main__':
    main()
