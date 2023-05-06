from django.db import models
import datetime as dt

# Create your models here.
class Empleado(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    rut = models.CharField(max_length=12, verbose_name='Rut', unique=True)
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')
    fecha_contrato = models.DateField(verbose_name='Fecha de contrato')
    email = models.EmailField(verbose_name='Correo electrónico')
    phone = models.CharField(max_length=12, verbose_name='Teléfono')
    salario = models.IntegerField(verbose_name='Salario')
    estado = models.BooleanField(verbose_name='Estado', default=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, verbose_name='Avatar')
    tipo = models.ForeignKey('Tipo', on_delete=models.CASCADE, verbose_name='Tipo')

    def __str__(self):
        return self.nombres
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['nombres']

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=150, verbose_name='Descripción')
    estado = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

class Tipo(models.Model):
    nombre_tipo = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.CharField(max_length=250, verbose_name='Descripción')

    def __str__(self):
        return self.nombre_tipo

    

