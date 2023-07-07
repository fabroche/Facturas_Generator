from rest_framework import generics
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from facturas.Models.models import Factura, ListadoFactura
from ..Serializers.facturasSerializer import ListadoFacturaSerializer
from ..Utils.Facturas_generator.facturas_generator import create_listado_factura


class FacturasViews(generics.GenericAPIView):
    serializer_class = ListadoFacturaSerializer

    def post(self, request: Request) -> Response:
        """
        Al enviar la ruta hasta el file en la nube, y su url el endpoint procesara el documento
        , subira a la nube el resultado y devolvera un JSON con los valores del documento procesado.
        opcionalmente puedes enviar un name para asignarselo al documento resultante
        :param request:
        :return: ListadoFactura
        """
        cloud_file_name: str = request.data.get('cloud_name', None)
        cloud_file_url: str = request.data.get('url', None)
        listado_name: str = request.data.get('name', None)

        factura = Factura()
        factura.cloud_name = cloud_file_name
        factura.url = cloud_file_url
        factura.name = listado_name
        Factura.objects.filter(
            cloud_name=factura.cloud_name,
            url=factura.url
        ).update_or_create(
            cloud_name=factura.cloud_name,
            url=factura.url,
            name=factura.name
        )

        listado_factura: ListadoFactura = create_listado_factura(factura)

        data = ListadoFacturaSerializer(listado_factura).data

        return Response(
            status=status.HTTP_200_OK,
            data=data,
        )
