from django.shortcuts import render
from MainApp.models import Item


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru",
    }
    return render(request, "index.html", context)


def about(request):
    author = {
        "name": "Иван",
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
    context = {
        "author": author
    }
    return render(request, "about.html", context)


def get_item(request, item_id: int):
    """ Get item by id from db."""
    for item in items:
        if item["id"] == item_id:
            context = {
                "item": item
            }
            return render(request, "item_page.html", context)
    
    return render(request, "errors.html", {"errors": [f'Item with id={item_id} not found.']}, status=404)


def get_items(request):
    """ Get all items from db."""
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)
