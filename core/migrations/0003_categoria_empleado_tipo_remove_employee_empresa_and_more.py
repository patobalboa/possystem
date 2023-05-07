# Generated by Django 4.2 on 2023-05-07 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_empresa_logo_empresa_mfa_empresa_mfa_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=150, verbose_name='Descripción')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['nombre_categoria'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=150, verbose_name='Nombres')),
                ('rut', models.CharField(max_length=12, unique=True, verbose_name='Rut')),
                ('birth_date', models.DateField(verbose_name='Fecha de nacimiento')),
                ('fecha_contrato', models.DateField(verbose_name='Fecha de contrato')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('phone', models.CharField(max_length=12, verbose_name='Teléfono')),
                ('salario', models.IntegerField(verbose_name='Salario')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Avatar')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['nombres'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=150, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripción')),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='distribuidores',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='detalle_productos',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='empresa',
        ),
        migrations.DeleteModel(
            name='Distribuidor',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='Inventario',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Ventas',
        ),
        migrations.AddField(
            model_name='empleado',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipo', verbose_name='Tipo'),
        ),
    ]