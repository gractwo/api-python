from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, StreamingResponse
from starlette.status import HTTP_401_UNAUTHORIZED
from typing import Union
from db import db_session
import os
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
