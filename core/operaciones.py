from helpers.utils import limpiar_pantalla
from core.interfaz import seleccion_numeros

def suma(num1: float, num2: float) -> float:
    """Funcion donde se realiza y devuelva el resusltado de la suma"""
    limpiar_pantalla()
    print(f"La suma de {num1} + {num2} = {num1 + num2}")


def resta(num1: float, num2: float) -> float:
    """Operacion donde se realiza y devuelve el resultado de la resta"""
    limpiar_pantalla()
    print(f"La resta de {num1} - {num2} = {num1 - num2}")


def division(num1: float, num2: float) -> float:
    """Operacion donde se realiza y devuelve el resultado de la división"""
    limpiar_pantalla()
    try:
        print(f"La division de {num1} / {num2} = {num1 / num2}")
    except ZeroDivisionError as ex:
        print(f"{ex} No se puede dividir por 0, Ingrese un número valido")
        division(*seleccion_numeros())

def multiplicacion(num1: float, num2: float) -> float:
    """Operacion donde se realiza y devuelve el resultado de la multiplicación"""
    limpiar_pantalla()
    print(f"La multiplicación de {num1} x {num2} = {num1 * num2}")
