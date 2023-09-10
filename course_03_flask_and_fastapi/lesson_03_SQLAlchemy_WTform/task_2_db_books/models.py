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

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)    
    year = db.Column(db.Integer, nullable=False)   
    amount = db.Column(db.Integer, nullable=False)
    
    authors = db.relationship('Author', secondary='book_author', backref="books", lazy=True)

    def __repr__(self):
        return f'Book: {self.id}, {self.name}, {self.amount} шт.'

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False) 
    lastname = db.Column(db.String(80), nullable=False)  
    
    def __repr__(self):
        return f'Author: {self.id}, {self.name} {self.lastname}'

class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)     