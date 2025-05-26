from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru",
}


def home(request):
    # from pprint import pprint
    # pprint(f'{vars(request) = }')
    # print(request.META.get("SERVER_NAME"))
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)


def about(request):
    text = ""
    for key, value in author.items():
        text += f'{key}: <b>{value}</b><br>'
    return HttpResponse(text)