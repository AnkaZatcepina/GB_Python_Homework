
from pathlib import PurePath, Path
from flask import Flask,  render_template, request, abort, redirect, url_for, flash
from werkzeug.utils import secure_filename
from markupsafe import escape
import logging

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e'

logger = logging.getLogger(__name__)


@app.route('/')
def base():
    return render_template('base.html')

"""
📌 Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""
@app.route('/next')
def next_page():
    return 'Привет, Вася'


"""
📌 Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""
@app.route('/load_image', methods=['GET', 'POST'])
def load_image():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    context = {'task': 'Задание 2'}
    return render_template('task_2_load_image.html', **context)


"""
📌 Создать страницу, на которой будет форма для ввода логина
и пароля
📌 При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
"""
@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
    users = {'test1@gmail.com': '123'}
    if request.method == 'POST':
        auth_email = request.form.get('auth_email')
        auth_pass = request.form.get('auth_pass')
        if users.get(auth_email) == auth_pass:
            return f"Вход с почты: {escape(auth_email)} выполнен"
        else:
            return 'Ошибка'
    context = {'task': 'Задание 3'}
    return render_template('task_3_authorization.html', **context)

"""
📌 Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
📌 При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""

@app.route('/calc_words', methods=['GET', 'POST'])
def calc_words():
    if request.method == 'POST':
        text = request.form.get('text')
        return f"Количество слов: {len(text.split())}"

    context = {'task': 'Задание 4'}
    return render_template('task_4_calc_words.html', **context)


"""
📌 Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
📌 При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.
"""
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        number_1 = request.form.get('number_1')
        number_2 = request.form.get('number_2')
        operation = request.form.get('operation')
        if operation == 'add':
            return f'{int(number_1) + int(number_2)}'
        elif operation == 'subtract':
            return f'{int(number_1) - int(number_2)}'
        elif operation == 'multiply':
            return f'{int(number_1) * int(number_2)}'
        elif operation == 'divide':
            if number_2 == '0':
                return f'Нельзя делить на ноль'
            return f'{int(number_1) / int(number_2)}'
    context = {'task': 'Задание 5'}
    return render_template('task_5_calculator.html', **context)

"""
📌 Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
📌 При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
"""
@app.errorhandler(403)
def access_forbidden(e):
    logger.warning(e)
    context = {
        'title': 'Доступ запрещен по возрасту',
        'url': request.base_url,
    }
    return render_template('403.html', **context), 403

@app.route('/input_name_age', methods=['GET', 'POST'])
def input_name_age():
    MIN_AGE = 18
    MAX_AGE = 130
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if MIN_AGE < int(age) < MAX_AGE:
            return f'{name}, вы вошли'
        abort(403)    
    context = {'task': 'Задание 6'}
    return render_template('task_6_input_name_age.html', **context)

"""
📌 Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
📌 При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
"""
@app.route('/calc_square', methods=['GET', 'POST'])
def calc_square():
    if request.method == 'POST':
        number = request.form.get('number')
        return redirect(url_for('calc_square_result', number=number))
            
    context = {'task': 'Задание 7'}
    return render_template('task_7_calc_square.html', **context)

@app.route('/calc_square/<int:number>')
def calc_square_result(number: int):
    result = int(number) ** 2
    return f'{number} в квадрате равно {result}'    

"""
📌 Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
📌 При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
"""
@app.route('/hello_user', methods=['GET', 'POST'])
def hello_user():
    if request.method == 'POST':
        name = request.form.get('name')
        # Проверка данных формы
        if not name:
            flash('Введите имя!', 'danger')
            return redirect(url_for('hello_user'))
        # Обработка данных формы
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('hello_user'))
            
    context = {'task': 'Задание 8'}
    return render_template('task_8_hello_user.html', **context)

if __name__ == '__main__':
    app.run(debug=True)    