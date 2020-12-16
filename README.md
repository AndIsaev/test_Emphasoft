# test_Emphasoft
Тестовое задание от компании Emphasoft

# Задача:
Реализовать CRUD для пользователя в api-сервисе

# Реализовано:
- Реристрация пользователя
- Авторизация поьзователя
- Возмоожность изменения и удаления своих данных только владельцу юзера или администратору
- Пермишены (доступ только авторизованным пользователям)
- Тестирование приложения

# Стек:
- Python
- Django
- Django REST-framework
- djoser

# Запуск приложения
Чтобы развернуть проект локально:

- python -m venv venv
- source venv/Scripts/activate
- cd test_project
- pip install -r requirements.txt
- python manage.py test
