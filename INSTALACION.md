# Instalación y ejecución

Guía paso a paso para instalar y ejecutar el **planificador de rutas del Metro CDMX con A\*** desde cero, en **Windows** y en **Linux**. La instalación es corta: basta con instalar Python, las dos librerías del proyecto y ejecutar el script.

> Los pasos de Linux están redactados para **Ubuntu y Debian**. En otras distribuciones los paquetes son equivalentes, pero los comandos pueden variar. En macOS el procedimiento es similar (se recomienda el Python oficial de python.org, que incluye Tkinter), pero no se describe aquí.

Para conocer cómo funciona el programa (el grafo, el algoritmo A\* y la arquitectura), consulta el [README](README.md).

## Índice

- [Resumen rápido](#resumen-rápido)
- [Requisitos](#requisitos)
- [Instalar Python](#instalar-python)
- [Descargar el proyecto](#descargar-el-proyecto)
- [Instalar las librerías](#instalar-las-librerías)
- [Ejecutar la aplicación](#ejecutar-la-aplicación)
- [Probar la aplicación](#probar-la-aplicación)
- [Solución de problemas](#solución-de-problemas)

## Resumen rápido

**Windows (PowerShell)**, con [Python instalado](#instalar-python) y la casilla *Add python.exe to PATH* marcada:

```powershell
git clone https://github.com/DaniCaste10/metro-cdmx-aestrella.git
cd metro-cdmx-aestrella
pip install networkx matplotlib
python metro_aestrella.py
```

**Linux (Ubuntu/Debian)**:

```bash
sudo apt update
sudo apt install -y git python3 python3-tk python3-networkx python3-matplotlib
git clone https://github.com/DaniCaste10/metro-cdmx-aestrella.git
cd metro-cdmx-aestrella
python3 metro_aestrella.py
```

Se abrirá una ventana con el mapa del metro. Si es la primera vez que haces esto, sigue la guía completa a continuación.

## Requisitos

| Software | Versión | Para qué se usa | Dónde obtenerlo |
|---|---|---|---|
| **Python** | 3.10 o superior (se recomienda la 3.12 o más reciente) | Ejecutar el programa | https://www.python.org/downloads/ |
| **Tkinter** | Incluido con Python en Windows. En Linux es un paquete aparte (`python3-tk`). | Interfaz gráfica | Viene con Python |
| **NetworkX** | Cualquier versión reciente | Grafo y algoritmo A* | `pip` o `apt` |
| **Matplotlib** | Cualquier versión reciente | Dibujo del mapa | `pip` o `apt` |
| **Git** | Cualquiera reciente | Descargar el proyecto (opcional: también se puede bajar como ZIP) | https://git-scm.com/downloads |

Además, se necesita un **entorno gráfico** (el escritorio de Windows o de Linux), porque la aplicación abre una ventana, y **conexión a Internet** para descargar el proyecto y las librerías.

## Instalar Python

**Windows**

1. Entra en https://www.python.org/downloads/windows/ y descarga el instalador de Windows (64-bit) de la versión estable más reciente de Python 3.
2. Ejecuta el instalador. En la **primera pantalla**, marca la casilla **Add python.exe to PATH** (está en la parte inferior) y pulsa **Install Now**. Con esa opción se instala también Tkinter (aparece como *tcl/tk and IDLE*) y `pip`.
3. Al terminar, abre una terminal **nueva** (PowerShell) y comprueba la instalación:

```powershell
python --version
```

Debe mostrar una versión 3.10 o superior. Si PowerShell responde que `python` no se reconoce, consulta [Solución de problemas](#solución-de-problemas).

**Linux (Ubuntu/Debian)**

Python ya viene instalado en Ubuntu y Debian. Lo único que falta es **Tkinter**, que en Linux no se incluye con Python, y se instala en el paso [Instalar las librerías](#instalar-las-librerías). Comprueba la versión:

```bash
python3 --version
```

Debe mostrar una versión 3.10 o superior (Ubuntu 22.04 incluye la 3.10 y Ubuntu 24.04 la 3.12).

## Descargar el proyecto

El código está en un repositorio de GitHub. Hay dos formas de obtenerlo.

### Opción A: clonar el repositorio con Git (recomendada)

1. Instala Git si no lo tienes.
   - **Windows**: descarga el instalador desde https://git-scm.com/download/win y acepta las opciones por defecto. Después, abre una terminal **nueva**.
   - **Linux**: `sudo apt install -y git`.
2. Abre la página del repositorio en GitHub, pulsa el botón verde **Code**, selecciona la pestaña **HTTPS** y copia la URL. Tiene la forma `https://github.com/DaniCaste10/metro-cdmx-aestrella.git`.
3. Elige una carpeta donde guardar el proyecto. Es preferible que la ruta **no contenga espacios ni acentos** y que **no esté dentro de una carpeta sincronizada con OneDrive** (como `Escritorio` o `Documentos`).
4. Clona el repositorio.

**Windows (PowerShell)**

```powershell
mkdir C:\proyectos
cd C:\proyectos
git clone https://github.com/DaniCaste10/metro-cdmx-aestrella.git
cd metro-cdmx-aestrella
```

**Linux**

```bash
mkdir -p ~/proyectos
cd ~/proyectos
git clone https://github.com/DaniCaste10/metro-cdmx-aestrella.git
cd metro-cdmx-aestrella
```

### Opción B: descargar un ZIP (sin Git)

1. En la página del repositorio en GitHub, pulsa **Code** y después **Download ZIP**.
2. Descomprime el archivo en una carpeta que cumpla las recomendaciones anteriores. Se creará una carpeta llamada `metro-cdmx-aestrella-main`.
   - **Windows**: clic derecho sobre el ZIP y **Extraer todo...**.
   - **Linux**: `sudo apt install -y unzip` y después `unzip metro-cdmx-aestrella-main.zip`.
3. Entra en esa carpeta desde la terminal.

### Contenido del repositorio

```
metro-cdmx-aestrella/
├── metro_aestrella.py       Programa completo
├── README.md                Descripción del proyecto
├── INSTALACION.md           Esta guía
└── docs/
    └── mapa-ruta.png        Imagen usada en el README
```

**Los comandos de las secciones siguientes se ejecutan desde la carpeta `metro-cdmx-aestrella`**, la que contiene `metro_aestrella.py`. Para comprobarlo, lista su contenido con `dir` (Windows) o `ls` (Linux): debes ver ese fichero.

## Instalar las librerías

El programa necesita dos librerías: **NetworkX** (el grafo y el algoritmo A\*) y **Matplotlib** (el dibujo del mapa).

### Windows

```powershell
pip install networkx matplotlib
```

Cuando termine, comprueba que se han instalado:

```powershell
python -c "import networkx, matplotlib; print('Librerías instaladas correctamente')"
```

### Linux (Ubuntu/Debian)

En Ubuntu y Debian recientes, `pip` no permite instalar librerías en el Python del sistema (da el error `externally-managed-environment`). La forma más sencilla es instalarlas con `apt`, junto con Tkinter:

```bash
sudo apt update
sudo apt install -y python3-tk python3-networkx python3-matplotlib
```

Comprueba que se han instalado:

```bash
python3 -c "import tkinter, networkx, matplotlib; print('Todo instalado correctamente')"
```

## Ejecutar la aplicación

Desde la carpeta del proyecto:

**Windows (PowerShell)**

```powershell
python metro_aestrella.py
```

**Linux**

```bash
python3 metro_aestrella.py
```

### Qué ocurre al ejecutarla

- Se abre una ventana titulada **Metro CDMX - Basado en algoritmo de búsqueda A\***, con dos desplegables (**Origen** y **Destino**), el botón verde **Calcular Ruta**, tres etiquetas vacías de resultados y el mapa de la red.
- **No aparece nada en la terminal**, y se queda ocupada mientras la ventana está abierta. Es lo normal.
- Para cerrar la aplicación, cierra la ventana con la **X**.

### Ejecutar desde un editor (opcional)

Si prefieres ejecutarlo desde un editor, por ejemplo **Visual Studio Code**:

1. Instala la extensión **Python** de Microsoft desde la pestaña de extensiones (`Ctrl + Shift + X`).
2. Abre la carpeta del proyecto con **File → Open Folder**, y después el fichero `metro_aestrella.py`.
3. Pulsa el botón **Run Python File** (el triángulo de la esquina superior derecha). La aplicación se abrirá en una ventana.

Si VS Code muestra un error de que falta alguna librería, comprueba que el intérprete seleccionado (abajo a la derecha, o con `Ctrl + Shift + P` y **Python: Select Interpreter**) es el mismo Python en el que instalaste las librerías.

## Probar la aplicación

Con la aplicación abierta, calcula una ruta:

1. En **Origen**, despliega la lista y elige una estación (también puedes escribir su nombre).
2. En **Destino**, haz lo mismo con otra estación.
3. Pulsa **Calcular Ruta**.
4. Los resultados aparecen en tres líneas y el mapa muestra la ruta en rojo:
   - **Ruta**: las estaciones del recorrido, separadas por `->`.
   - **Distancia y tiempo total**: la distancia en metros y el tiempo en formato `mm:ss`.
   - **Transbordos**: el número de cambios de línea y el tiempo extra que suponen.

### Casos de prueba

Estos cinco casos tienen un único resultado posible. Si ves lo mismo, la aplicación funciona correctamente.

| Origen | Destino | Recorrido | Distancia | Tiempo | Transbordos |
|---|---|---|---|---|---|
| Observatorio | Balderas | Toda la Línea 1 | 5741 metros | 18:14 | 0 (+0:00) |
| Polanco | Eje Central | Línea 7 y cambio a la Línea 12 en Mixcoac | 9394 metros | 31:54 | 1 (+5:10) |
| Universidad | Lázaro Cárdenas | Línea 3 y cambio a la Línea 9 en Centro Médico | 10119 metros | 31:05 | 1 (+1:40) |
| Barranca del Muerto | Coyoacán | Línea 7, cambio a la Línea 12 en Mixcoac y a la Línea 3 en Zapata | 4455 metros | 23:59 | 2 (+12:10) |
| Tacubaya | Tacubaya | La misma estación | 0 metros | 00:00 | 0 (+0:00) |

El texto mostrado tiene este formato:

```
Ruta: Polanco -> Auditorio -> Constituyentes -> Tacubaya -> San Pedro de los Pinos -> San Antonio -> Mixcoac -> Insurgentes Sur -> Hospital 20 de Noviembre -> Zapata -> Parque de los Venados -> Eje Central
Distancia: 9394 metros | Tiempo: 31:54 minutos
Número de transbordos: 1 (Tiempo extra: +5:10 minutos)
```

El tiempo total incluye el de los transbordos. En el segundo caso, por ejemplo, son 26:44 de viaje y 5:10 de transbordo.

### Comprobar las validaciones

| Prueba | Resultado esperado |
|---|---|
| Pulsar **Calcular Ruta** con el origen o el destino vacíos | Ventana de aviso con el mensaje `Selecciona origen y destino`. |
| Escribir en **Origen** un nombre inexistente (por ejemplo, `Atlantis`) y elegir un destino válido | Ventana de error con el mensaje `La estación de origen 'Atlantis' no existe.` |
| Elegir un origen válido y escribir en **Destino** un nombre inexistente | Ventana de error con el mensaje `La estación de destino '...' no existe.` |
| Escribir un nombre con otras mayúsculas o sin acentos (por ejemplo, `tacubaya` o `Juanacatlan`) | Error de estación inexistente: los nombres deben coincidir **exactamente**. Lo más cómodo es elegirlos de la lista. |

## Solución de problemas

| Síntoma o mensaje | Causa probable | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'networkx'` (o `'matplotlib'`) | Las librerías no están instaladas, o el editor usa otro Python. | **Windows**: ejecuta `pip install networkx matplotlib`. **Linux**: `sudo apt install -y python3-networkx python3-matplotlib`. En VS Code, comprueba que el intérprete seleccionado es el correcto. |
| `ModuleNotFoundError: No module named 'tkinter'` o `'_tkinter'` | Python se instaló sin Tkinter. | **Linux**: `sudo apt install -y python3-tk`. **Windows**: abre el instalador de Python, pulsa **Modify** y marca **tcl/tk and IDLE**. |
| `'python' no se reconoce como un comando...` o se abre la Microsoft Store (Windows) | Python no está en el PATH o el acceso directo de la Store lo intercepta. | Prueba `py --version`. Si funciona, usa `py` en lugar de `python`. Si no, reinstala Python marcando **Add python.exe to PATH**. También puedes desactivar los alias de la Store en **Configuración → Aplicaciones → Configuración avanzada de aplicaciones → Alias de ejecución de aplicaciones**. |
| `'pip' no se reconoce como un comando...` (Windows) | `pip` no está en el PATH. | Usa `python -m pip install networkx matplotlib`. |
| `error: externally-managed-environment` al usar `pip` (Linux) | Ubuntu y Debian no permiten instalar librerías con `pip` en el Python del sistema. | Instala las librerías con `apt`, como se explica en [Instalar las librerías](#instalar-las-librerías). No uses `--break-system-packages`. |
| `_tkinter.TclError: no display name and no $DISPLAY environment variable` | No hay entorno gráfico (SSH, servidor, contenedor). | Ejecuta la aplicación desde una sesión de escritorio. En Windows 11, WSL2 con WSLg también la soporta. |
| `can't open file '...metro_aestrella.py': [Errno 2] No such file or directory` | Estás en una carpeta incorrecta. | Entra en la carpeta del proyecto con `cd` y comprueba con `dir` (Windows) o `ls` (Linux) que aparece `metro_aestrella.py`. |
| `pip` o `apt` no pueden descargar las librerías | No hay conexión a Internet o la bloquea un proxy o un cortafuegos. | Comprueba la conexión. `pip` necesita acceso a `https://pypi.org`. |
