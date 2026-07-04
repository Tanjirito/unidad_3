# negocio.py
# Aca va toda la logica de los 3 ejercicios. Esta capa no le pregunta nada
# al usuario ni imprime menus, solo recibe datos y devuelve resultados.

from datos import datos


def filtrar_por_categoria(categoria):
    """
    Ejercicio 1 - Tienda de Videojuegos
    Recibe una categoria y devuelve los juegos que pertenecen a ella.
    """
    try:
        categoria = categoria.strip().lower()
        if categoria == "":
            raise ValueError("La categoria no puede quedar vacia")

        resultado = []
        for juego in datos.videojuegos:
            if juego["categoria"].lower() == categoria:
                resultado.append(juego)

        return resultado

    except ValueError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Ocurrio un error inesperado al filtrar: {e}")
        return []


def buscar_vehiculo_por_patente(patente):
    """
    Ejercicio 2 - Registro de Vehiculos
    Busca un vehiculo en la lista a partir de su patente.
    """
    try:
        patente = patente.strip().upper().replace(" ", "").replace(".", "").replace("-", "")
        if patente == "":
            raise ValueError("Debe ingresar una patente")

        for vehiculo in datos.vehiculos:
            patente_guardada = vehiculo["patente"].upper().replace("-", "")
            if patente_guardada == patente:
                return vehiculo

        # si no encuentra nada retorna None, la capa de presentacion avisa
        return None

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Ocurrio un error inesperado al buscar la patente: {e}")
        return None


def consultar_habitaciones_disponibles():
    """
    Ejercicio 3 - Gestion de Reservas
    Devuelve solo las habitaciones que estan en estado disponible.
    """
    try:
        disponibles = [h for h in datos.habitaciones if h["estado"].lower() == "disponible"]
        return disponibles
    except Exception as e:
        print(f"Ocurrio un error inesperado al consultar habitaciones: {e}")
        return []
