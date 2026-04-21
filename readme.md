# Clase 7 - Biblioteca estándar de Python

## ¿En qué rama estás?

Estás en la rama `Clase_7`, que hace un recorrido por 10 módulos sencillos y muy útiles de la biblioteca estándar de Python, todos disponibles sin instalar nada.

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

El notebook en la carpeta `/codigo` cubre los siguientes módulos:

| Módulo | Para qué sirve |
|--------|----------------|
| `datetime` | Fechas, horas e intervalos de tiempo |
| `math` | Funciones matemáticas y constantes (π, e, sqrt, factorial...) |
| `os` | Sistema operativo, directorios y variables de entorno |
| `collections` | `Counter`, `defaultdict`, `namedtuple`, `deque` |
| `time` | Medir tiempo de ejecución, pausas y timestamps |
| `string` | Constantes de caracteres y templates de texto |
| `re` | Búsqueda y validación con expresiones regulares |
| `functools` | `partial`, `reduce` y `lru_cache` |
| `copy` | Copia superficial (`copy`) y profunda (`deepcopy`) de objetos |
| `pprint` | Mostrar estructuras de datos complejas de forma legible |

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!

## Proyecto propuesto (~30 minutos)

**Analizador de texto:**
Crea un programa que lea un archivo de texto (puedes usar cualquier texto largo) y genere un informe usando varios módulos de esta clase:
- Con `re`: cuenta palabras, oraciones y párrafos; extrae todos los emails o URLs presentes.
- Con `collections.Counter`: muestra las 10 palabras más frecuentes (ignorando palabras cortas y puntuación).
- Con `datetime` y `time`: registra cuándo se analizó y cuánto tardó.
- Muestra el informe con `pprint` y guárdalo en un archivo `.txt`.

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
