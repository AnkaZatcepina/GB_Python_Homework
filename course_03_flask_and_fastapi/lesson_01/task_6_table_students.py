"""
📌 Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
📌 Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
📌 Данные о студентах должны быть переданы в шаблон через
контекст.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/students/')
def students_html():
    head = {
        'name': 'Имя',
        'lastname': 'Фамилия',
        'age': 'Возраст',
        'rating': 'Средий балл'
    }

    students_list = [
        {
            'name': 'Иван',
            'lastname': 'Иванов',
            'age': 18,
            'rating': 4.5
        },
        {
            'name': 'Пётр',
            'lastname': 'Петров',
            'age': 19,
            'rating': 3.75
        },
        {
            'name': 'Семён',
            'lastname': 'Семёнов',
            'age': 20,
            'rating': 5
        }
    ]

    return render_template('task_6.html', **head, students_list=students_list)   

if __name__ == '__main__':
    app.run(debug=True)   