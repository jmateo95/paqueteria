from app.models.sucursal.segmento_model import SegmentoCreate, SegmentoUpdate
from config.Connection import prisma_connection
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64

class SegmentoRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self, test:bool=False):
        where_conditions = {}
        if not test:
            where_conditions["test"] = test
        return await self.connection.prisma.segmento.find_many(include={"sucursal_destino":True,"sucursal_origen":True}, where=where_conditions, order=[{"id": "desc"}])

    async def get_by_id(self, segmento_id: int):
        return await self.connection.prisma.segmento.find_first(where={"id": segmento_id},include={"sucursal_destino":True,"sucursal_origen":True})
    
    async def get_by_sucursal_origen(self, sucursal_origen_id: int, test:bool=False):
        where_params = {"sucursal_origen_id": sucursal_origen_id}
        if not test:
            where_params["test"] = False
        return await self.connection.prisma.segmento.find_many(where=where_params)
    
    async def get_by_sucursales(self, sucursal_origen_id: int, sucursal_destino_id: int, test:bool=False):
        where_params = {"sucursal_origen_id": sucursal_origen_id, "sucursal_destino_id": sucursal_destino_id}
        if not test:
            where_params["test"] = False
        return await self.connection.prisma.segmento.find_first(where=where_params)
    
    async def create(self, segmento: SegmentoCreate):
        return await self.connection.prisma.segmento.create(segmento)
    
    async def update(self, segmento_id: int, segmento: SegmentoUpdate):
        return await self.connection.prisma.segmento.update(where={"id": segmento_id}, data=segmento)

    async def delete(self, segmento_id: int):
        return await self.connection.prisma.segmento.delete(where={"id": segmento_id})
    

    async def generate_graph(self, test: bool = False):
        # Obtén todos los segmentos
        where_conditions = {}
        if not test:
            where_conditions["test"] = test
        segmentos= await self.connection.prisma.segmento.find_many(include={"sucursal_destino":True,"sucursal_origen":True}, where=where_conditions, order=[{"id": "desc"}])

        # Crea un grafo dirigido
        G = nx.DiGraph()

        # Agrega nodos y aristas al grafo
        for segmento in segmentos:
            origen = f"{segmento.sucursal_origen.nombre} ({segmento.sucursal_origen_id})"
            destino = f"{segmento.sucursal_destino.nombre} ({segmento.sucursal_destino_id})"
            distancia = segmento.distancia
            G.add_edge(origen, destino, distancia=distancia)

        # Dibuja el grafo
        pos = nx.spring_layout(G, center=(0.5, 0.5))  # Centra el grafo en el punto (0.5, 0.5)
        labels = nx.get_edge_attributes(G, 'distancia')

        # Ajustes visuales para mejorar el estilo
        plt.figure(figsize=(10, 8))
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightgray', font_size=8, font_color='black',
                font_weight='bold', edge_color='darkgray', width=2, alpha=0.7)

        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=6)  # Ajusta el tamaño de la fuente

        # Guarda la imagen en un objeto BytesIO
        img_stream = BytesIO()
        plt.savefig(img_stream, format='png', bbox_inches='tight', pad_inches=0.2)
        img_stream.seek(0)

        # Convierte la imagen a base64
        base64_img = base64.b64encode(img_stream.read()).decode('utf-8')

        return base64_img
