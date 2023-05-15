from django.forms import ModelForm
from core.models import *
from django import forms


# Formulario para el modelo Categoria
class CategoriaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
            field.field.widget.attrs['autocomplete'] = 'off'
            field.field.widget.attrs['autofocus'] = True

    class Meta:
        model = Categoria
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'nombre_categoria': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la categoría',
                    'maxlength': 50,
                    'autofocus': True,
                    'required': True
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese la descripción de la categoría',
                    'rows': 3,
                    'maxlength': 150
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'placeholder': 'Ingrese el estado de la categoría'
                }
            )}
            
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data