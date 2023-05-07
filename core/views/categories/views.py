from django.shortcuts import render
from core import db


def category_list(request):
    data = db.categories.findAll()
    return render(request, 'categories/list.html', data)
    