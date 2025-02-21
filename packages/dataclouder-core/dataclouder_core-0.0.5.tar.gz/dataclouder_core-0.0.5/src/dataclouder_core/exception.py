import sys, traceback

from typing_extensions import Any
from fastapi import status, HTTPException


async def handle_app_exception(e: Exception):
    # TODO Retomar la aproximación de AppException
    # TODO para el mensaje me parece que hay una nueva forma de regresar la exception que no teniamos antes si no quiero que este en detail
    # https://fastapi.tiangolo.com/tutorial/handling-errors/

    if 'AppException' in str(e.__class__):
        print("Ocurrió una exeption controlada")
        print(e)
        code = e.code if e.code != None else status.HTTP_400_BAD_REQUEST
        print("el codigo es", e.code)
        raise HTTPException(code, detail=vars(e))
    else:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        first = {'type': str(exception_type), 'file_name': str(filename), 'line': str(line_number)}
        # print(first)
        formatted_lines = traceback.format_exc().splitlines()
        second = {
            'last_file': formatted_lines[-3],
            'last_line': formatted_lines[-2],
            'last_reason': formatted_lines[-1]
        }
        # print(second)
        # err = {"message": str(e), "code_data": first , "code_data2": second}
        err = AppException(error_message=str(e), stack_messages=first, stack_methods=second)

        print("__Ocurrió una excepción no controlada___", err, err.stack_methods)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=vars(err))


class AppException(Exception):

    error_message: str
    explanation: str
    code: int
    method: str
    obj: dict[Any]
    stack_messages: list[str]
    stack_methods: list[str]

    def __init__(self,
                 error_message: str,
                 explanation: str = None,
                 code: int = 400,
                 method: str = None,
                 obj: dict[Any] = None,
                 stack_messages: list[str] = None,
                 stack_methods: list[str] = None):
        """Iniciar la clase de error de la aplicación

        Args:
            error_message (str): mensaje principal del error
            explanation: (str): mensaje entendible para el usuario
            code (int): código de error
            method (str): metódo donde ocurrió el error
            obj (Dict): objeto principal que existia cuando el error ocurrió
            messages (list[str]): messages apilados de error
            methods (list[str]): metódos apilados de los errores
        """

        self.error_message = error_message
        self.code = code
        self.method = method
        self.obj = obj
        self.explanation = explanation
        self.stack_messages = stack_messages
        self.stack_methods = stack_methods

    def __str__(self):
        return repr(f"{self.error_message} en {self.method}")


# ---- DECORATORS ----
# Aqui se encuentra la idea del decorador agrega try except y maneta la excepcion estandar
# https://stackoverflow.com/questions/64497615/how-to-add-a-custom-decorator-to-a-fastapi-route
from functools import wraps

def handler_exception(func):
    @wraps(func)
    async def inner_function(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            await handle_app_exception(e)
    return inner_function 