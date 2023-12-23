# TestFructorum

Описание проекта

TestFructorum это django-rest-framework проект. Проект создан для работы над закладками и добывлении их в коллекции.

Запуск проэкта

    1. Установите docker
    2. Склонируйте себе проект 
    3. Из папки  app проекта запустите docker-compose build
    4. После docker-compose up
    5.Проект доступен по адрессу http://127.0.0.1:8000

Приложения и модели

    1. Complation - Коллекция, вкотору можно добавить закладку
    2. Bookmark - Закладка с данными со страницы сайта
    3. CustomUser - кастомная модель пользователей. Переопределен и кастомизирован также и UersManager класс (app/users/manager.py)


Эндпоинты и документация

  Настроена документация yasg-drf. Все эндпоинты можно изучить по ссылкам: http://localhost:8000/redoc/ http://localhost:8000/dosc/


Технологии и стек:

        python, django, djangorestframework, python-dotenv, psycopg2-binary, djangorestframework-simplejwt,
        drf-yasg, flake8-for-pycharm, opengraph_py3

