from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]



def home(request):
    text = """
            <h1>"Изучаем django"</h1>
            <strong>Автор</strong>: <i>Быстрова Е.А.</i>
            """
    return HttpResponse(text)

def users(request):
    text = """
            <strong>Имя</strong>: <i>Иван</i><br>
            <strong>Отчество</strong>: <i>Петрович</i><br>
            <strong>Фамилия</strong>: <i>Иванов</i><br>
            <strong>телефон</strong>: <i>8-923-600-01-02</i><br>
            <strong>email</strong>: <i>vasya@mail.ru</i>
            """

    return HttpResponse(text)

def products(request, id):
    text = """
            <strong>Имя</strong>: <i>Иван</i><br>
            <strong>Отчество</strong>: <i>Петрович</i><br>
            <strong>Фамилия</strong>: <i>Иванов</i><br>
            <strong>телефон</strong>: <i>8-923-600-01-02</i><br>
            <strong>email</strong>: <i>vasya@mail.ru</i>
            """

    return HttpResponse(text)


