from fastapi import Request
from fastapi.responses import JSONResponse

class CustomException(BaseException):
    def __init__(self, name: str, description: str, status_code: int):
        self.name = name
        self.description = description
        self.status_code = status_code
        super().__init__(self.description)


class ItemNotFoundException(CustomException):
    def __init__(self, item_id: int):
        super().__init__(name="Item Not Found",
                         description=f"Item with ID {item_id} not found",
                         status_code=404)


class UnauthorizedException(CustomException):
    def __init__(self):
        super().__init__(name="Unauthorized",
                         description="You are not authorized to perform this action",
                         status_code=401)


def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.name, "message": exc.description}
    )
