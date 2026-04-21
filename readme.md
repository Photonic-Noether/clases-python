# Clase 4 - Funciones avanzadas

## ¿En qué rama estás?

Estás en la rama `Clase_4`, que profundiza en las funciones de Python: `*args`, `**kwargs`, type hints, docstrings y funciones como ciudadanos de primera clase (callbacks y funciones de orden superior).

## Cómo cambiar de rama

Para moverte a otra clase, usa el comando:

```bash
git checkout Clase_5
```

Para volver a la clase anterior:

```bash
git checkout Clase_3
```

## Contenido de esta clase

Los notebooks en la carpeta `/codigo` cubren:

**Funciones (avanzado):**
- Repaso: `def`, parámetros, `return`
- Parámetros posicionales vs keyword, valores por defecto
- Parámetros solo-posicionales (`/`) y solo-keyword (`*`)
- `*args`: número variable de argumentos posicionales
- `**kwargs`: número variable de argumentos keyword
- Desempaquetado de argumentos con `*` y `**` en la llamada
- Type hints: `param: tipo -> tipo_retorno` y `list[int]`, etc.
- Docstrings en estilo Google
- Funciones de orden superior: funciones que reciben o devuelven funciones
- Regla LEGB y ámbito de variables
- `global` y `nonlocal`
- Funciones lambda

**Colecciones (repaso):**
- Slicing, métodos de listas, sets y diccionarios

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!

## Proyecto propuesto (~30 minutos)

**Constructor de consultas dinámico:**
Crea una función `construir_query(tabla: str, campos: list[str] = None, **condiciones)` que genere una cadena SQL de tipo `SELECT campo1, campo2 FROM tabla WHERE clave1='valor1' AND clave2=valor2`. Si `campos` es `None`, usa `SELECT *`. Maneja correctamente strings (entre comillas simples) y números. Pruébala con al menos 3 casos distintos.

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
