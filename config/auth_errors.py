class UnauthorizedError(Exception):
    def __init__(self, detail="No tienes permisos de administrador"):
        self.detail = detail

class TokenExpiredError(Exception):
    def __init__(self, detail="Token expirado"):
        self.detail = detail

class InvalidTokenError(Exception):
    def __init__(self, detail="Token inválido"):
        self.detail = detail