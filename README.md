# Curso de Python - Tajamar

Bienvenido al repositorio del curso de Python. Aquí encontrarás todos los apuntes, ejemplos de código y ejercicios organizados por clases.

---

## ¿Cómo está organizado este repositorio?

El contenido del curso está repartido en **ramas de Git** (branches), una por cada clase. Cada rama contiene:

- **`/codigo/`** — Notebooks de Jupyter (`.ipynb`) con los apuntes y ejemplos de código de la clase.
- **`ejercicios.py`** — 3 ejercicios propuestos para practicar por tu cuenta, sin solución.
- **`readme.md`** — Descripción de la rama: temario, cómo cambiar de rama, ejercicios y proyecto propuesto.

Esta rama (`main`) es la raíz del proyecto y no contiene código de clase.

---

## Cómo navegar entre clases

Para ver el contenido de una clase específica, cambia a su rama con:

```bash
git checkout Clase_1
```

Sustituye `Clase_1` por la rama que quieras. Las ramas disponibles son:

| Rama | Contenido |
|------|-----------|
| `Clase_1` | Variables, tipos de datos y control de flujo |
| `Clase_2` | Colecciones avanzadas: slicing, métodos y operaciones |
| `Clase_3` | Funciones: definición, parámetros, ámbito y lambdas |
| `Clase_4` | Orientación a objetos, herencia y excepciones |
| `Clase_5` | Módulos, paquetes y entornos virtuales |
| `Clase_6` | Archivos y context managers |
| `Clase_7` | Biblioteca estándar de Python |
| `Clase_8` | Iteradores, generadores, comprensiones e itertools |

Para volver a la rama principal:

```bash
git checkout main
```

Para ver todas las ramas disponibles:

```bash
git branch -a
```

---

## Temario completo del curso

### Clase 1 — Variables, tipos de datos y control de flujo
- I/O básico: `print()` e `input()`
- Variables y asignación
- Tipos básicos: `int`, `float`, `bool`, `str`, `None`
- Operadores aritméticos y lógicos
- Métodos de strings, f-strings y caracteres de escape
- Colecciones: listas, tuplas, conjuntos y diccionarios
- Mutabilidad e inmutabilidad
- Asignaciones aumentadas (`+=`, `-=`, etc.)
- Funciones integradas: `abs()`, `max()`, `min()`, `len()`, `range()`
- Bucles `while` y `for`, bucles anidados
- Condicionales `if / elif / else` y operador ternario

### Clase 2 — Colecciones avanzadas
- Slicing: `[inicio:fin:paso]`, índices negativos
- Operadores `+` y `*` en secuencias
- Métodos de listas: `.append()`, `.insert()`, `.extend()`, `.pop()`, `.sort()`, etc.
- Unpacking con `*variable` y el placeholder `_`
- Operaciones de sets: `-`, `^`, `&`, `|`
- Métodos de diccionarios: `.get()`, `.setdefault()`, `.keys()`, `.values()`, `.items()`, `.fromkeys()`
- Fusión de diccionarios con el operador `|`

### Clase 3 — Funciones
- Definición con `def` y llamada de funciones
- 4 tipos de funciones según parámetros y retorno
- Parámetros posicionales, keyword, con valor por defecto
- Parámetros solo-posicionales (`/`) y solo-keyword (`*`)
- `*args` y `**kwargs`
- Type hints y docstrings (estilo Google)
- Funciones de orden superior y callbacks
- Regla LEGB: Built-in, Global, Enclosing, Local
- Keywords `global` y `nonlocal`
- Funciones lambda

### Clase 4 — Orientación a objetos, herencia y excepciones
- Clases, instancias, `__init__()` y `self`
- Atributos de instancia y de clase
- Métodos y ejemplo práctico con sistema de combate
- Herencia: `class Hijo(Padre):`
- El problema del diamante y herencia múltiple
- `super()` y orden de resolución de métodos (MRO)
- `try / except / else / finally`
- `raise` para lanzar errores manualmente
- Excepciones personalizadas (heredando de `Exception`)

### Clase 5 — Módulos, paquetes y entornos virtuales
- Módulos: `import`, `from ... import`, alias con `as`
- Paquetes con `__init__.py` y estructura de directorios
- Gestión de paquetes con `pip`
- Entornos virtuales con `venv`: creación, activación y uso
- Proyecto completo integrando todo lo visto hasta la clase

### Clase 6 — Archivos y context managers
- `open()` y sus modos: `r`, `w`, `a`, `x`, `b`, `t`
- Métodos de archivo: `.read()`, `.readline()`, `.write()`, `.seek()`, etc.
- Context managers: `with open(...) as archivo:`
- `random`: generación de números y selecciones aleatorias
- `sys`: información del intérprete y argumentos del programa
- `pathlib`: trabajo con rutas de forma multiplataforma
- `shutil`: copiar, mover y eliminar archivos y directorios

### Clase 7 — Biblioteca estándar de Python
- `datetime`: fechas, horas, duraciones y operaciones con `timedelta`
- `math`: constantes y funciones matemáticas
- `os`: información del sistema y variables de entorno
- `collections`: `Counter`, `defaultdict`, `OrderedDict`, `namedtuple`, `deque`
- `time`: medición de tiempo y pausas con `sleep`
- `string`: constantes de caracteres y `Template`
- `re`: expresiones regulares — `match`, `search`, `findall`, `sub`
- `functools`: `reduce`, `partial`, `lru_cache`
- `copy`: copias superficiales y profundas con `copy` y `deepcopy`
- `pprint`: impresión legible de estructuras de datos

### Clase 8 — Iteradores, generadores, comprensiones e itertools
- Serialización con `pickle` y `json`
- Protocolo de iteración: `__iter__()`, `__next__()`, `StopIteration`
- Iterables personalizados
- Generadores con `yield` y evaluación perezosa
- Generadores como funciones vs clases iteradoras
- Comprensiones: de lista, conjunto, diccionario y expresión generadora
- Comprensiones anidadas
- `itertools`: `chain()`, `zip_longest()`, `islice()` y más

---

## Objetivos de aprendizaje

Al completar este curso, serás capaz de:

- **Escribir código Python idiomático**: usar las estructuras de datos correctas, comprensiones, type hints y docstrings.
- **Diseñar funciones reutilizables**: con parámetros flexibles (`*args`, `**kwargs`), lambdas y funciones de orden superior.
- **Modelar problemas con POO**: crear jerarquías de clases con herencia, encapsulación y excepciones propias.
- **Organizar proyectos Python**: estructura de módulos y paquetes, entornos virtuales y gestión de dependencias.
- **Trabajar con el sistema de archivos**: leer y escribir archivos, serializar datos con JSON/pickle y manejar rutas con `pathlib`.
- **Aprovechar la biblioteca estándar**: usar módulos como `datetime`, `collections`, `re`, `functools` y más sin dependencias externas.
- **Procesar datos de forma eficiente**: usando generadores, comprensiones e `itertools` para evitar cargar todo en memoria.

---

## Requisitos previos

- Tener Python 3.10 o superior instalado.
- Tener Jupyter instalado para abrir los notebooks (o usar VS Code con la extensión de Jupyter).

```bash
pip install jupyter
jupyter notebook
```

---

## Recursos adicionales

- [Documentación oficial de Python](https://docs.python.org/es/3/)
- [Python Tutor](https://pythontutor.com/) — Visualiza la ejecución de tu código paso a paso
- [Codewars](https://www.codewars.com/) — Practica con katas de programación
- [Real Python](https://realpython.com/) — Tutoriales y artículos en profundidad
