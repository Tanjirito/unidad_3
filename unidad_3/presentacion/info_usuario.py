from unidad_3.negocio import crear_nuevo_usuario
from unidad_3.datos import opcion_invalida,correo_invalido
import re
import pwinput
import bcrypt

def solicitar_datos_usuario():
    nombre = input('Nombre Usuario: ')
    rut = input('Rut Usuario (12.345.678-5): ')
    nacionalidad = input('Nacionalidad Usuario: ')
    telefono = input('Teléfono Usuario: ')
    email = validar_email()
    print('Seleccione el tipo de usuario: ')
    print('[1] Administrador')
    print('[2] Observador')
    tipo_usuario = ''
    while tipo_usuario == '':
        opcion_tipo_usuario = input('Seleccione el tipo de usuario [1-2]: ')
        if opcion_tipo_usuario in ['1','2']:
            if opcion_tipo_usuario == '1':
                tipo_usuario = 'administrador'
            else:
                tipo_usuario = 'observador'
        else:
            print(opcion_invalida)
    contrasena = pwinput.pwinput(prompt='Contraseña: ',mask='*')
    contrasena = contrasena.encode('utf-8')
    contrasena_encriptada = bcrypt.hashpw(contrasena, bcrypt.gensalt())

    crear_nuevo_usuario(nombre,rut,nacionalidad,telefono,email,tipo_usuario,contrasena_encriptada)

def ingresar_correo():
    email = validar_email()
    return email

def validar_email():
    patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$'
    email = ''
        
    while email == '':
        email = input('Email Usuario (nombreusuario@servidor.dom): ')
        if re.fullmatch(patron_email, email):
            return email
        else:
            print(correo_invalido)
            email = ''