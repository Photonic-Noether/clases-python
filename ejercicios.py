# Ejercicios propuestos - Clase 7
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Gestor de logs rotativo
# Crea una clase GestorLogs con un método registrar(nivel, mensaje) donde nivel
# puede ser "INFO", "WARNING" o "ERROR". Los mensajes se escriben en un archivo
# "app.log" con formato "[NIVEL] YYYY-MM-DD HH:MM:SS - mensaje".
# Cuando el archivo supere 1KB, debe "rotar": renombra el actual añadiendo un
# sufijo con timestamp (ej: "app_20240101_120000.log") y crea uno nuevo vacío.
# Usa pathlib para las rutas y el módulo datetime para el timestamp.


# Ejercicio 2: Explorador de directorios estadístico
# Crea una función explorar(ruta: str, extensiones: list[str] = None) que use pathlib
# para recorrer recursivamente un directorio y devuelva un diccionario:
# {".py": {"archivos": 5, "tamaño_total": 12340}, ".txt": {...}, ...}
# Si extensiones no es None, filtra solo esas extensiones.
# Al final imprime el resumen formateado mostrando cada extensión, cantidad de
# archivos y tamaño total en formato legible (B, KB, MB).


# Ejercicio 3: Juego de cartas "Guerra" con registro en archivo
# Usando las clases Carta y Baraja del notebook, implementa el juego "Guerra":
# - Reparte todas las cartas entre dos jugadores (listas).
# - Cada ronda: ambos revelan su primera carta; quien tenga mayor valor se lleva ambas.
# - En empate: cada jugador pone 1 carta boca abajo y juegan la siguiente.
# - El juego termina cuando uno se queda sin cartas.
# Registra cada ronda en un archivo "guerra.log" usando context managers (with).
# Los valores van de As(1) a Rey(13); usa un diccionario para mapear nombres a números.
