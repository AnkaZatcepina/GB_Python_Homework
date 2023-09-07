"""
📌 Создать страницу, на которой будет форма для ввода имени
и электронной почты
📌 При отправке которой будет создан cookie файл с данными
пользователя
📌 Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
📌 На странице приветствия должна быть кнопка "Выйти"
📌 При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""

from flask import Flask, render_template, request, abort, redirect, url_for, flash, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect(url_for('hello_user')))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return response
    return render_template('hw_login.html')

@app.route('/hello_user', methods=['GET', 'POST'])
def hello_user():
    name = request.cookies.get('name')
    if request.method == 'POST':
        response = make_response(redirect(url_for('login')))
        response.set_cookie('name', '', expires=0)
        response.set_cookie('email', '', expires=0)
        return response
    return render_template('hw_hello_user.html', name=name)   

if __name__ == '__main__':
    app.run(debug=True)       