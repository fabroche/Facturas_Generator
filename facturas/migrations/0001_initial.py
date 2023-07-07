# Generated by Django 4.2.3 on 2023-07-07 18:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, help_text='ID único para cada factura', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Nombre que tendra el listado de esta factura', max_length=255)),
                ('cloud_name', models.CharField(help_text='Ruta hasta el archivo en la nube', max_length=255, unique=True)),
                ('url', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.CreateModel(
            name='ListadoFactura',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, help_text='ID único para cada listado de facturas', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Nombre que tendra el listado de esta factura', max_length=255)),
                ('cloud_name', models.CharField(help_text='Ruta hasta el archivo en la nube', max_length=255, unique=True)),
                ('url', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Listados_Facturas',
            },
        ),
    ]
