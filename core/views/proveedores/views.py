from django.shortcuts import render
from django.views.generic import ListView
from core.models import Proveedor



class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedores/list.html'
    context_object_name = 'proveedores'
    #paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proveedores'
        return context
    