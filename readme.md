# Clase 3 - Funciones

## ¿En qué rama estás?

Estás en la rama `Clase_3`, que introduce las funciones en Python: cómo definirlas, los distintos tipos de parámetros, el ámbito de variables (LEGB), lambdas y funciones de orden superior.

## Cómo cambiar de rama

Para moverte a otra clase, usa el comando:

```bash
git checkout Clase_4
```

Para volver a la clase anterior:

```bash
git checkout Clase_2
```

## Contenido de esta clase

Los notebooks en la carpeta `/codigo` cubren:

**Funciones:**
- Definición con `def` y llamada de funciones
- Tipos de funciones según parámetros y retorno
- Parámetros posicionales y por nombre (keyword)
- Parámetros con valor por defecto
- Parámetros solo-posicionales (`/`) y solo-keyword (`*`)
- Unpacking de argumentos: `*args` y `**kwargs`
- Type hints y anotaciones de tipo
- Docstrings (estilo Google)
- Funciones de orden superior y callbacks
- Regla LEGB: ámbito Built-in, Global, Enclosing, Local
- Keywords `global` y `nonlocal`
- Introspección con `globals()` y `locals()`
- Funciones lambda (anónimas)

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!

## Proyecto propuesto (~30 minutos)

**Calculadora científica modular:**
Crea un diccionario de operaciones `{"+": sumar, "-": restar, "*": multiplicar, "/": dividir, "^": potencia, "raiz": raiz_cuadrada}` donde cada valor es una función. Implementa un bucle que pida operación y operandos, ejecute la función correspondiente y muestre el resultado. Añade validación de errores (división por cero, raíz de negativos) usando las funciones con manejo de casos especiales.

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
