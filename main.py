
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
                suma(*seleccion_numeros())
            case 2:
                resta(*seleccion_numeros())
            case 3:
                division(*seleccion_numeros())
            case 4:
                multiplicacion(*seleccion_numeros())
            case 0:
                print("Gracias por usar nuestra aplicacion!!")
                break
            case _:
                print("Selecciones una opcion habilitada: ")


if __name__ == "__main__":
    main()
