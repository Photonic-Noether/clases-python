# Ejercicios propuestos - Clase 3
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Decorador manual (closure)
# Crea una función registrar(funcion) que reciba otra función como argumento y devuelva
# una nueva función que, al llamarla, imprima "Llamando a [nombre_funcion]",
# ejecute la función original y luego imprima "Función [nombre_funcion] completada".
# Aplícala a al menos dos funciones distintas usando funciones como argumentos (callback).
# Pista: usa el atributo __name__ de las funciones para obtener el nombre.


# Ejercicio 2: Suma de dígitos recursiva
# Implementa una función recursiva suma_digitos(n: int) -> int que reciba un número
# entero positivo y devuelva la suma de sus dígitos.
# Ejemplo: suma_digitos(1234) == 10, suma_digitos(9999) == 36
# Añade type hints y un docstring en estilo Google.
# No conviertas el número a string: usa operaciones aritméticas (// y %).


# Ejercicio 3: Validador de contraseña configurable
# Crea una función validar_contrasena(contrasena: str, *validadores) que reciba
# una contraseña y una cantidad variable de funciones de validación.
# Cada validador recibe la contraseña y devuelve True o False.
# La función principal devuelve True solo si todas las validaciones pasan,
# e imprime qué validaciones han fallado.
# Define al menos 3 validadores: longitud_minima(n), contiene_numero, contiene_mayuscula.
