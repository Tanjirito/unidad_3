import os

def guardar_rifa(listado_rifas):
    try:
        ruta = os.path.join('unidad_3/datos/','info_rifas.py')
        ruta_absoluta = os.path.abspath(ruta)
        ruta_real = os.path.realpath(ruta_absoluta)
        with open(ruta_real,'+w', encoding="utf-8") as archivo:   
            archivo.write(f'listado_rifas ={listado_rifas}')
            archivo.close()
    except Exception as error:
        print(error)