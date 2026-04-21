# Clase 5 - Módulos, paquetes y entornos virtuales

## ¿En qué rama estás?

Estás en la rama `Clase_5`, que cubre cómo organizar el código Python en módulos y paquetes, gestionar dependencias con `pip` y crear entornos virtuales con `venv`.

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

**Módulos:**
- Qué es un módulo: un archivo `.py` con código reutilizable
- `import`, `from ... import`, `import ... as`
- Imports relativos y absolutos
- Import circular: qué es y cómo evitarlo

**Paquetes:**
- Qué es un paquete: directorio con `__init__.py`
- Estructura de un proyecto Python
- Imports dentro de paquetes

**Gestión de dependencias:**
- `pip`: `install`, `uninstall`, `upgrade`, `list`, `show`, `freeze`
- `requirements.txt`: generar e instalar desde él

**Entornos virtuales:**
- Por qué usar entornos virtuales (aislar dependencias por proyecto)
- Crear y activar un entorno con `venv`
- Instalar paquetes en el entorno virtual

**Archivos de configuración:**
- `.ini` / `.cfg` con `configparser`
- `.env` con `python-dotenv`
- `.yaml` y `.toml` (visión general)

## Ejercicios propuestos

En el archivo `ejercicios.py` encontrarás 3 ejercicios propuestos para practicar. Son de dificultad ligeramente superior al temario y no tienen solución: ¡intenta resolverlos tú!

## Proyecto propuesto (~30 minutos)

**Gestor de configuración de aplicación:**
Crea un paquete `config/` con un módulo `settings.py` que lea parámetros de un archivo `.ini` usando `configparser`. El archivo `.ini` debe tener secciones como `[database]`, `[app]`, `[logging]`. El módulo expone una función `get(seccion, clave)` y otra `set(seccion, clave, valor)` que persiste los cambios. Crea un script `main.py` que use el paquete y demuestre la lectura y escritura de configuración.

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
