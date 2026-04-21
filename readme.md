# Clase 7 - Archivos y biblioteca estándar de Python

## ¿En qué rama estás?

Estás en la rama `Clase_7`, que cubre el trabajo con archivos en Python y varios módulos de la biblioteca estándar: `random`, `sys`, `pathlib` y `shutil`. También se repasa la orientación a objetos.

## Cómo cambiar de rama

Para moverte a otra clase, usa el comando:

```bash
git checkout Clase_8
```

Para volver a la clase anterior:

```bash
git checkout Clase_6
```

## Contenido de esta clase

Los notebooks en la carpeta `/codigo` cubren:

**Archivos (I/O):**
- La función `open(<archivo>, <modo>)` y sus modos: `r`, `w`, `a`, `x`, `b`, `t`
- Métodos de archivo: `.close()`, `.read()`, `.readline()`, `.readlines()`, `.write()`, `.writelines()`, `.tell()`, `.seek()`
- Context managers con `with open(...) as archivo:` (cierre automático)

**Biblioteca estándar:**
- `random`: `random()`, `uniform()`, `randint()`, `seed()`, `choice()`, `shuffle()`, `sample()`
- `sys`: `version`, `platform`, `executable`, `argv`, `exit()`, `getsizeof()`, `modules`, `path`
- `pathlib`: `Path()`, operador `/` para construir rutas, `.resolve()`, `.joinpath()`, `.parent`, `.name`, `.stem`, `.suffix`, `.iterdir()`, `.is_dir()`, `.is_file()`, `.stat()`
- `shutil`: `copyfile()`, `copy2()`, `copytree()`, `rmtree()`, `move()`, `which()`

**Ejemplo práctico:**
- Clase `Carta` y `Baraja` usando OOP + `random.shuffle()`

**Orientación a objetos (repaso):**
- Clases, herencia, `super()` y excepciones personalizadas

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
4. **Clase 4** - Funciones avanzadas: `*args`, `**kwargs` y type hints
5. **Clase 5** - Funciones completas: funciones de orden superior y closures
6. **Clase 6** - Orientación a objetos, herencia y excepciones
7. **Clase 7** - Archivos, módulos y biblioteca estándar de Python
8. **Clase 8** - Iteradores, generadores, comprensiones e itertools
