from models.operacion_model import Operacion
from helpers.utils import limpiar_pantalla
from helpers.error_treatment import tratamiento_opc_cambiar_op
from core.historial_operaciones import guardar_historial, mostrar_historial, eliminar_historial,modificar_op

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
            print("7: Modificar Operaciones")
            print("0: Salir")
            opcion: float = cls.seleccion_operacion()
            match opcion:
                case 1:
                    guardar_historial(cls.suma(cls.seleccion_numeros()))
                case 2:
                    guardar_historial(cls.resta(cls.seleccion_numeros()))
                case 3:
                    guardar_historial(cls.division(cls.seleccion_numeros()))
                case 4:
                    guardar_historial(cls.multiplicacion(cls.seleccion_numeros()))
                case 5:
                    mostrar_historial()
                case 6:
                    eliminar_historial()
                case 7:
                    cls.op_modif()
                case 0:
                    limpiar_pantalla()
                    print("Gracias por usar nuestra aplicacion!!")
                    break
                case _:
                    limpiar_pantalla()
                    print("Selecciones una opcion habilitada: ")


    @classmethod
    def seleccion_operacion(cls) -> float:
        """Funcion donde se solicita el numero que nos dira que operacion usar"""
        while True:
            try:
                opcion: float = float(
                    input("Seleccione la operacion que desea ejecutar: "))
                return opcion
                break
            except ValueError as ex:
                limpiar_pantalla()
                print(f"{ex} Se esperaba un número")
    @classmethod
    def seleccion_numeros(cls) -> "Operacion":
        """Segun la operacion les solicita los operandos al usuario,
        si esta es una division verifica que no sean 0"""
        while(True):
            try:
                num1: float = float(input("Ingrese el primer operando: "))
                num2: float = float(input("Ingrese el segundo operando: "))
                nueva_op = Operacion(operando_1=num1, operando_2=num2)
                Operacion.all.append(nueva_op)
                return nueva_op
                break
            except ValueError as ex:
                limpiar_pantalla()
                print(f"{ex} Se esperaba un número")
    @classmethod
    def seleccion_numeros_modificar(cls) -> "Operacion":
        """Segun la operacion les solicita los operandos al usuario,
        si esta es una division verifica que no sean 0"""
        while(True):
            try:
                num1: float = float(input("Ingrese el primer operando: "))
                num2: float = float(input("Ingrese el segundo operando: "))
                nueva_op = Operacion(operando_1=num1, operando_2=num2)
                return nueva_op
                break
            except ValueError as ex:
                limpiar_pantalla()
                print(f"{ex} Se esperaba un número")
                    

    @classmethod
    def suma(cls, nueva_op: "Operacion") -> "Operacion":
        """Funcion donde se realiza y devuelva el resusltado de la suma"""
        limpiar_pantalla()
        resultado: str = f"{nueva_op.operando_1} + {nueva_op.operando_2} = {
            nueva_op.operando_1 + nueva_op.operando_2}"
        nueva_op.resultado_op = resultado
        print(nueva_op.resultado_op)
        return nueva_op

    @classmethod
    def resta(cls, nueva_op: "Operacion") -> "Operacion":
        """Operacion donde se realiza y devuelve el resultado de la resta"""
        limpiar_pantalla()
        resultado: str = f"{nueva_op.operando_1} - {nueva_op.operando_2} = {
            nueva_op.operando_1 - nueva_op.operando_2}"
        nueva_op.resultado_op = resultado
        print(nueva_op.resultado_op)
        return nueva_op
    @classmethod
    def division(cls, nueva_op: "Operacion") -> "Operacion":
        """Operacion donde se realiza y devuelve el resultado de la división"""
        limpiar_pantalla()
        while True:
            try:
                resultado: str = f"{nueva_op.operando_1} / {nueva_op.operando_2} = {
                    nueva_op.operando_1 / nueva_op.operando_2}"
                nueva_op.resultado_op = resultado
                print(nueva_op.resultado_op)
                return nueva_op
                break
            except ZeroDivisionError as ex:
                print(f"{ex} No se puede dividir por 0, Ingrese un número valido")
                return cls.division(cls.seleccion_numeros())

    @classmethod
    def multiplicacion(cls, nueva_op: "Operacion") -> "Operacion":
        """Operacion donde se realiza y devuelve el resultado de la multiplicación"""
        limpiar_pantalla()
        resultado: str = f"{nueva_op.operando_1} * {nueva_op.operando_2} = {
            nueva_op.operando_1 * nueva_op.operando_2}"
        nueva_op.resultado_op = resultado
        print(nueva_op.resultado_op)
        return nueva_op

    @classmethod
    def op_modif(cls) -> None:
        limpiar_pantalla()
        print("¿Cual operación desea ejecutar?")
        print("1: Suma")
        print("2: Resta")
        print("3: División")
        print("4: Multiplicación")
        opcion: float = cls.seleccion_operacion()
        match opcion:
            case 1:
                    op_nums :"Operacion" = cls.seleccion_numeros()
                    tratamiento_opc_cambiar_op(cls.suma,op_nums)
            case 2:
                    op_nums :"Operacion" = cls.seleccion_numeros()
                    tratamiento_opc_cambiar_op(cls.resta,op_nums)
            case 3:
                    op_nums :"Operacion" = cls.seleccion_numeros()
                    tratamiento_opc_cambiar_op(cls.division,op_nums)
            case 4:
                    op_nums :"Operacion" = cls.seleccion_numeros()
                    tratamiento_opc_cambiar_op(cls.multiplicacion,op_nums)
            case _:
                print("Ingrese un numero de operacion valido")
                cls.op_modif()