import jwt
from datetime import datetime, timedelta
from config.auth_errors import TokenExpiredError, UnauthorizedError, InvalidTokenError
from config.config import settings
from schema import ResponseSchema
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
auth = HTTPBearer()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def validate_token(token, allowed_roles):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload["rol"] in allowed_roles:
            return payload
        else:
            raise UnauthorizedError()
    except jwt.ExpiredSignatureError:
        raise TokenExpiredError()
    except jwt.InvalidTokenError:
        raise InvalidTokenError()


def get_current_user_with_roles(allowed_roles: list = None):
    def _get_current_user(authorization: HTTPAuthorizationCredentials = Depends(auth)):
        try:
            token = authorization.credentials  # Obtiene el token del objeto HTTPAuthorizationCredentials
            roles_to_check = allowed_roles if allowed_roles is not None else ["Admin"]  # Usar los roles permitidos o el rol predeterminado
            payload = validate_token(token, roles_to_check)
            return payload
        except UnauthorizedError as e:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permisos para acceder a este recurso.")
        except TokenExpiredError as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Tu token de acceso ha expirado.")
        except InvalidTokenError as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El token no es válido.")
    return _get_current_user