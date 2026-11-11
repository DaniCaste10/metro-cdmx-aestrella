import math
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox

#Coordenadas gráficas de cada estación
coordenadas_graficas = {
    "Observatorio": (-1.9, -2.4),
    "Tacubaya": (0.0, -1.6),
    "Juanacatlán": (2.4, -0.4),
    "Chapultepec": (4.4, 0.8),
    "Sevilla": (6.2, 1.9),
    "Insurgentes": (7.6, 2.8),
    "Cuauhtémoc": (9.2, 2.8),
    "Balderas": (11.2, 2.8),

    "Universidad": (11.2, -13.2),
    "Copilco": (11.2, -12.0),
    "Miguel Ángel de Quevedo": (11.2, -10.8),
    "Viveros": (11.2, -9.2),
    "Coyoacán": (11.2, -7.6),
    "Zapata": (11.2, -6.0),
    "División del Norte": (11.2, -4.8),
    "Eugenia": (11.2, -3.6),
    "Etiopía": (11.2, -2.4),
    "Centro Médico": (11.2, -1.2),
    "Hospital General": (11.2, 0.4),
    "Niños Héroes": (11.2, 1.6),
    "Juárez": (11.2, 4.8),

    "Barranca del Muerto": (0.0, -8.0),
    "Mixcoac": (0.0, -6.0),
    "San Antonio": (0.0, -4.8),
    "San Pedro de los Pinos": (0.0, -3.2),
    "Constituyentes": (0.0, 0.0),
    "Auditorio": (0.0, 2.4),
    "Polanco": (0.0, 4.8),

    "Patriotismo": (4.0, -1.2),
    "Chilpancingo": (8.4, -1.2),
    "Lázaro Cárdenas": (14.8, -1.2),

    "Insurgentes Sur": (3.2, -6.0),
    "Hospital 20 de Noviembre": (7.6, -6.0),
    "Parque de los Venados": (14.4, -6.0),
    "Eje Central": (18.0, -10.0)
}

tiempos_entre_estaciones = {
    ("Observatorio", "Tacubaya"): 160,      
    ("Tacubaya", "Juanacatlán"): 174,        
    ("Juanacatlán", "Chapultepec"): 170,    
    ("Chapultepec", "Sevilla"): 140,         
    ("Sevilla", "Insurgentes"): 150,         
    ("Insurgentes", "Cuauhtémoc"): 160,      
    ("Cuauhtémoc", "Balderas"): 140,         

    ("Universidad", "Copilco"): 185,         
    ("Copilco", "Miguel Ángel de Quevedo"): 200,  
    ("Miguel Ángel de Quevedo", "Viveros"): 170,  
    ("Viveros", "Coyoacán"): 165,            
    ("Coyoacán", "Zapata"): 180,             
    ("Zapata", "División del Norte"): 165,   
    ("División del Norte", "Eugenia"): 155,  
    ("Eugenia", "Etiopía"): 165,             
    ("Etiopía", "Centro Médico"): 195,       
    ("Centro Médico", "Hospital General"): 170,  
    ("Hospital General", "Niños Héroes"): 155,   
    ("Niños Héroes", "Balderas"): 150,       
    ("Balderas", "Juárez"): 165,             

    ("Barranca del Muerto", "Mixcoac"): 130, 
    ("Mixcoac", "San Antonio"): 140,         
    ("San Antonio", "San Pedro de los Pinos"): 145,  
    ("San Pedro de los Pinos", "Tacubaya"): 175,     
    ("Tacubaya", "Constituyentes"): 165,     
    ("Constituyentes", "Auditorio"): 190,    
    ("Auditorio", "Polanco"): 155,           

    ("Tacubaya", "Patriotismo"): 165,        
    ("Patriotismo", "Chilpancingo"): 165,    
    ("Chilpancingo", "Centro Médico"): 185,  
    ("Centro Médico", "Lázaro Cárdenas"): 185, 
 
    ("Mixcoac", "Insurgentes Sur"): 160,     
    ("Insurgentes Sur", "Hospital 20 de Noviembre"): 130, 
    ("Hospital 20 de Noviembre", "Zapata"): 109, 
    ("Zapata", "Parque de los Venados"): 100, 
    ("Parque de los Venados", "Eje Central"): 135 
}

tiempos_transbordo = {
    "Tacubaya": {
        ("Línea 1", "Línea 7"): 176,
        ("Línea 1", "Línea 9"): 382,
        ("Línea 7", "Línea 1"): 176,
        ("Línea 7", "Línea 9"): 272,
        ("Línea 9", "Línea 1"): 382, 
        ("Línea 9", "Línea 7"): 272
    },
    "Mixcoac": {
        ("Línea 7", "Línea 12"): 310,
        ("Línea 12", "Línea 7"): 310
    },
    "Centro Médico": {
        ("Línea 3", "Línea 9"): 100,
        ("Línea 9", "Línea 3"): 100
    },
    "Balderas":{
        ("Línea 1", "Línea 3"): 152,
        ("Línea 3", "Línea 1"): 152
    },
    "Zapata":{
        ("Línea 3", "Línea 12"): 310,
        ("Línea 12", "Línea 3"): 420
    }  
}


#Definición del grafo
def crear_grafo_metro():
    grafo = nx.Graph()
    colores = {}

    def anadir_linea(nombre, color, estaciones, pesos):
        for i in range(len(estaciones) - 1):
            e1, e2 = estaciones[i], estaciones[i + 1]
            peso = pesos[i]
            tiempo = tiempos_entre_estaciones.get((e1, e2)) or tiempos_entre_estaciones.get((e2, e1))
            grafo.add_edge(e1, e2, weight=peso, tiempo=tiempo, linea=nombre)
        colores[nombre] = color

    anadir_linea("Línea 1", "#A2006D",
                 ["Observatorio", "Tacubaya", "Juanacatlán", "Chapultepec",
                  "Sevilla", "Insurgentes", "Cuauhtémoc", "Balderas"],
                 [1262, 1158, 973, 501, 645, 793, 409])

    anadir_linea("Línea 3", "#B5BD00",
                 ["Universidad", "Copilco", "Miguel Ángel de Quevedo", "Viveros",
                  "Coyoacán", "Zapata", "División del Norte", "Eugenia", "Etiopía",
                  "Centro Médico", "Hospital General", "Niños Héroes", "Balderas", "Juárez"],
                 [1306, 1295, 824, 904, 1153, 794, 715, 950, 1119,
                  653, 559, 665, 659])

    anadir_linea("Línea 7", "#E77C00",
                 ["Barranca del Muerto", "Mixcoac", "San Antonio",
                  "San Pedro de los Pinos", "Tacubaya", "Constituyentes",
                  "Auditorio", "Polanco"],
                 [1476, 788, 606, 1084, 1005, 1430, 812])

    anadir_linea("Línea 9", "#A05A2C",
                 ["Tacubaya", "Patriotismo", "Chilpancingo",
                  "Centro Médico", "Lázaro Cárdenas"],
                 [1133, 955, 1152, 1059])

    anadir_linea("Línea 12", "#918521",
                 ["Mixcoac", "Insurgentes Sur", "Hospital 20 de Noviembre",
                  "Zapata", "Parque de los Venados", "Eje Central"],
                 [651, 725, 450, 563, 1280])

    return grafo, colores

#Heurística
def heuristica(a, b):
    if a not in coordenadas_graficas or b not in coordenadas_graficas:
        return 0
    x1, y1 = coordenadas_graficas[a]
    x2, y2 = coordenadas_graficas[b]
    return math.hypot(x1 - x2, y1 - y2)

#Función encargada de la parte gráfica
def dibujar_metro(ax, grafo, colores_lineas, ruta=None):
    ax.clear() #Limpiamos
    ax.set_axis_off() #Para que quede una mejor estética
    ax.set_facecolor("#ffffff") #Fondo blanco
    ax.set_title("Metro CDMX - Basado en algoritmo de búsqueda A*", fontsize=14, pad=10) #Título
    # Dibujar líneas
    for linea, color in colores_lineas.items():
        aristas = [(u, v) for u, v, datos in grafo.edges(data=True) if datos["linea"] == linea]
        nx.draw_networkx_edges(grafo, coordenadas_graficas, edgelist=aristas, width=6, edge_color=color, ax=ax)
    # Transbordos
    transbordos = [n for n in grafo.nodes if len({d["linea"] for _, _, d in grafo.edges(n, data=True)}) > 1]
    normales = [n for n in grafo.nodes if n not in transbordos]
    #Dibujamos
    nx.draw_networkx_nodes(grafo, coordenadas_graficas, nodelist=normales, node_size=85, node_color="white",edgecolors="black", ax=ax)
    nx.draw_networkx_nodes(grafo, coordenadas_graficas, nodelist=transbordos, node_size=175, node_color="white",edgecolors="black", linewidths=3, ax=ax)
    # Etiquetas
    for estacion, (x, y) in coordenadas_graficas.items():
        if estacion in transbordos:
            color = "black"
        else:
            linea = next(iter({d["linea"] for _, _, d in grafo.edges(estacion, data=True)}))
            color = colores_lineas[linea]
        ax.text(x+0.15, y+0.42, estacion, fontsize=8, fontweight="bold", color=color, ha="center", va="center", bbox=dict(facecolor="white", alpha=0.6, edgecolor="none"))

    # Ruta óptima
    if ruta:
        edges = list(zip(ruta[:-1], ruta[1:])) #Genera pares consecutivos. Ej si tuta = [a, b, c] -> edges: (a,b), (b,c)
        nx.draw_networkx_edges(grafo, coordenadas_graficas, edgelist=edges,width=5, edge_color="red", ax=ax)
        nx.draw_networkx_nodes(grafo, coordenadas_graficas, nodelist=ruta, node_size=85, node_color="#f8a1a1",edgecolors="black", ax=ax)
    # Leyenda
    items = []
    etiquetasl = []
    for linea, color in colores_lineas.items():
        h, = ax.plot([], [], color=color, linewidth=6)
        items.append(h)
        etiquetasl.append(linea)

    r, = ax.plot([], [], color="red", linewidth=6)
    items.append(r)
    etiquetasl.append("Ruta óptima")
    ax.legend(items, etiquetasl,loc="lower left", fontsize=8,frameon=True, facecolor="white") #Mostrar leyenda

#Para calcular el tiempo extra si hacemos transbordo  
def calcular_tiempo_transbordos(grafo, ruta, tiempos_transbordo):
    tiempo_extra = 0
    transbordos = 0
    linea_anterior = None
    for a, b in zip(ruta[:-1], ruta[1:]):
        linea_actual = grafo[a][b]["linea"]
        if linea_anterior is not None and linea_actual != linea_anterior:
            transbordos += 1
            if a in tiempos_transbordo:
                clave = (linea_anterior, linea_actual)
                if clave in tiempos_transbordo[a]:
                    tiempo_extra += tiempos_transbordo[a][clave]
        linea_anterior = linea_actual
    return transbordos, tiempo_extra

#Parte interactiva con el usuario
class MetroApp:
    def __init__(self, root):
        #Parámetros de la ventana
        self.root = root
        root.title("Metro CDMX - Basado en algoritmo de búsqueda A*") 
        root.geometry("1150x750")
        root.configure(bg="#FFFFFF")
        root.protocol("WM_DELETE_WINDOW", self.cerrar)
        #Creamos grafo
        self.grafo, self.colores = crear_grafo_metro()
        self.estaciones = sorted(self.grafo.nodes())
        #Etiqueta título
        tk.Label(root, text="Metro CDMX - Algoritmo A*", font=("Arial", 20, "bold"), bg="#FFFFFF").pack(pady=10)
        marco_entradas = tk.Frame(root, bg="#FFFFFF")
        marco_entradas.pack(pady=6)
        #Etiqueta campo origen
        tk.Label(marco_entradas, text="Origen:", bg="#FFFFFF").grid(row=0, column=0)
        self.caja_origen = ttk.Combobox(marco_entradas, values=self.estaciones, width=30)
        self.caja_origen.grid(row=0, column=1)
        #Etiqueta campo destino
        tk.Label(marco_entradas, text="Destino:", bg="#FFFFFF").grid(row=0, column=2)
        self.caja_destino = ttk.Combobox(marco_entradas, values=self.estaciones, width=30)
        self.caja_destino.grid(row=0, column=3)
        #Botón calcular ruta
        tk.Button(marco_entradas, text="Calcular Ruta", bg="#007A53", fg="white", command=self.calcular_ruta).grid(row=0, column=4, padx=10)
        marco_res = tk.Frame(root, bg="#FFFFFF")
        marco_res.pack(pady=6)
        #Etiqueta para donde sale la ruta
        tk.Label(marco_res, text="Ruta:", font=("Arial", 12, "bold"), bg="#FFFFFF").grid(row=0, column=0)
        self.etiqruta = tk.Label(marco_res, text="", bg="#FFFFFF", wraplength=800)
        self.etiqruta.grid(row=0, column=1)
        #Etiqueta para donde sale la distancia y tiempo total
        tk.Label(marco_res, text="Distancia y tiempo total:", font=("Arial", 12, "bold"), bg="#FFFFFF").grid(row=1, column=0)
        self.etiqcoste = tk.Label(marco_res, text="", bg="#FFFFFF")
        self.etiqcoste.grid(row=1, column=1)
        #Etiqueta para donde salen los transbordos
        tk.Label(marco_res, text="Transbordos:", font=("Arial", 12, "bold"), bg="#FFFFFF").grid(row=2, column=0)
        self.etiqtrans = tk.Label(marco_res, text="", bg="#FFFFFF")
        self.etiqtrans.grid(row=2, column=1)
        #Creación del marco
        self.marcograf = tk.Frame(root, bg="white", relief="sunken", borderwidth=2)
        self.marcograf.pack(fill="both", expand=True, padx=10, pady=10)

        #Se crea el gráfico de matplotlib dentro de tkinter
        self.fig, self.ax = plt.subplots(figsize=(9, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.marcograf)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        dibujar_metro(self.ax, self.grafo, self.colores)
        self.canvas.draw()

    def peso_tiempo(self, u, v, datos):    
        tiempo_base = datos.get("tiempo", 0)
        linea_actual = datos.get("linea")
        # Si aún no tenemos línea previa
        if not hasattr(self, "_linea_prev") or self._linea_prev is None: 
            self._linea_prev = linea_actual
            return tiempo_base
        # Detectar cambio de línea
        if linea_actual != self._linea_prev:
            estacion = u

            clave = (self._linea_prev, linea_actual)
            if estacion in tiempos_transbordo and clave in tiempos_transbordo[estacion]:
                tiempo_trans = tiempos_transbordo[estacion][clave]
            else:
                tiempo_trans = 120
            tiempo_total = tiempo_base + tiempo_trans
        else:
            tiempo_total = tiempo_base
        # actualizar línea previa
        self._linea_prev = linea_actual
        return tiempo_total             
    
    #Para detener la ejecución
    def cerrar(self):
        plt.close('all')
        self.root.destroy()
    #Calculamos ruta
    def calcular_ruta(self):
        origen = self.caja_origen.get()
        destino = self.caja_destino.get()
        #Funcionalidad extra para que salte error si no hay origen y/o destino seleccionado
        if origen == "" or destino == "":
            messagebox.showwarning("Error", "Selecciona origen y destino")
            return
        #Funcionalidad extra para que salte error si la parada origen descrita no existe 
        if origen not in self.estaciones:
            messagebox.showerror("Error", f"La estación de origen '{origen}' no existe.")
            return
        #Funcionalidad extra para que salte error si la parada destino descrita no existe 
        if destino not in self.estaciones:
            messagebox.showerror("Error", f"La estación de destino '{destino}' no existe.")
            return
        self._linea_prev = None
        ruta = nx.astar_path(self.grafo, origen, destino, heuristic=heuristica, weight=self.peso_tiempo) 

        ttotal = 0
        for a, b in zip(ruta[:-1], ruta[1:]):
            ttotal += self.grafo[a][b]["tiempo"]

        num_transbordos, tiempo_extra_transb = calcular_tiempo_transbordos(self.grafo, ruta, tiempos_transbordo)
        ttotal += tiempo_extra_transb
        minutos = ttotal // 60
        segundos = ttotal % 60
        tiempo_str = f"{minutos:02d}:{segundos:02d}"
        coste = nx.path_weight(self.grafo, ruta, weight="weight")
        #Impresión de resultados
        self.etiqruta.config(text=" -> ".join(ruta))
        self.etiqcoste.config(text=f"Distancia: {coste} metros | Tiempo: {tiempo_str} minutos")
        self.etiqtrans.config(text= f"Número de transbordos: {num_transbordos} " f"(Tiempo extra: +{tiempo_extra_transb//60}:{tiempo_extra_transb%60:02d} minutos)")
        dibujar_metro(self.ax, self.grafo, self.colores, ruta)
        self.canvas.draw()

def main():
    root = tk.Tk()
    MetroApp(root) #Al definir inicio con los guiones bajos, cuando se ejecute esta instrucción se ejecutará inicio
    root.mainloop()

main()
