from django.urls import path
#from core.views.categories.views import category_list
from . import views
from core.views.categories.views import category_list

app_name = 'core'

app_name = 'core'

urlpatterns = [
<<<<<<< HEAD
    #path('', views.index, name='index'),
    #path('categories/list/', category_list, name='category_list')
=======
    path('', views.index, name='index'),
    path('categories/list/', category_list, name='category_list'),
>>>>>>> dev
]