from django.urls import path
#from core.views.categories.views import category_list
from core.views.views import baseUrl
from core.views.categories.views import *
from core.views.productos.views import *
from core.views.proveedores.views import *

app_name = 'core'

urlpatterns = [
    path('', baseUrl, name='baseUrl'),

    # Categorias URLs
    path('categoria', CategoriaListView.as_view(), name='category_list'),
    path('categoria/create/', CategoriaCreateView.as_view(), name='category_create'),
    path('categoria/edit/<int:pk>/', CategoriaUpdateView.as_view(), name='category_update'),

    # Productos URLs
    path('producto/list/', ProductoListView.as_view(), name='product_list'),

    # Proveedores URLs
    path('proveedor/list/', ProveedorListView.as_view(), name='provider_list'),


]