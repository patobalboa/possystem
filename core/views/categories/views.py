from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.models import Categoria
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.forms import CategoriaForm
from django.urls import reverse_lazy

def category_list(request):
    data ={
        'title': 'Listado de Categorias',
        'categories': Categoria.objects.all()
    }
    return render(request, 'categories/list.html', data)

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'core/list.html'
    context_object_name = 'categories'
    #paginate_by = 10

    #@method_decorator(login_required)
    # disable csrf
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Categoria.objects.get(pk=request.POST['id']).toJSON()            
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        context['entity'] = 'Categoria'
        context['create_url'] = reverse_lazy('core:category_create')
        context['list_url'] = reverse_lazy('core:category_list')
        return context
    
# Create class for create a new category with widgets from forms.py
class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categories/create.html'
    success_url = reverse_lazy('core:category_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    


    # def post(self, request, *args, **kwargs):
    #     form = CategoriaForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return reverse_lazy('core:category_list')
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     context['create_url'] = reverse_lazy('core:category_create')
    #     context['entity'] = 'Categoria'
    #     context['list_url'] = reverse_lazy('core:category_list')
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Crear una categoria"
        context['entity'] = 'Categoria'
        context['create_url'] = reverse_lazy('core:category_create')
        context['list_url'] = reverse_lazy('core:category_list')
        context['action'] = 'add'
        return context
    
    
