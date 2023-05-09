from django.shortcuts import render
from django.views.generic import ListView
from core.models import Producto



class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/list.html'
    context_object_name = 'productos'
    #paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        return context
    