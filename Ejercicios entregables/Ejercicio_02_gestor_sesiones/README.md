# Gestor de Sesiones de Aula (`SesionAula`)

Práctica integradora correspondiente al **RA1 (criterios d, e y f)** de Programación Orientada a Objetos en Python.

---

## 1. Explicación del modelo

El modelo gira en torno a la clase `SesionAula`, diseñada para representar el uso de un aula durante una clase y gestionar de forma segura el fichero de registro (*log*) asociado a dicha sesión.

* **Estado de la sesión:** Cada sesión almacena los datos básicos (`aula`, `profesor`, `alumnos`, `log_path`) junto con dos atributos internos (`_log` y `_cerrada`) que controlan el ciclo de vida del fichero.
* **Validación temprana:** Antes de permitir la creación del objeto, el constructor verifica que los datos cumplan las reglas de negocio (textos no vacíos y número de alumnos estrictamente positivo), evitando objetos en estados inconsistentes.
* **Protocolo de gestor de contexto:** La clase implementa `__enter__` y `__exit__` para asegurar que el fichero se abra únicamente al entrar en un bloque `with` y se cierre de forma determinista al salir, independientemente de si ocurren errores durante la ejecución.

---

## 2. Diferencia entre clase e instancia

En Python, la relación entre clase e instancia sigue el principio de **molde frente a objeto concreto**:

| Aspecto | Clase (`SesionAula`) | Instancia (`sesion1`, `sesion2`) |
| :--- | :--- | :--- |
| **Naturaleza** | Plantilla o molde que define estructura y comportamiento. | Objeto concreto creado a partir de la clase. |
| **Tipo (`type`)** | `<class 'type'>` (en Python, las clases también son objetos). | `<class '__main__.SesionAula'>`. |
| **Atributos** | **Atributos de clase** (`centro`, `total_sesiones`), compartidos por todas las instancias. | **Atributos de instancia** (`aula`, `profesor`, etc.), almacenados en su propio diccionario `__dict__`. |
| **Resolución** | Si se modifica `sesion1.centro`, Python crea un atributo en el `__dict__` de `sesion1` que "tapa" al de clase sin afectar a `sesion2` ni a `SesionAula`. | Si una instancia no tiene un atributo propio, Python lo busca automáticamente en el espacio de nombres de la clase. |

---

## 3. Explicación de `__new__`, `__init__` y `__del__`

El ciclo de vida completo de un objeto en Python involucra tres métodos especiales:

1. **`__new__(cls, ...)` (Creación):** Es el verdadero constructor. Se ejecuta en primer lugar, recibe la clase (`cls`) y se encarga de reservar memoria y crear la instancia vacía antes de devolverla. En esta práctica no se sobrescribe porque el comportamiento estándar heredado de `object` es suficiente.
2. **`__init__(self, ...)` (Inicialización):** Se ejecuta automáticamente justo después de `__new__`. Recibe la instancia recién creada (`self`), valida los parámetros de entrada, inicializa sus atributos en `__dict__` e incrementa el contador de clase `total_sesiones`. No debe devolver ningún valor distinto de `None`.
3. **`__del__(self)` (Destructor):** Se invoca cuando el objeto está a punto de ser destruido en memoria al quedarse sin referencias. En `SesionAula` se utiliza únicamente como red de seguridad para imprimir un aviso por consola si la sesión se destruye con `_cerrada == False`.

---

## 4. Justificación del uso de `with`

Recursos externos del sistema operativo como ficheros, sockets o conexiones a bases de datos son limitados y requieren **liberación determinista** (cerrarse exactamente en el instante en que dejan de utilizarse).

El uso de la sentencia `with` garantiza:
* **Apertura controlada (`__enter__`):** El fichero solo se abre cuando comienza el bloque de trabajo y se devuelve la instancia lista para operar mediante `as`.
* **Cierre garantizado (`__exit__`):** Al finalizar el bloque `with`, Python ejecuta `__exit__` de manera automática **tanto si el bloque termina con éxito como si se lanza una excepción en su interior**. De este modo se evitan fugas de recursos (*resource leaks*) y pérdida de datos por búferes sin vaciar.

---

## 5. Ejemplos de ejecución

Al ejecutar `python sesion_aula.py`, se obtiene una salida por consola similar a la siguiente:

```text
--- Inspección de tipos y espacios de nombres ---
type(SesionAula): <class 'type'>
type(sesion1): <class '__main__.SesionAula'>
isinstance(sesion1, SesionAula): True
__dict__ de sesion1: {'aula': 'AULA 101', 'profesor': 'Laura Gómez', 'alumnos': 25, 'log_path': 'sesion1.txt', '_log': None, '_cerrada': False}
__dict__ de sesion2: {'aula': 'AULA 202', 'profesor': 'Carlos Ruiz', 'alumnos': 18, 'log_path': 'sesion2.txt', '_log': None, '_cerrada': False}

--- Atributo de clase vs de instancia ---
Centro (clase): CFGS Python
Centro visto desde sesion1: CFGS Python
Centro visto desde sesion2: CFGS Python
Tras modificar sesion1.centro:
sesion1.centro: CFGS Python - Turno Tarde
sesion2.centro: CFGS Python
SesionAula.centro: CFGS Python

--- Uso normal de with ---
¿sesion1 cerrada correctamente?: True

--- Uso de with con excepción ---
Excepción capturada fuera del with: Fallo simulado en el proyector
¿sesion2 cerrada tras el error?: True

--- Total de sesiones creadas ---
Total sesiones: 2
```

### Ficheros generados

**Contenido de `sesion1.txt` (ejecución normal):**
```text
Inicio de registro: AULA 101 | Profesor: Laura Gómez | Alumnos: 25
Explicación de gestores de contexto
Ejercicios prácticos realizados
Fin de registro de la sesión
```

**Contenido de `sesion2.txt` (ejecución con excepción capturada en `__exit__`):**
```text
Inicio de registro: AULA 202 | Profesor: Carlos Ruiz | Alumnos: 18
Inicio de práctica en laboratorio
Error en la sesión: ValueError
```

---

## 6. Limitaciones de `__del__`

Confiar en `__del__` como mecanismo principal para cerrar ficheros o liberar recursos es una mala práctica en Python debido a las siguientes limitaciones:

* **Ejecución no determinista:** Aunque CPython utiliza conteo de referencias, si existen referencias circulares entre objetos la destrucción depende del recolector de basura cíclico (`gc`), cuyo momento de ejecución es impredecible.
* **Apagado del intérprete:** Al finalizar un programa, el orden en que se destruyen los objetos y módulos globales no está garantizado; algunos recursos o funciones internas como `open` o `print` pueden no estar disponibles, provocando errores si no se protegen con bloques `try...except`.
* **Silenciamiento de excepciones:** Cualquier excepción lanzada dentro de `__del__` es ignorada por Python (solo imprime un aviso en `stderr`), lo que dificulta detectar fallos reales durante el cierre de un recurso.