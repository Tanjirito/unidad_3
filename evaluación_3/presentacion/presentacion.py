# presentacion.py
# Esta es la capa que interactua con el usuario. Todo lo que es
# input() y print() para mostrar cosas por pantalla va aca.

import os
from negocio import negocio


def limpiar_pantalla():
    # funciona tanto en windows como en mac/linux
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresione ENTER para volver al menu...")


def mostrar_menu():
    print("=" * 40)
    print("   SISTEMA DE GESTION - EVALUACION 03")
    print("=" * 40)
    print("1. Tienda de Videojuegos - Buscar por categoria")
    print("2. Registro de Vehiculos - Consultar por patente")
    print("3. Gestion de Reservas - Ver habitaciones disponibles")
    print("4. Salir")
    print("=" * 40)


def opcion_videojuegos():
    limpiar_pantalla()
    print("--- TIENDA DE VIDEOJUEGOS ---\n")
    categoria = input("Ingrese la categoria a buscar (Ej: Aventura, Deportes, Accion, Sandbox): ")

    juegos = negocio.filtrar_por_categoria(categoria)

    if len(juegos) == 0:
        print("\nNo se encontraron juegos para esa categoria.")
    else:
        print(f"\nJuegos encontrados en la categoria '{categoria}':\n")
        for juego in juegos:
            print(f"- {juego['titulo']} | ${juego['precio']}")

    pausar()


def opcion_vehiculos():
    limpiar_pantalla()
    print("--- REGISTRO DE VEHICULOS ---\n")
    patente = input("Ingrese la patente a consultar (Ej: AB1234): ")

    vehiculo = negocio.buscar_vehiculo_por_patente(patente)

    if vehiculo is None:
        print("\nNo se encontro ningun vehiculo con esa patente.")
    else:
        print("\nVehiculo encontrado:")
        print(f"Patente: {vehiculo['patente']}")
        print(f"Marca: {vehiculo['marca']}")
        print(f"Modelo: {vehiculo['modelo']}")
        print(f"Propietario: {vehiculo['propietario']}")

    pausar()


def opcion_reservas():
    limpiar_pantalla()
    print("--- GESTION DE RESERVAS ---\n")

    disponibles = negocio.consultar_habitaciones_disponibles()

    if len(disponibles) == 0:
        print("No hay habitaciones disponibles en este momento.")
    else:
        print("Habitaciones disponibles:\n")
        for hab in disponibles:
            print(f"Habitacion {hab['numero']} | Tipo: {hab['tipo']}")

    pausar()


def iniciar_menu():
    opcion = ""
    while opcion != "4":
        limpiar_pantalla()
        mostrar_menu()

        opcion = input("Ingrese una opcion: ")

        try:
            if opcion == "1":
                opcion_videojuegos()
            elif opcion == "2":
                opcion_vehiculos()
            elif opcion == "3":
                opcion_reservas()
            elif opcion == "4":
                print("\nSaliendo del sistema... bye!")
            else:
                print("\nEsa opcion no existe, intente de nuevo.")
                pausar()
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
            pausar()
