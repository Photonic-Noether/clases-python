# Ejercicios propuestos - Clase 2
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Detector de anagramas
# Dadas dos palabras introducidas por el usuario, comprueba si son anagramas
# (contienen exactamente las mismas letras). No uses sort(): hazlo construyendo
# un diccionario que cuente la frecuencia de cada letra en cada palabra y compáralos.
# Ignora mayúsculas y espacios.


# Ejercicio 2: Top 3 de estudiantes
# Dado un diccionario de estudiantes con sus listas de notas:
# {"Ana": [7, 8, 6], "Luis": [9, 5, 8], "Marta": [10, 9, 8], ...}
# Calcula la media de cada alumno y muestra el top 3 con mayor media.
# Usa slicing para obtener los 3 primeros tras ordenar el resultado.


# Ejercicio 3: Inventario de tienda
# Modela un inventario como un diccionario {producto: (precio, cantidad)}.
# Implementa las siguientes operaciones usando métodos de diccionario:
# - Añadir producto (con .setdefault para evitar sobreescribir si ya existe)
# - Actualizar stock de un producto
# - Calcular el valor total del inventario (precio * cantidad de cada producto)
# - Listar los productos agotados (cantidad == 0)
