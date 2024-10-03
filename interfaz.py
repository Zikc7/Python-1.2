from utils import limpiar_pantalla
def menu():
    """Despliega un menu y solo eso"""
    print("Hola bienvenido a la calculadora")
    print("¿Cual operación desea ejecutar?")
    print("1: suma")
    print("2: resta")
    print("3: división")
    print("4: multiplicación")
    print("0: Salir")

def seleccion_operacion() ->float:
    """Funcion donde se solicita el numero que nos dira que operacion usar"""
    opcion : float = float(input("Seleccione la operacion que desea ejecutar: "))
    return opcion

def seleccion_numeros (opcion : float) -> tuple:
    """Segun la operacion les solicita los operandos al usuario,
    si esta es una division verifica que no sean 0"""
    if opcion != 3:
        num1: float = float(input("Ingrese el primer operando: "))
        num2: float = float(input("Ingrese el segundo operando: "))
        return num1,num2
    elif opcion == 3:
        while True:
            num1: float = float(input("Ingrese el primer operando: "))
            num2: float = float(input("Ingrese el segundo operando: "))
            if num1 != 0 and num2 != 0:
                return num1,num2
                break
            else:
                limpiar_pantalla()
                print("Ingrese operandos distintos a 0")