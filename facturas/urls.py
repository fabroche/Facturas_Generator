from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from facturas.ApiViews.facturasApiViews import FacturasViews

swaggerUi_schema = get_schema_view(
    title='SwaggerUi ApiMetrics',
    description='Guide for the Factura Generator',
    version='v1.0.0',
)

urlpatterns = [

    # EndPoint para generar listado de Factura
    path('factura/', FacturasViews.as_view(), name="listado-factura"),

    # EndPoint para construir el schema de configuracion del Swagger
    path('schema/', swaggerUi_schema, name="schema-apiMetrics"),

    # EndPoint para visitar la Documentacion de la Api
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'schema-apiMetrics'}
    ), name='swagger-ui'),
]
