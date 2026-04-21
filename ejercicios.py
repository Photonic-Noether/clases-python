# Ejercicios propuestos - Clase 5
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Paquete de utilidades matemáticas
# Crea un paquete llamado matutils/ con tres módulos:
# - estadistica.py: funciones media(lista), mediana(lista), moda(lista)
# - geometria.py: funciones area_circulo(r), area_rectangulo(b, h), hipotenusa(a, b)
# - conversiones.py: funciones celsius_a_fahrenheit(c), km_a_millas(km), kg_a_libras(kg)
# En __init__.py importa las funciones más útiles de cada módulo para que se puedan usar
# directamente como matutils.media([1,2,3]) sin especificar el submódulo.


# Ejercicio 2: Configuración de aplicación con configparser
# Crea un archivo config.ini con secciones [servidor], [base_de_datos] y [app].
# Implementa un módulo settings.py con funciones:
# - cargar(): lee el .ini y devuelve el objeto ConfigParser
# - get(seccion, clave, fallback=None): obtiene un valor de forma segura
# - guardar(seccion, clave, valor): modifica un valor y persiste el archivo
# Demuestra su uso creando, leyendo y modificando valores desde un script main.py.


# Ejercicio 3: Instalador de entorno virtual automatizado
# Crea un script setup_env.py que:
# 1. Compruebe si existe un entorno virtual en ./venv usando os.path
# 2. Si no existe, lo cree usando subprocess para ejecutar 'python -m venv venv'
# 3. Lea un archivo requirements.txt (créalo tú con al menos 3 paquetes)
# 4. Instale los paquetes en el entorno usando subprocess
# 5. Genere un informe en pantalla con los paquetes instalados y sus versiones
# Pista: usa subprocess.run() con capture_output=True para leer la salida de pip.
