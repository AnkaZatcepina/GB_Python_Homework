"""
📌 Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
📌 Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

cloth_list = [
    {
        "name": "куртка",
        "img": "https://img.freepik.com/free-photo/cheerful-young-european-girl-with-dark-flowing-hair-and-closed-eyes-in-winter-clothes-studio-people-emotions-lifestyle-and-fashion-concept_197531-31623.jpg?w=740&t=st=1693555138~exp=1693555738~hmac=a476cafef69552f40121134b23b35c7feadc2279bbce96fdd0335dc208e6237f",
        "href": "jacket/",
        "size_list": ["S", "M", "L"],
        "color_list": ["белый", "синий", "зеленый"]
    },
    {
        "name": "штаны",
        "img": "https://img.freepik.com/free-photo/hand-holding-light-brown-beige-pants_23-2150756276.jpg?t=st=1693555358~exp=1693555958~hmac=074a15aa925a7f6c0deea30b135df7177800c70abe0e374f247291214fa4171a",
        "href": "trousers/",
        "size_list": ["S", "L"],
        "color_list": ["синий", "черный"]
    }
]

def get_item(href:str)-> {}:
    for item in cloth_list:
        if item["href"] == (href+'/'):
            return item
    return None        

@app.route('/')
def main():    
    return render_template('hw_task_1_home.html')

@app.route('/cloth/')
def cloth():
    return render_template('hw_task_1_cloth_list.html', cloth_list=cloth_list)  

@app.route('/cloth/<string:item_name>/')
def item(item_name: str):
    item = get_item(item_name)
    return render_template('hw_task_1_item.html', **item)    

@app.route('/shoes/')
def shoes():
    return render_template('hw_task_1_shoes_list.html')


if __name__ == '__main__':
    app.run(debug=True)            