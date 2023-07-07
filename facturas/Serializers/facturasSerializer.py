from rest_framework import serializers

from facturas.Models.models import Factura, ListadoFactura


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'


class ListadoFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListadoFactura
        fields = '__all__'
