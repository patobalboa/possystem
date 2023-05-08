from django.urls import path
#from core.views.categories.views import category_list
#from . import views
from core.views.categories.views import *

app_name = 'core'

urlpatterns = [
    #path('', views.index, name='index'),
    path('categoria/list/', CategoriaListView.as_view(), name='category_list'),
]