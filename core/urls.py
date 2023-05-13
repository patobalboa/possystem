from django.urls import path
#from core.views.categories.views import category_list
#from . import views
from core.views.categories.views import *
from core.views.productos.views import *
from core.views.proveedores.views import *

app_name = 'core'

urlpatterns = [
    #path('', views.index, name='index'),

    # Categorias URLs
    path('categoria/list/', CategoriaListView.as_view(), name='category_list'),
    path('categoria/create/', CategoriaCreateView.as_view(), name='category_create'),

    # Productos URLs
    path('producto/list/', ProductoListView.as_view(), name='product_list'),

    # Proveedores URLs
    path('proveedor/list/', ProveedorListView.as_view(), name='provider_list'),


]