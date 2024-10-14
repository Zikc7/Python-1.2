import json


def leer_archivo(path: str) -> list:
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError as ex:
        from controller.operacion_controller import Operacion
        escribir_archivo(path,[Operacion.__dict__ for op in Operacion.all])
        return []


def escribir_archivo(path: str, content: list) -> None:
    with open(path, "w") as file:
        json.dump(content, file, indent=4)


def borrar_archivo(path: str) -> None:
    with open(path, "w") as file:
        file.truncate(0)
    print("Se elimino el historial")
