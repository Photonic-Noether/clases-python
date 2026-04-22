# Clase 8 - Iteradores, generadores, comprensiones e itertools

## Antes de empezar: actualiza esta rama

> **Haz esto cada vez que abras el repositorio antes de mirar el código.**

```bash
git fetch origin
git reset --hard origin/Clase_8
```

Si hiciste algún commit accidental en esta rama, `git pull` fallará con un error de ramas divergentes. Este comando siempre funciona: descarga los últimos cambios y deja la rama en el estado correcto, pase lo que pase.

---
## ¿En qué rama estás?

Estás en la rama `Clase_8`, la última del curso. Cubre técnicas avanzadas de iteración en Python: el protocolo de iteradores, generadores con `yield`, comprensiones, serialización con `pickle` y `json`, y el módulo `itertools`.

## Cómo cambiar de rama

Para volver a la clase anterior, usa el comando:

```bash
git checkout Clase_7
```

Para ver el índice general del curso:

```bash
git checkout main
```

## Contenido de esta clase

Los notebooks en la carpeta `/codigo` cubren:

**Serialización:**
- `pickle`: `dumps()`, `loads()`, `dump()`, `load()` — serialización binaria de objetos Python
- `json`: `dumps()`, `loads()`, `dump()`, `load()` — serialización a formato texto universal
- Diferencias entre pickle (binario, solo Python) y JSON (texto, universal)

**Iteradores:**
- El protocolo de iteración: `__iter__()` y `__next__()`
- La excepción `StopIteration`
- Funciones `iter()` y `next()`
- Crear iterables personalizados: ejemplo con clase `Frase` e `IteradorFrases`

**Generadores:**
- La keyword `yield` y la evaluación perezosa (lazy evaluation)
- Generadores como funciones: más simples que clases iteradoras
- Ejemplo: generador de Fibonacci infinito
- Diferencia entre generadores e iteradores de clase

**Comprensiones:**
- Comprensión de lista: `[expr for x in iterable if condición]`
- Comprensión de conjunto: `{expr for x in iterable}`
- Comprensión de diccionario: `{clave: valor for x in iterable}`
- Expresión generadora: `(expr for x in iterable)` — perezosa, no crea lista
- Comprensiones anidadas

**itertools:**
- `chain()`, `chain.from_iterable()`: encadenar iterables
- `zip_longest()`: zip con relleno para iterables de distinto tamaño
- `islice()`: tomar un número limitado de elementos de un iterador
- Y más funciones del módulo

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!

## Proyecto propuesto (~30 minutos)

**Procesador de logs con generadores:**
Crea un pipeline de procesamiento de texto usando generadores encadenados: un generador que lea líneas de un archivo una a una, otro que filtre las líneas vacías, otro que normalice (minúsculas, sin espacios extra), y uno final que cuente las palabras de cada línea. Une todo con `itertools.chain` si procesas varios archivos. Guarda el resultado (lista de `{linea, num_palabras}`) como JSON.

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
