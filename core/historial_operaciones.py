from helpers.file_helpers import leer_archivo,escribir_archivo,borrar_archivo
from config import constant
from helpers.utils import limpiar_pantalla
from models.operacion_model import Operacion


def guardar_historial(op : "Operacion"):
    """Recibe un str de la operacion ejecutada y lo guarda en el archivo historial calculadora.json"""
    historial: list[dict]= leer_archivo(constant.HISTORIAL_PATH)
    historial.append(op.__dict__)
    escribir_archivo(constant.HISTORIAL_PATH,historial )
    #?[op.__dict__ for op in Operacion.all]



def mostrar_historial() -> list[str]:
    """Muestra el historial a travez de la funcion leer_archivo retorna una lista y la enseña
    , en caso de no haber historial muestra el msj pertinente"""
    historial: list[dict] = leer_archivo(constant.HISTORIAL_PATH,)
    limpiar_pantalla()
    if historial:
        print("El historial es: ")
        for i,  operacion in enumerate (historial, start = 1):
            resultado_historial= f"La operacion n°{i}: {operacion.get("_resultado_op")}"
            print(resultado_historial)
    else:
        print("El historial esta vacio")

def eliminar_historial():
    """Elimina el historial"""
    borrar_archivo(constant.HISTORIAL_PATH)