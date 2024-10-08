from helpers.utils import limpiar_pantalla


def menu():
    """Despliega un menu y solo eso"""
    print("¿Cual operación desea ejecutar?")
    print("1: Suma")
    print("2: Resta")
    print("3: División")
    print("4: Multiplicación")
    print("5: Mostrar Historial de Operaciones")
    print("6: Eliminar Historial de Operaciones")
    print("0: Salir")


def seleccion_operacion() -> float:
    """Funcion donde se solicita el numero que nos dira que operacion usar"""
    try:
        opcion: float = float(
            input("Seleccione la operacion que desea ejecutar: "))
        return opcion
    except ValueError as ex:
        limpiar_pantalla()
        print(f"{ex} Se esperaba un número")
        seleccion_operacion()


def seleccion_numeros() -> tuple:
    """Segun la operacion les solicita los operandos al usuario,
    si esta es una division verifica que no sean 0"""
    try:
        num1: float = float(input("Ingrese el primer operando: "))
        num2: float = float(input("Ingrese el segundo operando: "))
        return num1, num2
    except ValueError as ex:
        limpiar_pantalla()
        print(f"{ex} Se esperaba un número")
        seleccion_numeros()
