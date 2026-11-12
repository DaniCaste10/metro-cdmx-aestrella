# Instalación y ejecución

Guía paso a paso para instalar y ejecutar el **planificador de rutas del Metro CDMX con A\*** desde cero, tanto en **Windows** como en **Linux**. No hace falta experiencia previa con Python: basta con seguir los pasos en orden.

> Los pasos de Linux están redactados para **Ubuntu y Debian**. En otras distribuciones los paquetes son equivalentes, pero los comandos de instalación pueden variar. En macOS el procedimiento es similar (se recomienda el Python oficial de python.org, que incluye Tkinter), pero no se describe aquí.

Para conocer cómo funciona el programa (el grafo, el algoritmo A\* y la arquitectura), consulta el [README](README.md).

## Índice

- [Resumen rápido](#resumen-rápido)
- [Requisitos](#requisitos)
- [Instalar el software](#instalar-el-software)
- [Descargar el proyecto](#descargar-el-proyecto)
- [Crear el entorno virtual e instalar las librerías](#crear-el-entorno-virtual-e-instalar-las-librerías)
- [Ejecutar la aplicación](#ejecutar-la-aplicación)
- [Probar la aplicación](#probar-la-aplicación)
- [Cerrar, reactivar y limpiar](#cerrar-reactivar-y-limpiar)
- [Solución de problemas](#solución-de-problemas)

## Resumen rápido

Si ya tienes instalados **Python 3.10 o superior (con Tkinter)** y **Git**, estos son todos los pasos.

**Windows (PowerShell)**

```powershell
git clone https://github.com/DaniCaste10/metro-cdmx-aestrella.git
cd metro-cdmx-aestrella
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python metro_aestrella.py
```

**Linux (Ubuntu/Debian)**

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip python3-tk git
git clone https://github.com/DaniCaste10/metro-cdmx-aestrella.git
cd metro-cdmx-aestrella
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python metro_aestrella.py
```

Se abrirá una ventana con el mapa del metro. Si es la primera vez que haces esto, sigue la guía completa a continuación.

## Requisitos

| Software | Versión | Para qué se usa | Dónde descargarlo |
|---|---|---|---|
| **Python** | 3.10 o superior (se recomienda la 3.12 o más reciente) | Ejecutar el programa | https://www.python.org/downloads/ |
| **Tkinter** | Incluido con Python en Windows. En Linux es un paquete aparte (`python3-tk`). | Interfaz gráfica | Viene con Python |
| **NetworkX** | Última versión | Grafo y algoritmo A* | Se instala con `pip` |
| **Matplotlib** | Última versión | Dibujo del mapa | Se instala con `pip` |
| **Git** | Cualquiera reciente | Descargar el proyecto (opcional: también se puede bajar como ZIP) | https://git-scm.com/downloads |

Además:

- **Se necesita un entorno gráfico** (el escritorio de Windows o de Linux), porque la aplicación abre una ventana. No funciona por SSH ni en un terminal sin pantalla.
- **Se necesita conexión a Internet** para descargar el proyecto y las librerías.
- Las librerías **NetworkX** y **Matplotlib** no hace falta instalarlas a mano: el fichero `requirements.txt` del proyecto las indica y `pip` las instala de una sola vez.

## Instalar el software

### Python

**Windows**

1. Entra en https://www.python.org/downloads/windows/ y descarga el instalador de Windows (64-bit) de la versión estable más reciente de Python 3.
2. Ejecuta el instalador. En la **primera pantalla**, marca la casilla **Add python.exe to PATH** (está en la parte inferior) y pulsa **Install Now**. Con esa opción se instala también Tkinter (aparece como *tcl/tk and IDLE*) y `pip`.
3. Al terminar, cierra el instalador y abre una terminal **nueva** (PowerShell). Comprueba la instalación:

```powershell
python --version
python -m pip --version
python -m tkinter
```

Los dos primeros comandos deben mostrar una versión (Python 3.10 o superior). El tercero abre una ventana pequeña de prueba de Tk, que confirma que Tkinter funciona: ciérrala.

Si PowerShell responde que `python` no se reconoce, prueba con `py --version`. Si funciona, usa `py` en lugar de `python` en el resto de la guía. En [Solución de problemas](#solución-de-problemas) tienes más opciones.

**Linux (Ubuntu/Debian)**

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip python3-tk
```

Cada paquete cumple una función:

- `python3`: el intérprete de Python.
- `python3-venv`: permite crear entornos virtuales, que se usan más adelante.
- `python3-pip`: el instalador de librerías.
- `python3-tk`: Tkinter. **En Linux no viene incluido con Python** y es imprescindible para la interfaz.

Comprueba la instalación:

```bash
python3 --version
python3 -m tkinter
```

La primera orden debe mostrar una versión 3.10 o superior (Ubuntu 22.04 incluye la 3.10 y Ubuntu 24.04 la 3.12, y ambas sirven). La segunda abre una ventana pequeña de prueba de Tk, que confirma que Tkinter funciona: ciérrala.

### Git

**Windows**

1. Descarga el instalador desde https://git-scm.com/download/win.
2. Ejecútalo y acepta las opciones que propone por defecto.
3. Abre una terminal **nueva** y comprueba la instalación:

```powershell
git --version
```

**Linux (Ubuntu/Debian)**

```bash
sudo apt install -y git
git --version
```

## Descargar el proyecto

El código está en un repositorio de GitHub. Hay dos formas de obtenerlo.

### Opción A: clonar el repositorio con Git (recomendada)

1. Abre la página del repositorio en GitHub, pulsa el botón verde **Code**, selecciona la pestaña **HTTPS** y copia la URL. Tiene la forma `https://github.com/DaniCaste10/metro-cdmx-aestrella.git`.
2. Elige una carpeta donde guardar el proyecto. Es preferible que la ruta **no contenga espacios ni acentos** y que **no esté dentro de una carpeta sincronizada con OneDrive** (como `Escritorio` o `Documentos`), porque la sincronización puede bloquear ficheros.
3. Clona el repositorio.

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
├── requirements.txt         Librerías necesarias
├── README.md                Descripción del proyecto
├── INSTALACION.md           Esta guía
└── docs/
    └── mapa-ruta.png        Imagen usada en el README
```

**Todos los comandos de las secciones siguientes se ejecutan desde la carpeta `metro-cdmx-aestrella`**, la que contiene `metro_aestrella.py`. Para comprobarlo, lista su contenido con `dir` (Windows) o `ls` (Linux): debes ver ese fichero.

## Crear el entorno virtual e instalar las librerías

Un **entorno virtual** es una carpeta (`.venv`) con una copia aislada de Python en la que se instalan las librerías del proyecto, sin mezclarlas con las del sistema. Es la forma recomendada de trabajar con Python y, en Ubuntu y Debian recientes, es **obligatorio**: instalar librerías directamente en el sistema con `pip` falla con el error `externally-managed-environment`.

### Windows (PowerShell)

Desde la carpeta del proyecto, crea el entorno y actívalo:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Cuando está activo, el prompt de la terminal empieza por `(.venv)`. Si PowerShell muestra un error al activarlo (*la ejecución de scripts está deshabilitada en este sistema*), consulta [Solución de problemas](#solución-de-problemas).

Después, instala las librerías:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Comprueba que se han instalado:

```powershell
python -c "import networkx, matplotlib; print('Librerías instaladas correctamente')"
```

Si prefieres el símbolo del sistema clásico (`cmd`), el comando de activación es `.venv\Scripts\activate.bat`.

### Linux (Ubuntu/Debian)

Desde la carpeta del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Cuando está activo, el prompt empieza por `(.venv)`. Dentro del entorno basta con escribir `python` (en lugar de `python3`). Instala las librerías:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Comprueba que se han instalado:

```bash
python -c "import networkx, matplotlib; print('Librerías instaladas correctamente')"
```

## Ejecutar la aplicación

Con el entorno virtual **activado** (el prompt empieza por `(.venv)`) y desde la carpeta del proyecto:

**Windows (PowerShell)**

```powershell
python metro_aestrella.py
```

**Linux**

```bash
python metro_aestrella.py
```

### Qué ocurre al ejecutarla

- Se abre una ventana titulada **Metro CDMX - Basado en algoritmo de búsqueda A\***, con dos desplegables (**Origen** y **Destino**), el botón verde **Calcular Ruta**, tres etiquetas vacías de resultados y el mapa de la red.
- **No aparece nada en la terminal**, y se queda ocupada mientras la ventana está abierta. Es lo normal.
- Para cerrar la aplicación, cierra la ventana con la **X**. La terminal quedará libre de nuevo.

### Ejecutar desde Visual Studio Code (opcional)

Si prefieres un editor, Visual Studio Code facilita la ejecución:

1. Instala Visual Studio Code desde https://code.visualstudio.com/ y, en la pestaña de extensiones (`Ctrl + Shift + X`), la extensión **Python** de Microsoft.
2. Abre la carpeta del proyecto con **File → Open Folder** y selecciona `metro-cdmx-aestrella`.
3. Crea el entorno virtual e instala las librerías como se explica en la sección anterior (puedes usar el terminal integrado, con `Ctrl + ñ` en teclado español o el menú **Terminal → New Terminal**).
4. Pulsa `Ctrl + Shift + P`, escribe **Python: Select Interpreter** y elige el que está dentro de `.venv`.
5. Abre `metro_aestrella.py` y pulsa el botón **Run Python File** (el triángulo de la esquina superior derecha).

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

### Observación sobre las rutas

En algunas parejas de estaciones, la ruta calculada puede no ser la de menor tiempo posible. Es una limitación conocida del programa, descrita en la sección [Limitaciones y posibles mejoras](README.md#limitaciones-y-posibles-mejoras) del README. Los casos de prueba de arriba no se ven afectados.

## Cerrar, reactivar y limpiar

**Salir del entorno virtual.** Cuando termines, escribe en la terminal (en Windows y en Linux):

```
deactivate
```

**Volver a usar la aplicación otro día.** Las librerías siguen instaladas en `.venv`, así que solo hay que volver a activar el entorno y ejecutar el programa, desde la carpeta del proyecto:

| Sistema | Activar el entorno | Ejecutar |
|---|---|---|
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` | `python metro_aestrella.py` |
| Linux | `source .venv/bin/activate` | `python metro_aestrella.py` |

Cada vez que abras una terminal nueva, hay que activar el entorno de nuevo.

**Actualizar el proyecto** si hay cambios nuevos en GitHub (desde la carpeta del repositorio):

```
git pull
```

**Eliminar el entorno virtual** (se puede volver a crear cuando quieras). Desactívalo primero con `deactivate` y borra la carpeta:

| Sistema | Comando |
|---|---|
| Windows (PowerShell) | `Remove-Item -Recurse -Force .venv` |
| Linux | `rm -rf .venv` |

## Solución de problemas

| Síntoma o mensaje | Causa probable | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'networkx'` (o `'matplotlib'`) | El entorno virtual no está activado o las librerías no están instaladas. | Activa el entorno (el prompt debe empezar por `(.venv)`) y ejecuta `python -m pip install -r requirements.txt`. |
| `ModuleNotFoundError: No module named 'tkinter'` o `'_tkinter'` | Python se instaló sin Tkinter. | **Linux**: `sudo apt install -y python3-tk`. **Windows**: abre el instalador de Python, pulsa **Modify** y marca **tcl/tk and IDLE**. |
| `error: externally-managed-environment` al usar `pip` (Linux) | Ubuntu y Debian no permiten instalar librerías en el Python del sistema. | Usa un entorno virtual, como se explica en [Crear el entorno virtual](#crear-el-entorno-virtual-e-instalar-las-librerías). No uses `--break-system-packages`. |
| `The virtual environment was not created successfully because ensurepip is not available` | Falta el paquete de entornos virtuales. | `sudo apt install -y python3-venv` y repite `python3 -m venv .venv`. |
| `'python' no se reconoce como un comando...` o se abre la Microsoft Store (Windows) | Python no está en el PATH o el acceso directo de la Store lo intercepta. | Prueba `py --version`. Si no funciona, reinstala Python marcando **Add python.exe to PATH**. También puedes desactivar los alias de la Store en **Configuración → Aplicaciones → Configuración avanzada de aplicaciones → Alias de ejecución de aplicaciones**. |
| `La ejecución de scripts está deshabilitada en este sistema` al activar el entorno (PowerShell) | La política de PowerShell bloquea el script de activación. | Ejecuta `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`, confirma con `S` y vuelve a activar el entorno. Otra opción es no activarlo y ejecutar directamente `.venv\Scripts\python.exe metro_aestrella.py`. |
| `_tkinter.TclError: no display name and no $DISPLAY environment variable` | No hay entorno gráfico (SSH, servidor, contenedor). | Ejecuta la aplicación desde una sesión de escritorio. En Windows 11, WSL2 con WSLg también la soporta. |
| `can't open file '...metro_aestrella.py': [Errno 2] No such file or directory` | Estás en una carpeta incorrecta. | Entra en la carpeta del proyecto con `cd` y comprueba con `dir` (Windows) o `ls` (Linux) que aparece `metro_aestrella.py`. |
| `pip` no puede descargar las librerías (`Could not find a version`, `Connection timed out`) | No hay conexión a Internet o la bloquea un proxy o un cortafuegos. | Comprueba la conexión. Se necesita acceso a `https://pypi.org`. |
| Al abrir una terminal nueva vuelve el error `ModuleNotFoundError` | El entorno virtual no está activado en esa terminal. | Actívalo de nuevo (véase [Cerrar, reactivar y limpiar](#cerrar-reactivar-y-limpiar)). |
| La ventana no se abre y la terminal queda libre sin mensajes | El script no se ejecutó realmente o se cerró al instante. | Ejecútalo de nuevo desde la terminal con `python metro_aestrella.py` y lee los mensajes de error, si los hay. |
