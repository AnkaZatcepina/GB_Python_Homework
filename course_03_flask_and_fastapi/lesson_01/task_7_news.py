"""
📌 Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
📌 Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
📌 Данные о новостях должны быть переданы в шаблон через
контекст.
"""
from datetime import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/news/')
def news_html():
    news_list = [
        {
            'title': 'Новость 1',
            'description': 'новость 1, опсание 1',
            'date': datetime.now().strftime('%H:%M - %m.%d.%Y года')
        },
        {
            'title': 'Новость 2',
            'description': 'новость 2, опсание 2',
            'date': datetime.now().strftime('%H:%M - %m.%d.%Y года')
        },
        {
            'title': 'Новость 3',
            'description': 'новость 3, опсание 3',
            'date': datetime.now().strftime('%H:%M - %m.%d.%Y года')
        }
    ]

    return render_template('task_7.html', news_list=news_list)   

if __name__ == '__main__':
    app.run(debug=True)   