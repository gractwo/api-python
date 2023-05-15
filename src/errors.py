from starlette.exceptions import HTTPException


class BadRequest(HTTPException):
    def __init__(self, msg: str):
        super().__init__(status_code=400, detail=msg)


class NotFound(HTTPException):
    def __init__(self, msg: str):
        super().__init__(status_code=404, detail=msg)


class Conflict(HTTPException):
    def __init__(self, msg: str):
        super().__init__(status_code=409, detail=msg)


class ServerError(HTTPException):
    def __init__(self, msg: str):
        super().__init__(status_code=500, detail=msg)
