import uuid

from django.db import models


# Create your models here.
class Factura(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID único para cada factura",
        auto_created=True
    )
    name = models.CharField(
        max_length=255,
        help_text="Nombre que tendra el listado de esta factura",
        blank=True,
        null=True
    )
    cloud_name = models.CharField(
        max_length=255,
        help_text="Ruta hasta el archivo en la nube",
        blank=True,
        null=True
    )
    url = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.cloud_name

    class Meta:
        verbose_name_plural = 'Facturas'


class ListadoFactura(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID único para cada listado de facturas",
        auto_created=True
    )
    name = models.CharField(
        max_length=255,
        help_text="Nombre que tendra el listado de esta factura",
        blank=True,
        null=True
    )

    cloud_name = models.CharField(
        max_length=255,
        help_text="Ruta hasta el archivo en la nube",
        blank=True,
        null=True
    )
    url = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.cloud_name

    class Meta:
        verbose_name_plural = 'Listados_Facturas'
