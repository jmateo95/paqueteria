class TipoVehiculo:
    CAMION = 1
    PANEL = 2
    FURGONETA = 3
    PICK_UP = 4

class TipoGasto:
    FIJOS = 1
    VARIABLES = 2
    TRANSPORTE = 3

class ConceptoGasto:
    PLANILLA = 1
    GASOLINA = 2
    LUZ = 3
    AGUA = 4
    INTERNET = 5
    TELEFONO = 6

class TipoSalida:
    PROYECCION = 1
    LISTO_PARA_CARGAR = 2
    CARGANDO = 3
    EN_RUTA = 4
    FIN = 5

class EstadoPaquete:
    RECEPCION = 1
    TRANSITO = 2
    RUTA_FINAL = 3
    ENTREGADO = 4

class EstadoTracking:
    EN_ESPERA = 1
    EN_BODEGA = 2
    CARGANDO = 3
    CARGADO = 4
    EN_RUTA = 5
    COMPLETADO = 6