# Ejercicios propuestos - Clase 8
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Iterador de ventana deslizante
# Implementa una clase VentanaDeslizante que actúe como iterador personalizado.
# Recibe un iterable y un tamaño de ventana n. En cada iteración devuelve
# una tupla con los n elementos siguientes, solapándose de 1 en 1.
# Ejemplo: VentanaDeslizante([1, 2, 3, 4, 5], 3) ->  (1,2,3), (2,3,4), (3,4,5)
# Implementa __iter__ y __next__ correctamente y lanza StopIteration al terminar.
# No uses itertools.islice ni collections.deque en la implementación principal.


# Ejercicio 2: Pipeline de transformación con generadores encadenados
# Crea 4 generadores que se puedan encadenar:
# - leer_palabras(texto): genera las palabras de un texto una a una
# - filtrar_cortas(palabras, min_len=3): genera solo palabras de longitud >= min_len
# - normalizar(palabras): genera palabras en minúscula sin caracteres no alfabéticos
# - contar_frecuencia(palabras): devuelve un dict {palabra: frecuencia} al finalizar
# Encadénalos para procesar un texto de prueba y muestra las 5 palabras más frecuentes.
# Pista: usa yield y next() para encadenar generadores de forma perezosa.


# Ejercicio 3: Serializador configurable con comprensiones
# Crea una clase Serializador con método guardar(datos, ruta) y cargar(ruta).
# El formato (json o pickle) se detecta automáticamente por la extensión del archivo.
# Antes de guardar como JSON, transforma la lista de diccionarios usando una
# comprensión de diccionario para: convertir las claves a snake_case (minúsculas
# con guiones bajos en lugar de espacios) y excluir claves que empiecen por "_".
# Ejemplo: {"Nombre Completo": "Ana", "_id": 1} -> {"nombre_completo": "Ana"}
