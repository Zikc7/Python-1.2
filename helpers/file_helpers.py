import json


def leer_archivo(path: str) -> list:
    try:
        with open(path, "r") as file:
            return json.load(file)
    except:
        pass


def escribir_archivo(path: str, content: list) -> None:
    with open(path, "w") as file:
        asdas
