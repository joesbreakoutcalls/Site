
from fastapi import Request, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

security = HTTPBasic()

USERNAME = "JoeIsAwesome"
PASSWORD = "ClemsonTigers"

def basic_auth(credentials: HTTPBasicCredentials = None):
    if credentials is None or credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
