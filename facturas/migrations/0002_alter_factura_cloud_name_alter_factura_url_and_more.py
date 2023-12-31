# Generated by Django 4.2.3 on 2023-07-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='cloud_name',
            field=models.CharField(blank=True, help_text='Ruta hasta el archivo en la nube', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='listadofactura',
            name='cloud_name',
            field=models.CharField(blank=True, help_text='Ruta hasta el archivo en la nube', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='listadofactura',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
