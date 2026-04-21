# Clase 5 - Funciones completas

## ¿En qué rama estás?

Estás en la rama `Clase_5`, que cierra el bloque de funciones en Python: repaso completo de `*args`, `**kwargs`, type hints modernos (`int|float`, `list[int]`), funciones de orden superior, closures y expresiones lambda.

## Cómo cambiar de rama

Para moverte a otra clase, usa el comando:

```bash
git checkout Clase_6
```

Para volver a la clase anterior:

```bash
git checkout Clase_4
```

## Contenido de esta clase

Los notebooks en la carpeta `/codigo` cubren:

**Funciones (bloque completo):**
- Repaso y consolidación de todos los tipos de parámetros
- Type hints modernos: `int | float`, `list[int]`, `dict[str, int]`
- `*args` y `**kwargs` en profundidad
- Funciones lambda: casos de uso reales con `sorted()`, `map()`, `filter()`
- Funciones de orden superior: funciones que reciben y devuelven funciones
- Closures: funciones que recuerdan el estado de su entorno de definición
- `nonlocal` para modificar variables de funciones envolventes
- Regla LEGB completa con ejemplos prácticos

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!

## Proyecto propuesto (~30 minutos)

**Sistema de filtros para una lista de productos:**
Crea una lista de diccionarios que represente productos `{nombre, precio, categoria, disponible}`. Implementa funciones de filtrado que reciban la lista y criterios como `**kwargs` (por ejemplo, `categoria="electronica"`, `precio_max=100`, `disponible=True`). Combínalas usando una función `aplicar_filtros(productos, *filtros)` que encadene los filtros con lambdas.

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
