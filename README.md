# Proyecto Final Javier Juárez Montiel 2164665  — Programación Básica



Este repositorio reúne lo que trabajamos durante el semestre en **Programación Básica**. El proyecto es una calculadora en Python organizada por módulos que, además de hacer operaciones básicas y estadísticas, guarda un registro en CSV, entiende instrucciones escritas en texto normal y genera gráficas automáticamente usando **Matplotlib**.

---

## 1. ¿Qué hace el código?

El proyecto se divide en varias funciones principales dependiendo del archivo que ejecutes:

* **Calculadora interactiva (`main.py`):** Te muestra un menú en consola, te pide elegir una operación (`suma`, `resta`, `multiplicacion` o `division`) y dos números. Cada vez que haces un cálculo, guarda la operación en `historial.csv` y actualiza automáticamente una imagen llamada `grafica_sesion.png` con el conteo de las operaciones que llevas hechas.
* **Calculadora con lenguaje natural (`main_regex.py`):** Hace lo mismo que `main.py`, pero en lugar de escribir solo el nombre exacto de la operación, puedes escribir frases como *"suma 10 y 5"* o *"multiplica 4 por 3"*. Además, aquí también puedes pedir operaciones estadísticas (`promedio`, `mediana`, `moda`) que se calculan usando los resultados anteriores de tu sesión.
* **Lectura desde archivos (`main_archivo.py`):** En vez de pedir datos por teclado, lee una lista de operaciones desde un archivo `.csv` (como `csvs/programa.csv`) o `.json` (como `jsons/programa.json`) y las va resolviendo una por una.
* **Gráficas con Matplotlib (`matematicas/graficas/` y `ejemplo.py`):**
  * **Gráficas de la sesión:** Cada vez que corres `main.py` o `main_regex.py`, la función `graficar_historial()` revisa cuántas veces usaste cada operación y genera dos gráficas lado a lado (una de pastel y otra de barras) guardándolas en `grafica_sesion.png`.
  * **Script de ejemplo (`ejemplo.py`):** Es el ejercicio de visualización con `matplotlib` y `numpy`. Crea una sola imagen (`grafica.png`) dividida en tres paneles:
    1. Una recta ($y = x$) junto con una onda senoidal ($y = \sin(x)$) y sus límites en $1$ y $-1$.
    2. Una parábola ($y = x^2$) dibujada de tres formas distintas para comparar qué tan suave se ve según la cantidad de puntos (`range`, `np.arange` y `np.linspace`).
    3. Una gráfica de pastel con porcentajes para tres categorías de operaciones.

---

## 2. ¿Cómo fue construido?

Para no tener todo amontonado en un solo archivo, el código está separado en carpetas (paquetes de Python) usando archivos `__init__.py`:

```text
programacionBasica/
├── .python-version              # Versión de Python usada (3.10)
├── README.md                    # Documentación del proyecto
├── main.py                      # Ejecución principal por menú en consola
├── main_regex.py                # Ejecución escribiendo frases en lenguaje natural
├── main_archivo.py              # Ejecución leyendo archivos CSV o JSON
├── ejemplo.py                   # Ejercicio independiente de gráficas con Matplotlib y NumPy
├── historial.csv                # Archivo donde se van guardando las operaciones hechas
├── grafica_sesion.png           # Gráfica de barras y pastel generada durante la sesión
├── hola.png                     # Imagen de prueba generada con Matplotlib
├── csvs/
│   └── programa.csv             # Ejemplo de operaciones en formato CSV
├── jsons/
│   └── programa.json            # Ejemplo de operaciones en formato JSON
├── es/                          # Módulo de Entrada y Salida de datos
│   ├── __init__.py
│   ├── entrada.py               # Valida números/opciones, lee CSV/JSON y aplica regex
│   └── salida.py                # Guarda el historial en formato CSV
└── matematicas/                 # Módulo principal con toda la lógica matemática
    ├── __init__.py              # Junta las operaciones de aritmética y estadística
    ├── aritmetica/              # Operaciones básicas
    │   ├── __init__.py
    │   ├── suma.py
    │   ├── resta.py
    │   ├── multiplicacion.py
    │   └── division.py
    ├── estadistica/             # Cálculos estadísticos
    │   ├── __init__.py
    │   ├── promedio.py
    │   ├── mediana.py
    │   ├── moda.py
    │   └── frequencia.py
    └── graficas/                # Creación de gráficas con Matplotlib
        ├── __init__.py
        ├── barras.py
        └── pastel.py
