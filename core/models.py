from django.db import models
import datetime as dt
from django.forms import model_to_dict

# Create your models here.
class Empleado(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    rut = models.CharField(max_length=12, verbose_name='Rut', unique=True)
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')
    fecha_contrato = models.DateField(verbose_name='Fecha de contrato')
    fecha_fin_contrato = models.DateField(verbose_name='Fecha fin de contrato', null=True, blank=True)
    usuario = models.CharField(max_length=150, verbose_name='Usuario', unique=True)
    password = models.CharField(max_length=150, verbose_name='Contraseña')
    email = models.EmailField(verbose_name='Correo electrónico')
    phone = models.CharField(max_length=12, verbose_name='Teléfono')
    salario = models.IntegerField(verbose_name='Salario')
    estado = models.BooleanField(verbose_name='Estado', default=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, verbose_name='Avatar')
    perfiles = models.ManyToManyField('Perfil', verbose_name='Perfiles')
    

    def __str__(self):
        return self.nombres
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['nombres']

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    descripcion = models.CharField(max_length=150, verbose_name='Descripción')
    estado = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return self.nombre_categoria
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre_categoria']

class Perfil(models.Model):

    nombre_perfil = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.CharField(max_length=250, verbose_name='Descripción')

    def __str__(self):
        return self.nombre_perfil
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['nombre_perfil']

    
class Venta(models.Model):
    subtotal = models.IntegerField(verbose_name='Subtotal')
    iva = models.IntegerField(verbose_name='IVA')
    total = models.IntegerField(verbose_name='Total')
    fecha_venta = models.DateField(verbose_name='Fecha de venta')
    total = models.IntegerField(verbose_name='Total')
    numero_venta = models.IntegerField(verbose_name='Número de venta', unique=True)
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, verbose_name='Empleado')
    descuento = models.IntegerField(verbose_name='Descuento', default=0)


    def __str__(self):
        return self.fecha_venta
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['fecha_venta']

class DetalleVenta(models.Model):
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.IntegerField(verbose_name='Precio')
    subtotal = models.IntegerField(verbose_name='Subtotal')
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE, verbose_name='Venta')
    productos = models.ManyToManyField('Producto', verbose_name='Productos')

    def __str__(self):
        return self.cantidad
    
    class Meta:
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalles de venta'
        ordering = ['cantidad']

class Producto(models.Model):
    codigo_producto = models.CharField(max_length=50, verbose_name='Código del producto', unique=True)
    nombre_producto = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.CharField(max_length=250, verbose_name='Descripción')
    stock = models.IntegerField(verbose_name='Stock')
    precio = models.IntegerField(verbose_name='Precio')
    estado = models.BooleanField(verbose_name='Estado', default=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, verbose_name='Categoría')
    imagen = models.ImageField(upload_to='products', null=True, blank=True, verbose_name='Imagen')
    proveedores = models.ManyToManyField('Proveedor', verbose_name='Proveedores')

    


    def __str__(self):
        return self.nombre_producto
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre_producto']

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=150, verbose_name='Nombre')
    rut = models.CharField(max_length=12, verbose_name='Rut', unique=True)
    email = models.EmailField(verbose_name='Correo electrónico')
    phone = models.CharField(max_length=12, verbose_name='Teléfono')
    estado = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return self.nombre_proveedor
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre_proveedor']

