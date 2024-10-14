from models.operacion_model import Operacion
from helpers.utils import limpiar_pantalla
from core.historial_operaciones import guardar_historial,mostrar_historial

class OperacionModel:

    @classmethod
    def iniciar(cls):
        limpiar_pantalla()
        print("Hola bienvenido a la calculadora")
        while True:
            print("¿Cual operación desea ejecutar?")
            print("1: Suma")
            print("2: Resta")
            print("3: División")
            print("4: Multiplicación")
            print("5: Mostrar Historial de Operaciones")
            print("6: Eliminar Historial de Operaciones")
            print("0: Salir")
            opcion: float = cls.seleccion_operacion()
            match opcion:
                case 1:
                    cls.suma(cls.seleccion_numeros())
                case 2:
                    cls.resta(cls.seleccion_numeros())
                case 3:
                    cls.division(cls.seleccion_numeros())
                case 4:
                    cls.multiplicacion(cls.seleccion_numeros())
                case 5:
                    mostrar_historial()
                #case 6:
                    #!eliminar_historial() Se esta probrando jejeje
                case 0:
                    print("Gracias por usar nuestra aplicacion!!")
                    break
                case _:
                    print("Selecciones una opcion habilitada: ")

    @classmethod
    def seleccion_operacion(cls) -> float:
        """Funcion donde se solicita el numero que nos dira que operacion usar"""
        try:
            opcion: float = float(
                input("Seleccione la operacion que desea ejecutar: "))
            
            return opcion
        except ValueError as ex:
            limpiar_pantalla()
            print(f"{ex} Se esperaba un número")
            cls.seleccion_operacion()

    @classmethod
    def seleccion_numeros(cls) -> "Operacion":
        """Segun la operacion les solicita los operandos al usuario,
        si esta es una division verifica que no sean 0"""
        try:
            num1: float = float(input("Ingrese el primer operando: "))
            num2: float = float(input("Ingrese el segundo operando: "))
            nueva_op = Operacion(operando_1=num1,operando_2=num2)
            Operacion.all.append(nueva_op)
            return nueva_op
        except ValueError as ex:
            limpiar_pantalla()
            print(f"{ex} Se esperaba un número")
            cls.seleccion_numeros()

    @classmethod
    def suma(cls, nueva_op : "Operacion") -> str:
        """Funcion donde se realiza y devuelva el resusltado de la suma"""
        limpiar_pantalla()
        resultado: str =  f"{nueva_op.operando_1} + {nueva_op.operando_2} = {nueva_op.operando_1 + nueva_op.operando_2}"
        nueva_op.resultado_op= resultado
        guardar_historial(nueva_op)
        print(resultado)

    @classmethod
    def resta(cls,nueva_op : "Operacion") -> str:
        """Operacion donde se realiza y devuelve el resultado de la resta"""
        limpiar_pantalla()
        resultado: str =  f"{nueva_op.operando_1} - {nueva_op.operando_2} = {nueva_op.operando_1 - nueva_op.operando_2}"
        nueva_op.resultado_op= resultado
        guardar_historial(nueva_op)
        print(resultado)

    @classmethod
    def division(cls,nueva_op: "Operacion") -> str:
        """Operacion donde se realiza y devuelve el resultado de la división"""
        limpiar_pantalla()
        try:
            resultado: str =  f"{nueva_op.operando_1} / {nueva_op.operando_2} = {nueva_op.operando_1 / nueva_op.operando_2}"
            nueva_op.resultado_op= resultado
            guardar_historial(nueva_op)
            print(resultado)
        except ZeroDivisionError as ex:
            print(f"{ex} No se puede dividir por 0, Ingrese un número valido")
            cls.division(cls.seleccion_numeros())

    @classmethod
    def multiplicacion(cls,nueva_op: "Operacion") -> str:
        """Operacion donde se realiza y devuelve el resultado de la multiplicación"""
        limpiar_pantalla()
        resultado: str =  f"{nueva_op.operando_1} * {nueva_op.operando_2} = {nueva_op.operando_1 * nueva_op.operando_2}"
        nueva_op.resultado_op= resultado
        guardar_historial(nueva_op)
        print(resultado)