# Clase 6 - Archivos y context managers

## ¿En qué rama estás?

Estás en la rama `Clase_6`, que cubre el trabajo con archivos en Python: lectura, escritura, context managers y algunos módulos útiles de la biblioteca estándar relacionados con el sistema de archivos.

## Cómo cambiar de rama

Para moverte a otra clase, usa el comando:

```bash
git checkout Clase_7
```

Para volver a la clase anterior:

```bash
git checkout Clase_5
```

## Contenido de esta clase

Los notebooks en la carpeta `/codigo` cubren:

**Archivos (I/O):**
- La función `open(<archivo>, <modo>)` y sus modos: `r`, `w`, `a`, `x`, `b`, `t`
- Métodos de archivo: `.close()`, `.read()`, `.readline()`, `.readlines()`, `.write()`, `.writelines()`, `.tell()`, `.seek()`
- Context managers con `with open(...) as archivo:` (cierre automático)

**Módulos de sistema de archivos:**
- `pathlib`: `Path()`, operador `/` para construir rutas, `.resolve()`, `.parent`, `.name`, `.stem`, `.suffix`, `.iterdir()`, `.is_dir()`, `.is_file()`, `.stat()`
- `shutil`: `copyfile()`, `copy2()`, `copytree()`, `rmtree()`, `move()`, `which()`
- `sys`: información del intérprete, `argv`, `path`, `exit()`
- `random`: generación de números y selecciones aleatorias

**Ejemplo práctico:**
- Clase `Carta` y `Baraja` usando OOP + `random.shuffle()`

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!

## Proyecto propuesto (~30 minutos)

**Organizador automático de archivos:**
Usando `pathlib` y `shutil`, crea un script que recorra un directorio dado por el usuario, clasifique los archivos por extensión en subdirectorios (por ejemplo, `imagenes/`, `documentos/`, `codigo/`, `otros/`) y los mueva allí. Imprime un resumen con cuántos archivos movió a cada categoría y el espacio total procesado.

---

## Índice cronológico completo del temario

1. **Clase 1** - Variables, tipos de datos y control de flujo
2. **Clase 2** - Colecciones avanzadas: slicing, métodos y operaciones
3. **Clase 3** - Funciones: definición, parámetros, ámbito y lambdas
4. **Clase 4** - Orientación a objetos, herencia y excepciones
5. **Clase 5** - Módulos, paquetes y entornos virtuales
6. **Clase 6** - Archivos y context managers
7. **Clase 7** - Biblioteca estándar de Python
8. **Clase 8** - Iteradores, generadores, comprensiones e itertools
