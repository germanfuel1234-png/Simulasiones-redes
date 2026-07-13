import copy  # Importamos para poder hacer una copia "fiel" de los datos en cada salto

def bellman_ford_estricto(aristas, total_nodos, inicio):
    # --- 1. PREPARACIÓN ---
    # Creamos el diccionario de distancias inicial: todo es infinito ('-')
    distancias = {nodo: float('inf') for nodo in total_nodos}
    # La distancia a nosotros mismos (Router A) siempre es 0
    distancias[inicio] = 0

    print(f"Estado inicial (Salto 0):")
    mostrar_estado(distancias)
    print("-" * 20)

    # --- 2. EL BUCLE DE SALTOS (RELAJACIÓN) ---
    # Corremos el bucle tantas veces como nodos hay menos uno
    for i in range(1, len(total_nodos)):
        
        # IMPORTANTE: Creamos una copia de las distancias del salto anterior.
        # Esto evita que una actualización en este salto afecte a los demás nodos 
        # en la misma vuelta (fuerza a que la información viaje "un router a la vez").
        distancias_anteriores = copy.deepcopy(distancias)
        cambio = False # Usamos esta variable para saber si hubo alguna mejora
        
        # Revisamos cada conexión (arista) del mapa
        for origen, destino, peso in aristas:
            
            # Solo intentamos calcular si ya conocemos cómo llegar al nodo de 'origen'
            if distancias_anteriores[origen] != float('inf'):
                
                # Calculamos: ¿Es el costo acumulado + el peso actual menor a lo que ya sabíamos?
                if distancias_anteriores[origen] + peso < distancias[destino]:
                    # Si es más barato, actualizamos el valor en nuestro registro principal
                    distancias[destino] = distancias_anteriores[origen] + peso
                    cambio = True # Marcamos que encontramos una mejora
        
        # Mostramos cómo quedaron los routers tras este número de saltos
        print(f"Tras Salto {i}:")
        mostrar_estado(distancias)
        
        # Si en toda una vuelta no hubo ni un solo cambio, terminamos antes (optimización)
        if not cambio:
            print(f"\n¡El algoritmo Terminó! No hay más rutas que mejorar.")
            break
    
    return distancias

def mostrar_estado(distancias):
    """ Función para imprimir bonito: cambia el 'inf' por un guion '-' """
    linea = ""
    for nodo, dist in distancias.items():
        # Si el valor es infinito, mostramos '-', si no, el número
        valor = dist if dist != float('inf') else "-"
        linea += f"{nodo}: {valor} | "
    print(linea)

# --- DATOS DE TU MAPA DE ROUTERS ---
conexiones = [
    ('A', 'B', 1), ('A', 'C', 2), ('A', 'D', 8),   
    ('B', 'E', 3),   
    ('C', 'D', 5), ('C', 'E', 3), ('C', 'F', 8),
    ('D', 'F', 12),                                
    ('E', 'F', 4)    
]

nodos = ['A', 'B', 'C', 'D', 'E', 'F']

# Ejecutamos la función
bellman_ford_estricto(conexiones, nodos, 'A')