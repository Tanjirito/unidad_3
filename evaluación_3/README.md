# Evaluacion 03 - Unidad 3: Colecciones y librerias en Python

Proyecto hecho para la Evaluacion 03. La app junta 3 ejercicios distintos
en un solo programa con menu, usando una arquitectura separada en 3 capas.

## Ejercicios resueltos

1. **Tienda de Videojuegos - Clasificacion por categoria**: se usa una
   coleccion (lista de diccionarios) de videojuegos y se puede buscar
   todos los titulos que pertenecen a una categoria (Aventura, Deportes,
   Accion, Sandbox).

2. **Registro de Vehiculos - Consulta de patentes**: se usa una lista de
   vehiculos registrados y se puede buscar la info de uno a partir de la
   patente que ingresa el usuario.

3. **Gestion de Reservas - Control de disponibilidad**: la capa de datos
   guarda las habitaciones de un hotel con su estado, y se puede
   consultar cuales estan disponibles.

## Estructura del proyecto

```
evaluación_3/
├── main.py
├── datos/
│   ├── __init__.py
│   └── datos.py          -> listas con la info (videojuegos, vehiculos, habitaciones)
├── negocio/
│   ├── __init__.py
│   └── negocio.py        -> funciones con la logica de los 3 ejercicios
└── presentacion/
    ├── __init__.py
    └── presentacion.py   -> menu e interaccion con el usuario
```

- **datos**: solo guarda la informacion, no tiene logica.
- **negocio**: recibe parametros, procesa, maneja los errores con
  try-except y devuelve resultados. No hace print ni input.
- **presentacion**: se encarga del menu, pedir datos al usuario con
  input() y mostrar los resultados con print().

## Como ejecutar

Se necesita tener Python 3 instalado. Desde la carpeta `evaluación_3`
ejecutar:

```
python main.py
```

Se abre un menu con 4 opciones:

1. Buscar videojuegos por categoria
2. Buscar un vehiculo por patente
3. Ver habitaciones disponibles
4. Salir

## Librerias usadas

Se uso la libreria `os` (viene incluida en Python) para limpiar la
pantalla de la consola entre cada opcion del menu, para que se vea mas
ordenado.
