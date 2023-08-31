"""
📌 Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
📌 Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('task_8_base.html')

@app.route('/about/')
def about():
    return render_template('task_8_about.html') 

@app.route('/contacts/')
def contacts():
    return render_template('task_8_contacts.html') 

if __name__ == '__main__':
    app.run(debug=True)   