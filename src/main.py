import os
from typing import Union

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, StreamingResponse
from starlette.status import HTTP_401_UNAUTHORIZED

from db import db_session

app = FastAPI(
    title="GractwoApi",
    version="0.1.0",
)

app.include_router()
app.include_router()
