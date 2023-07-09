# Телеграм-бот для ввода показний счётчиков горячей и холодной воды
Создан: Анна Зацепина

## Для начала работы:

1.  Скопируйте файл .env.example в файл .env.
    Заполните недостающие данные
2.  Установите необходимые библиотеки из файла requirements.txt
3.  Запустите файл bot.py на сервере


## Модули:
* bot.py        - модуль для взаимодействия с API telegram 
* interface.py  - описание кнопок меню
* data_file.py  - работа с данными, чтение и запись показаний в файл

## Хранение данных
Показания хранится в файле meters.txt

## ToDo
1.  Добавить проверку введённых показаний на число.
2.  Добавить проверку разницы предыдущщих и текущих показаний.
    Должна быть > 0.