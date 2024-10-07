
from core.operaciones import division, suma, resta, multiplicacion
from helpers.utils import limpiar_pantalla
from core.interfaz import menu, seleccion_numeros, seleccion_operacion


def main():
    print("Hola bienvenido a la calculadora")
    while True:
        menu()
        opcion: float = seleccion_operacion()
        match opcion:
            case 1:
                operando_1, operando_2 = seleccion_numeros(opcion)
                limpiar_pantalla()
                suma(operando_1, operando_2)
            case 2:
                operando_1, operando_2 = seleccion_numeros(opcion)
                limpiar_pantalla()
                resta(operando_1, operando_2)
            case 3:
                operando_1, operando_2 = seleccion_numeros(opcion)
                limpiar_pantalla()
                division(operando_1, operando_2)
            case 4:
                operando_1, operando_2 = seleccion_numeros(opcion)
                limpiar_pantalla()
                multiplicacion(operando_1, operando_2)
            case 0:
                limpiar_pantalla()
                print("Gracias por usar nuestra aplicacion!!")
                break
            case _:
                limpiar_pantalla()
                print("Selecciones una opcion viable: ")


if __name__ == "__main__":
    main()
