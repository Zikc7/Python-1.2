import json


def leer_archivo(path: str) -> list:
    """Funcion que lee un archivo Json, si no lo encuentra crea uno"""
    try:
        with open(path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        from controller.operacion_controller import Operacion
        escribir_archivo(path, [Operacion.__dict__ for op in Operacion.all])
        return []


def escribir_archivo(path: str, content: list) -> None:
    """Funcion que escribe en un archivo Json o lo crea"""
    with open(path, "w") as file:
        json.dump(content, file, indent=4)


def borrar_archivo(path: str) -> None:
    """Funcion que elimina el contenido de un archivo Json"""
    with open(path, "w") as file:
        file.write("[]")
    print("Se elimino el historial")
