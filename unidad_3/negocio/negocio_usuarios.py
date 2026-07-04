from unidad_3.datos import listado_usuarios,guardar_usuario
from prettytable import PrettyTable

def obtener_listado_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['N°','Nombre','Rut','Nacionalidad','Teléfono','Email','Tipo Usuario']

    for usuario in listado_usuarios:
        tabla_usuarios.add_row([usuario['id'],usuario['nombre'], usuario['rut'], usuario['nacionalidad'], usuario['telefono'], usuario['email'],usuario['tipo_usuario']])
    
    return tabla_usuarios

def crear_nuevo_usuario(nombre,rut,nacionalidad,telefono,email,tipo_usuario,contrasena):
    nuevo_usuario = {
        'id': len(listado_usuarios) + 1,
        'nombre':nombre.title(),
        'rut':rut,
        'nacionalidad':nacionalidad.title(),
        'telefono':telefono,
        'email':email,
        'tipo_usuario':tipo_usuario,
        'contrasena':contrasena
    }
    listado_usuarios.append(nuevo_usuario)
    guardar_usuario(listado_usuarios)