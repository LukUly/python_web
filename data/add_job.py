from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

# Форма для добавления в БД новой работы. Написана с помощью flask_wtf
class AddJobForm(FlaskForm):
    # validators - означает, что поле обязательное для заполнения. 
    # то есть, без заполнения этого поля не удастся нажать кнопку
    job = StringField('Описание работы/ Job Title', validators=[DataRequired()])
    team_leader = IntegerField('id Тимлида/ Team Leader id', validators=[DataRequired()])
    work_size = StringField('Длительность работы/ Work Size', validators=[DataRequired()])
    collaborators = StringField('Исполнители/ Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Эта работа закончена?/ Is job finished?')

    submit = SubmitField('Submit')
