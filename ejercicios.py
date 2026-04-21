# Ejercicios propuestos - Clase 5
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Ordenador de registros configurable con lambdas
# Crea una función ordenar_registros(registros: list[dict], *campos, reverso: bool = False)
# que ordene una lista de diccionarios por múltiples campos en orden de prioridad.
# Si hay empate en el primer campo, ordena por el segundo, etc.
# Ejemplo: ordenar por "apellido" primero y por "nombre" en caso de empate.
# Usa sorted() con una lambda como clave. No uses itemgetter del módulo operator.


# Ejercicio 2: Contador con límite (closure con nonlocal)
# Crea una función crear_contador(limite: int, paso: int = 1) que devuelva
# dos funciones: incrementar() y obtener().
# - incrementar(): suma paso al contador interno, pero no supera el límite.
#   Devuelve True si incrementó y False si ya estaba en el límite.
# - obtener(): devuelve el valor actual del contador.
# El estado debe mantenerse entre llamadas usando closures con nonlocal.
# No uses clases ni variables globales.


# Ejercicio 3: Generador de informes configurable
# Crea una función generar_informe(titulo: str, datos: list[dict], *campos, **opciones)
# donde campos son las claves a incluir y opciones puede contener:
# separador (por defecto "|"), ancho_columna (por defecto 15), mostrar_total (bool).
# La función imprime una tabla formateada con los campos seleccionados.
# Si mostrar_total=True, suma la columna numérica indicada en opciones["columna_total"].
