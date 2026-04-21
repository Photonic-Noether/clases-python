# Ejercicios propuestos - Clase 4
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Constructor de consultas SQL con **kwargs
# Crea una función construir_query(tabla: str, **condiciones) que genere una cadena SQL:
# "SELECT * FROM tabla WHERE campo1='valor1' AND campo2=valor2"
# Los valores string deben ir entre comillas simples, los numéricos sin comillas.
# Ejemplo: construir_query("usuarios", nombre="Ana", edad=30)
# -> "SELECT * FROM usuarios WHERE nombre='Ana' AND edad=30"
# Si no hay condiciones, devuelve "SELECT * FROM tabla"


# Ejercicio 2: Función memoize con **kwargs
# Implementa una función memoize(funcion) que use un diccionario para almacenar
# los resultados ya calculados. La clave del caché debe funcionar tanto con args
# como con kwargs. Aplícala a una función que calcule el n-ésimo número de Fibonacci
# y compara el tiempo de ejecución con y sin caché usando time.time().
# Pista: necesitarás convertir los argumentos en algo hashable para usarlo como clave.


# Ejercicio 3: Pipeline de transformaciones con *args
# Crea una función pipeline(*transformaciones) que reciba funciones y devuelva
# una nueva función que aplique las transformaciones en orden al valor dado.
# Ejemplo: limpiador = pipeline(str.lower, str.strip, lambda s: s.replace(" ", "_"))
# limpiador("  Hola Mundo  ") debe devolver "hola_mundo"
# Añade type hints usando Callable del módulo typing.
