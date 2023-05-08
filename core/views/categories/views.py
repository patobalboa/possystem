from django.shortcuts import render
from django.views.generic import ListView
from core.models import Categoria

def category_list(request):
    data ={
        'title': 'Listado de Categorias',
        'categories': Categoria.objects.all()
    }
    return render(request, 'categories/list.html', data)

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categories/list.html'
    context_object_name = 'categories'
    #paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context
    