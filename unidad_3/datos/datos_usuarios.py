import os

def guardar_usuario(listado_usuarios):
    try:
        ruta = os.path.join('unidad_3/datos/','info_usuarios.py')
        ruta_absoluta = os.path.abspath(ruta)
        ruta_real = os.path.realpath(ruta_absoluta)
        with open(ruta_real,'+w', encoding="utf-8") as archivo:   
            archivo.write(f'listado_usuarios ={listado_usuarios}')
            archivo.close()
    except Exception as error:
        print(error)