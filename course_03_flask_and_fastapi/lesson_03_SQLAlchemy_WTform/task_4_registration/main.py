"""
    📌 Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
    содержать следующие поля:
        ○ Имя пользователя (обязательное поле)
        ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
        ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
        ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
    📌 После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
    и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
    заполнено или данные не прошли валидацию, то должно выводиться соответствующее
    сообщение об ошибке.
    📌 Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
    базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
    об ошибке.
"""

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from forms import RegisterForm
import os
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
app.app_context().push()

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.cli.command("test-data")
def add_test_data():
    user = User(username = 'test', email = 'test@test.com', password='test')
    db.session.add(user)
    db.session.commit()
    print('данные добавлены')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data

        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', form.password.data.encode('utf-8'), salt, 100000)        
        password = salt + key 

        birthdate = form.birthdate.data
        agreement = form.agreement.data
        new_user = User(username=username, email=email, password=password, birthdate=birthdate, agreement=agreement )
        db.session.add(new_user)
        db.session.commit()

        # Выводим сообщение об успешной регистрации
        success_msg = 'Registration successful!'
        return success_msg

    return render_template('register.html', form=form)

@app.get('/users')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)

if __name__ == "__main__":
    db.create_all()
    #add_test_data()
    app.run(debug=True)   