from unidad_3.datos import numero_version,titulo_app,menu_aplicacion,sub_menu,opcion_invalida
from unidad_3.negocio import obtener_listado_usuarios,obtener_listado_rifas
from unidad_3.presentacion import solicitar_datos_rifa,solicitar_datos_usuario,ingresar_correo

def login():
    print(f'\n{titulo_app} v{numero_version}')
    print(f'{'=' * len(titulo_app)}=={'=' * len(numero_version)}')
    titulo_menu('Login')
    correo = ingresar_correo()

def menu_principal():
    print(f'\n{titulo_app} v{numero_version}')
    print(f'{'=' * len(titulo_app)}=={'=' * len(numero_version)}')
    
    while True:
        titulo_menu('Menú Principal')
        for clave,valor in menu_aplicacion.items():
            print(f'[{clave}] - {valor}')
        opcion = seleccionar_opcion(menu_aplicacion)

        if opcion == '1':
            while True:
                titulo_menu('SubMenú Rifas')
                for clave,valor in sub_menu.items():
                    if clave != '0':
                        print(f'[{clave}] - {valor + ' Rifas'}')
                    else:
                        print(f'[{clave}] - {valor}')
                opcion_sub_menu = seleccionar_opcion(sub_menu)

                if opcion_sub_menu == '0':
                    print('Volviendo al menú anterior...')
                    break
                elif opcion_sub_menu == '1':
                    solicitar_datos_rifa()
                elif opcion_sub_menu == '2':
                    tabla_rifas = obtener_listado_rifas()
                    print(tabla_rifas)
                else:
                    print(opcion_invalida)
        elif opcion == '2':
            while True:
                titulo_menu('SubMenú Usuarios')
                for clave,valor in sub_menu.items():
                    if clave != '0':
                        print(f'[{clave}] - {valor + ' Usuarios'}')
                    else:
                        print(f'[{clave}] - {valor}')
                
                opcion_sub_menu = seleccionar_opcion(sub_menu)

                if opcion_sub_menu == '0':
                    print('Volviendo al menú anterior...')
                    break
                elif opcion_sub_menu == '1':
                    solicitar_datos_usuario()
                elif opcion_sub_menu == '2':
                    tabla_usuarios = obtener_listado_usuarios()
                    print(tabla_usuarios)
                else:
                    print(opcion_invalida)
        elif opcion == '0':
            print(f'Gracias por usar {titulo_app}.\n¡Hasta Luego!')
            break
        else:
            print(opcion_invalida)

def titulo_menu(menu):
    print()
    print(menu)
    print(f'{'=' * len(menu)}')

def seleccionar_opcion(menu):
    opcion = input(f'\nSeleccione su Opción [0-{len(menu) - 1}]: ')
    return opcion