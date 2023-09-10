"""
    📌 Создать базу данных для хранения информации о студентах университета.
    📌 База данных должна содержать две таблицы: "Студенты" и "Факультеты".
    📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
    возраст, пол, группа и id факультета.
    📌 В таблице "Факультеты" должны быть следующие поля: id и название
    факультета.
    📌 Необходимо создать связь между таблицами "Студенты" и "Факультеты".
    📌 Написать функцию-обработчик, которая будет выводить список всех
    студентов с указанием их факультета.
"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Student, Faculty
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
#db = SQLAlchemy(app)
db.init_app(app)
app.app_context().push()

"""Чтобы вызывать в командной строке 'flask init-db'"""
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.cli.command("test-data")
def add_test_data():
    count = 5
    for i in range(1, count + 1):
        faculty = Faculty(name=f"faculty{i}")
        db.session.add(faculty)
        for j in range(1, 3):
            student = Student(
                name=f"name{i}{j}",
                lastname=f"surname{i}{j}",
                age=random.randint(18, 25),
                group=2,
                gender=random.choice(["m", "s"]),
                faculty_id=i
            )
            db.session.add(student)
    db.session.commit()
    print('данные добавлены')


@app.get('/students')
def all_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)

if __name__ == "__main__":
    db.create_all()
    add_test_data()
    app.run(debug=True)    