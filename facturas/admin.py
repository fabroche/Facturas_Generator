from django.contrib import admin

from facturas.Models.models import Factura, ListadoFactura

# Register your models here.
admin.site.register(Factura)
admin.site.register(ListadoFactura)
