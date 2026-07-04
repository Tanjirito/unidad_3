from unidad_3.datos import listado_rifas,guardar_rifa
from prettytable import PrettyTable
from datetime import date

def obtener_listado_rifas():
    tabla_rifas = PrettyTable()
    tabla_rifas.field_names = ['Nombre','Fecha Creación','Precio Número','Cantidad Rifas','Fecha Lanzamiento']

    for rifa in listado_rifas:
        tabla_rifas.add_row([rifa['nombre'], rifa['fecha_creacion'], f'${rifa['precio']}', rifa['cantidad_rifas'], rifa['fecha_lanzamiento']])
    
    return tabla_rifas

def crear_nueva_rifa(nombre,precio,cantidad_rifas,numeros_rifa,fecha_creacion,fecha_lanzamiento,premios):
    nueva_rifa = {
        'nombre':nombre,
        'precio':precio,
        'cantidad_rifas':cantidad_rifas,
        'numeros_rifa':numeros_rifa,
        'fecha_creacion':fecha_creacion,
        'fecha_lanzamiento':fecha_lanzamiento,
        'premios':premios
    }
    listado_rifas.append(nueva_rifa)
    guardar_rifa(listado_rifas)