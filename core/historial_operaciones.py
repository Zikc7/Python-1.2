from helpers.file_helpers import leer_archivo,escribir_archivo,borrar_archivo
from config import constant
from helpers.utils import limpiar_pantalla

def guardar_historial(operacion : str):
    """Recibe un str de la operacion ejecutada y lo guarda en el archivo historial calculadora.json"""
    historial = leer_archivo(constant.HISTORIAL_PATH)
    historial.append(operacion)
    escribir_archivo(constant.HISTORIAL_PATH, historial)


def mostrar_historial() -> list[str]:
    """Muestra el historial a travez de la funcion leer_archivo retorna una lista y la enseña
    , en caso de no haber historial muestra el msj pertinente"""
    historial = leer_archivo(constant.HISTORIAL_PATH,)
    limpiar_pantalla()
    if historial:
        print("El historial es: ")
        for operacion in historial:
            print(operacion.strip())
    else:
        print("El historial esta vacio")

def eliminar_historial():
    """Elimina el historial"""
    borrar_archivo(constant.HISTORIAL_PATH)
    pass