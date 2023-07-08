import pandas as pd
from pandas import DataFrame

from djangoProject.settings import PROJECT_UTILS_FILES_ROOT
from facturas.Models.models import Factura, ListadoFactura
from facturas.firebaseconfig import FirebaseConfig


def create_listado_factura(factura: Factura) -> ListadoFactura:
    # 1 - descargar la factura
    firebase = FirebaseConfig()
    storage = firebase.get_storage()
    # sys_path = PROJECT_UTILS_FILES_ROOT.as_posix() if type(BASE_DIR) == PosixPath else PROJECT_UTILS_FILES_ROOT

    storage.child(factura.cloud_name).download(
        path="",
        filename=factura.cloud_name
    )

    # 2 - procesarla con pandas
    file_name = factura.cloud_name.split('/')[-1]
    # file_dir = sys_path + f'/{file_name}'
    dataframe_factura: DataFrame = pd.read_excel(file_name)
    # dataframe_listado_factura: DataFrame = dataframe_factura.groupby('FORNECEDORES').sum('VALOR S/IVA')
    dataframe_pivot: DataFrame = DataFrame(dataframe_factura.values)
    dataframe_listado_factura = DataFrame({
        'FORNECEDORES': [i for i in dataframe_pivot[0] if i != 'FORNECEDORES'],
        'VALOR S/IVA': [i for i in dataframe_pivot[3] if i != 'VALOR S/IVA'],
        'VALOR C/IVA': [i for i in dataframe_pivot[4] if i != 'VALOR C/IVA']
    }, )

    # 3 - crear objeto Listado factura
    listado_factura = ListadoFactura()
    listado_factura.name = factura.name
    listado_name_tail = f'_{listado_factura.name}.xlsx' if listado_factura.name else ''
    listado_factura.cloud_name = factura.cloud_name.replace(
        f'{file_name}',
        f'listado_{file_name.split(".xlsx")[0]}{listado_name_tail}',
    )
    listado_factura.name = listado_factura.name if listado_factura.name else \
        factura.cloud_name.split('/')[-1].split('.xlsx')[0]

    dataframe_listado_factura.to_excel(str(PROJECT_UTILS_FILES_ROOT) + f'/{listado_factura.name}.xlsx')

    # subir el fichero
    storage.child(listado_factura.cloud_name).put(str(PROJECT_UTILS_FILES_ROOT) + f'/{listado_factura.name}.xlsx')
    listado_factura.url = storage.child(listado_factura.cloud_name).get_url(None)
    ListadoFactura.objects.filter(
        cloud_name=listado_factura.cloud_name,
        url=listado_factura.url
    ).update_or_create(
        cloud_name=listado_factura.cloud_name,
        url=listado_factura.url,
        name=listado_factura.name

    )

    return listado_factura
