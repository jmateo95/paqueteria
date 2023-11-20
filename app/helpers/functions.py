import heapq
import math
from collections import defaultdict

def ruta_mas_corta(salidas, sucursal_origen_id, sucursal_destino_id, campo):
    # Crear un diccionario que represente el grafo
    grafo = defaultdict(list)
    for salida in salidas:
        grafo[salida['sucursal_origen_id']].append((salida['sucursal_destino_id'], salida['id'], salida[campo]))

    # Inicializar la cola de prioridad con el nodo de inicio y distancia 0
    cola_prioridad = [(0, sucursal_origen_id, [])]
    # Inicializar un diccionario para almacenar las distancias más cortas
    distancias = {sucursal_id: float('inf') for sucursal_id in grafo}
    distancias[sucursal_origen_id] = 0

    while cola_prioridad:
        # Obtener el nodo con la distancia más corta en la cola
        distancia_actual, nodo_actual, camino_actual = heapq.heappop(cola_prioridad)

        # Si hemos llegado al destino, terminamos
        if nodo_actual == sucursal_destino_id:
            return camino_actual

        # Si la distancia actual es mayor que la conocida, continuamos
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Explorar los nodos vecinos
        for vecino, salida_id, distancia in grafo[nodo_actual]:
            nueva_distancia = distancia_actual + distancia

            if vecino not in distancias:
                continue
            
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                nuevo_camino = camino_actual + [salida_id]
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino, nuevo_camino))

    # Si no se encontró un camino, retornar una lista vacía
    return []

def filtrar_salidas(salidas_ids, salidas):
    salidas_dict = {salida['id']: salida for salida in salidas}
    return [salidas_dict[salida_id] for salida_id in salidas_ids]


def get_salidas(salidas, sucursal_origen_id, sucursal_destino_id, campo):
    salidas_ids = ruta_mas_corta(salidas, sucursal_origen_id, sucursal_destino_id, campo)
    return filtrar_salidas(salidas_ids, salidas)

def get_criterio(salidas, tarifario, peso, criterio, descripcion=""):
    resultado=None
    if salidas:
        costo_total = 0
        distancia_total = 0
        for ruta in salidas:
            costo_total += peso * (ruta['costo_lb'] + tarifario.costo_lb)
            distancia_total += ruta['distancia']
        costo_total = round(math.ceil((costo_total * (1 + (tarifario.ganancia_envio / 100))) * 100) / 100, 2)
        distancia_total = round(distancia_total,2)
        resultado = {
            "criterio": criterio,
            "descripcion": descripcion,
            "costo_total": costo_total,
            "distancia_total": distancia_total
        }
    return resultado

def get_cotizar(por_distancia, por_costo, tarifario, peso):
    resultados = []
    costo_por_distancia = get_criterio(por_distancia, tarifario, peso, 'distancia', 'distancia menor')
    costo_por_costo = get_criterio(por_costo, tarifario, peso, 'costo_lb', 'costo menor')
    resultados.append(costo_por_distancia)
    resultados.append(costo_por_costo)
    return resultados
    

def get_costo(salidas, tarifario, peso, criterio):
    costo=get_criterio(salidas, tarifario, peso, criterio)
    return costo['costo_total']

