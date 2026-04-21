# Clase 6 - Orientación a objetos, excepciones y módulos

## ¿En qué rama estás?

Estás en la rama `Clase_6`, que introduce la Programación Orientada a Objetos (POO) en Python: clases, instancias, herencia, `super()`, manejo de excepciones y organización del código en módulos y paquetes.

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

**Orientación a objetos:**
- Clases y objetos: todo en Python es un objeto
- Constructor `__init__()` y el parámetro `self`
- Atributos de instancia y atributos de clase
- Métodos: funciones que pertenecen a una clase
- Ejemplo práctico: sistema de combate con clase `Personaje`
- Herencia: `class Hijo(Padre):` para extender clases
- El problema del diamante y herencia múltiple
- `super()` para llamar a métodos de la clase padre
- Orden de resolución de métodos (MRO): `__mro__`

**Manejo de errores:**
- Bloques `try / except / else / finally`
- Capturar excepciones específicas y genéricas
- `raise` para lanzar errores manualmente
- Crear excepciones personalizadas (heredando de `Exception`)
- Ejemplo: `CuentaBancaria` con excepción `RetiradaIncorrecta`

**Módulos y paquetes:**
- Módulos: archivos `.py` con código reutilizable
- `import`, `from ... import`, `import ... as`
- Imports relativos y absolutos
- Import circular: qué es y cómo evitarlo
- Paquetes: directorios con `__init__.py`
- Gestión de paquetes con `pip`
- Entornos virtuales con `venv`
- Archivos de configuración: `.ini`, `.env`, `.yaml`, `.toml`

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!

## Proyecto propuesto (~30 minutos)

**Sistema de gestión de biblioteca:**
Crea clases `Libro(titulo, autor, isbn, disponible)` y `Biblioteca`. La biblioteca gestiona una lista de libros y permite: prestar (marca como no disponible), devolver, buscar por título o autor, y listar disponibles. Define una excepción `LibroNoDisponible` que se lanza al intentar prestar un libro ya prestado. Incluye un menú de consola.

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
