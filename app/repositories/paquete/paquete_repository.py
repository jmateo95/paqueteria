from app.models.paquete.paquete_model import PaqueteCreate, PaqueteUpdate, PaqueteCotizar
import calendar
from config.Connection import prisma_connection
from datetime import datetime
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from barcode import Code128
from barcode.writer import ImageWriter
import base64
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

class PaqueteRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_paquetes_by_filters(self, salida_id:int=None, tipo_tracking_id:int=None, estado_paquete_id:int=None, sucursal_id:int=None):
        query = """
            SELECT DISTINCT ON (P.id) P.*, 
            (
                SELECT SU1.nombre
                FROM public."Tracking" T1 
                INNER JOIN public."Salida" S1 ON T1.salida_id = S1.id
                INNER JOIN public."Segmento" SE1 ON S1.segmento_id = SE1.id
                INNER JOIN public."Sucursal" SU1 ON SE1.sucursal_origen_id = SU1.id
                WHERE T1.paquete_id = P.id 
                ORDER BY T1.id ASC 
                LIMIT 1
            ) AS origen,
            (
                SELECT SU2.nombre
                FROM public."Tracking" T2 
                INNER JOIN public."Salida" S2 ON T2.salida_id = S2.id
                INNER JOIN public."Segmento" SE2 ON S2.segmento_id = SE2.id
                INNER JOIN public."Sucursal" SU2 ON SE2.sucursal_destino_id = SU2.id
                WHERE T2.paquete_id = P.id 
                ORDER BY T2.id DESC 
                LIMIT 1
            ) AS destino
            FROM public."Paquete" P
            INNER JOIN public."Tracking" T ON P.id = T.paquete_id
            WHERE 1=1
        """
        if salida_id is not None:
            query += f"AND T.salida_id = {salida_id}\n"
        if tipo_tracking_id is not None:
            query += f"AND T.estado_tracking_id = {tipo_tracking_id}\n"
        if estado_paquete_id is not None:
            query += f"AND P.estado_paquete_id = {estado_paquete_id}\n"
        if sucursal_id is not None:
            query += f"AND T.sucursal_id = {sucursal_id}\n"
        return await self.connection.prisma.query_raw(query)

    async def get_by_id(self, paquete_id: int):
        return await self.connection.prisma.paquete.find_first(where={"id": paquete_id})
    
    async def get_by_no_guia(self, no_guia: str):
        return await self.connection.prisma.paquete.find_first(where={"no_guia": no_guia})
    
    async def create(self, paquete: PaqueteCreate):
        return await self.connection.prisma.paquete.create(paquete)
    
    async def update(self, paquete_id: int, paquete: PaqueteUpdate):
        return await self.connection.prisma.paquete.update(where={"id": paquete_id}, data=paquete)

    async def delete(self, paquete_id: int):
        return await self.connection.prisma.paquete.delete(where={"id": paquete_id})
    
    async def numero_paquetes(self, fecha:datetime=None):
        query = """
            SELECT *
                FROM (
                    SELECT
                        p.*,
                        (
                            SELECT MAX(actualizacion)
                            FROM "Tracking"
                            WHERE paquete_id = p.id
                        ) AS fecha
                    FROM "Paquete" p
                ) AS subquery
            WHERE 1 = 1
        """
        if fecha is not None:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            query += f"AND fecha BETWEEN '{first_day}' AND '{last_day}'\n"
        return await self.connection.prisma.query_raw(query)

    async def peso_promedio(self, fecha:datetime=None):
        query = """
            SELECT avg(peso) peso
                FROM (
                    SELECT
                        p.*,
                        (
                            SELECT MAX(actualizacion)
                            FROM "Tracking"
                            WHERE paquete_id = p.id
                        ) AS fecha
                    FROM "Paquete" p
                ) AS subquery
            WHERE 1 = 1
        """
        if fecha is not None:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            query += f"AND fecha BETWEEN '{first_day}' AND '{last_day}'\n"
        return await self.connection.prisma.query_raw(query)
    
    async def costo_promedio(self, fecha:datetime=None):
        query = """
            SELECT avg(costo) costo
                FROM (
                    SELECT
                        p.*,
                        (
                            SELECT MAX(actualizacion)
                            FROM "Tracking"
                            WHERE paquete_id = p.id
                        ) AS fecha
                    FROM "Paquete" p
                ) AS subquery
            WHERE 1 = 1
        """
        if fecha is not None:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            query += f"AND fecha BETWEEN '{first_day}' AND '{last_day}'\n"
        return await self.connection.prisma.query_raw(query)
    

    async def paquetes_estado(self, fecha:datetime=None):
        query = """
            SELECT count (p.id) as value, ep.nombre as name
                FROM (
                    SELECT
                        p.*,
                        (
                            SELECT MIN(actualizacion)
                            FROM "Tracking"
                            WHERE paquete_id = p.id
                        ) AS fecha
                    FROM "Paquete" p
                ) AS p
            JOIN "EstadoPaquete" ep ON ep.id = p.estado_paquete_id
            WHERE 1 = 1
        """
        if fecha is not None:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            query += f"AND fecha BETWEEN '{first_day}' AND '{last_day}'\n"
        query += f"GROUP BY ep.nombre\n"
        return await self.connection.prisma.query_raw(query)
    
    async def draw_centered_text(self, canvas, text, x, y, font, size):
        canvas.setFont(font, size)
        width = canvas.stringWidth(text, font, size)
        canvas.drawCentredString((x+75) - (width / 2), y, text)
    
    async def generate_pdf(self, paquete):
        # Crear un objeto de lienzo PDF
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=(500, 350))  # Ajusté el tamaño a uno más ancho

        # Configuración del título en el centro de la página
        await self.draw_centered_text(p, "LA ENCOMIENDA", 250, 310, "Helvetica-Bold", 16)

        # Línea horizontal
        p.line(30, 300, 470, 300)  # Ajusté la línea para que siga la extensión de la página

        # Configuración del costo, peso y volumen
        p.setFont("Helvetica", 12)
        p.drawString(30, 280, f"Costo: Q{paquete['costo']:.2f}")
        p.drawString(200, 280, f"Peso: {paquete['peso']} lb")
        p.drawString(350, 280, f"Volumen: {paquete['volumen']} cc")

        # Línea horizontal
        p.line(30, 270, 470, 270)

        # Configuración del código de barras con más espacio
        code128 = Code128(str(paquete['no_guia']), writer=ImageWriter())
        code128_path = code128.save('temp_code128.png')
        # Centrar la imagen del código de barras
        img_width, img_height = 250, 50
        img_x = (500 - img_width) / 2
        img_y = 210
        p.drawInlineImage(code128_path, img_x, img_y, width=img_width, height=img_height)

        # Línea horizontal
        p.line(30, 200, 470, 200)

        # Configuración del código de barras de texto con letra más pequeña y centrado
        p.setFont("Helvetica", 8)  # Reduje el tamaño de la fuente para el número de guía
        p.drawCentredString(250, 180, f"No. de Guía: {paquete['no_guia']}")

        # Línea horizontal
        p.line(30, 150, 470, 150)

        # Configuración de la información de sucursales
        p.drawString(30, 130, "Sucursal Destino:")
        p.drawString(30, 110, paquete['destino'])
        p.drawString(250, 130, "Sucursal Origen:")
        p.drawString(250, 110, paquete['origen'])

        # Línea horizontal
        p.line(30, 90, 470, 90)

        # Configuración de la información de remitente y destinatario
        p.drawString(30, 70, "Remitente:")
        p.drawString(30, 50, paquete['remitente'])
        p.drawString(250, 70, "Destinatario:")
        p.drawString(250, 50, paquete['destinatario'])

        p.showPage()
        p.save()

        # Reset del buffer para lecturas posteriores
        buffer.seek(0)
        return base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    async def pdf(self, no_guia: str):
        query = """
            SELECT DISTINCT ON (P.id) P.*, 
            (
                SELECT SU1.nombre
                FROM public."Tracking" T1 
                INNER JOIN public."Salida" S1 ON T1.salida_id = S1.id
                INNER JOIN public."Segmento" SE1 ON S1.segmento_id = SE1.id
                INNER JOIN public."Sucursal" SU1 ON SE1.sucursal_origen_id = SU1.id
                WHERE T1.paquete_id = P.id 
                ORDER BY T1.id ASC 
                LIMIT 1
            ) AS origen,
            (
                SELECT SU2.nombre
                FROM public."Tracking" T2 
                INNER JOIN public."Salida" S2 ON T2.salida_id = S2.id
                INNER JOIN public."Segmento" SE2 ON S2.segmento_id = SE2.id
                INNER JOIN public."Sucursal" SU2 ON SE2.sucursal_destino_id = SU2.id
                WHERE T2.paquete_id = P.id 
                ORDER BY T2.id DESC 
                LIMIT 1
            ) AS destino
            FROM public."Paquete" P
            INNER JOIN public."Tracking" T ON P.id = T.paquete_id
            
        """
        query += f"WHERE no_guia='{no_guia}'\n"
        paquetes= await self.connection.prisma.query_raw(query)
        paquete=paquetes[0]
        pdf= await self.generate_pdf(paquete)
        return pdf

