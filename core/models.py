from django.db import models
import datetime as dt

# Create your models here.
class Empresa(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    razon_social = models.CharField(max_length=150, verbose_name='Razón social')
    rut = models.CharField(max_length=8, verbose_name='RUT')
    password = models.CharField(max_length=150, verbose_name='Contraseña')
    direccion = models.CharField(max_length=150, verbose_name='Dirección')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    mfa = models.BooleanField(default=False, verbose_name='MFA')
    logo = models.ImageField(upload_to='logo', null=True, blank=True, verbose_name='Logo')
    mfa_code = models.CharField(max_length=6, null=True, blank=True, verbose_name='Código MFA')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['name']
        db_table = 'empresas'

class Perfil(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['name']
        db_table = 'perfiles'


class Employee(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    last_name = models.CharField(max_length=150, verbose_name='Apellido')
    email = models.EmailField(max_length=150, verbose_name='Correo')
    password = models.CharField(max_length=150, verbose_name='Contraseña')
    rut = models.CharField(max_length=8, verbose_name='RUT')
    date_joined = models.DateTimeField(default=dt.datetime.now, verbose_name='Fecha de ingreso')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name='Perfil')
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True, verbose_name='Avatar')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['name']
        db_table = 'empleados'



class Producto(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Precio')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    distribuidores = models.ManyToManyField('Distribuidor', verbose_name='Distribuidores')
    description = models.TextField(verbose_name='Descripción')
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']
        db_table = 'productos'
        
class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    fecha = models.DateTimeField(default=dt.datetime.now, verbose_name='Fecha')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    def __str__(self):
        return self.producto.name
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        ordering = ['producto']
        db_table = 'inventarios'


class Distribuidor(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    razon_social = models.CharField(max_length=150, verbose_name='Razón social')
    rut = models.CharField(max_length=8, verbose_name='RUT')
    empresas = models.ManyToManyField(Empresa, verbose_name='Empresas')
    direccion = models.CharField(max_length=150, verbose_name='Dirección')
    productos = models.ManyToManyField(Producto, verbose_name='Productos')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Distribuidor'
        verbose_name_plural = 'Distribuidores'
        ordering = ['name']
        db_table = 'distribuidores'


class Ventas(models.Model):
    detalle_productos = models.ManyToManyField(Producto, verbose_name='Detalle de productos')
    fecha = models.DateTimeField(default=dt.datetime.now, verbose_name='Fecha')
    total = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    def __str__(self):
        return self.detalle
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['fecha']
        db_table = 'ventas'


