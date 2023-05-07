from django.shortcuts import render
<<<<<<< HEAD

def category_list(request):
    data = {}
=======
from core import db


def category_list(request):
    data = db.categories.findAll()
>>>>>>> dev
    return render(request, 'categories/list.html', data)
    