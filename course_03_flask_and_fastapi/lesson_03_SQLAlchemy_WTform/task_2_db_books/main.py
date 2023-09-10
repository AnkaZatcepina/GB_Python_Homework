"""
    📌 Создать базу данных для хранения информации о книгах в библиотеке.
    📌 База данных должна содержать две таблицы: "Книги" и "Авторы".
    📌 В таблице "Книги" должны быть следующие поля: id, название, год издания,
    количество экземпляров и id автора.
    📌 В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
    📌 Необходимо создать связь между таблицами "Книги" и "Авторы".
    📌 Написать функцию-обработчик, которая будет выводить список всех книг с
    указанием их авторов.
"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Book, Author, BookAuthor
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
        book = Book(name=f"book{i}",year=1900, amount=i)
        db.session.add(book)
        author = Author(name=f"author{i}", lastname=f"lastname{i}")
        db.session.add(author)
        
    
    for i in range(1, 15):       
        book_author = BookAuthor(book_id=random.randint(1, count + 1), author_id=random.randint(1, count + 1))
        db.session.add(book_author)
    db.session.commit()
    print('данные добавлены')


@app.get('/books')
def all_books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)

if __name__ == "__main__":
    db.create_all()
    add_test_data()
    app.run(debug=True)    