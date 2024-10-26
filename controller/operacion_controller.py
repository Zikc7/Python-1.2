import questionary


from models.operacion_model import Operacion
from helpers.utils import limpiar_pantalla
from helpers.error_treatment import tratamiento_opc_cambiar_op
from helpers.questionary import estilo_personalizado
from core.historial_operaciones import guardar_historial, mostrar_historial, eliminar_historial, modificar_op


class OperacionModel:

    @classmethod
    def iniciar(cls):
        """Funcion iniciadora, llama y trabaja con todas las demas funciones principales"""
        limpiar_pantalla()
        print("Hola bienvenido a la calculadora")
        while True:
            opcion = questionary.select(
                "¿Cual operación desea ejecutar?",

                choices=[
                    "Suma",
                    "Resta",
                    "División",
                    "Multiplicación",
                    "Mostrar Historial de Operaciones",
                    "Eliminar Historial de Operaciones",
                    "Modificar Operaciones",
                    "Salir",
                ], use_arrow_keys=True,
                instruction="Usar Flechas",
                style=estilo_personalizado()).ask()
            match opcion:
                case "Suma":
                    guardar_historial(cls.suma(cls.seleccion_numeros()))
                case "Resta":
                    guardar_historial(cls.resta(cls.seleccion_numeros()))
                case "División":
                    guardar_historial(cls.division(cls.seleccion_numeros()))
                case "Multiplicación":
                    guardar_historial(cls.multiplicacion(
                        cls.seleccion_numeros()))
                case "Mostrar Historial de Operaciones":
                    mostrar_historial()
                case "Eliminar Historial de Operaciones":
                    eliminar_historial()
                case "Modificar Operaciones":
                    cls.op_modif()
                case "Salir":
                    limpiar_pantalla()
                    print("Gracias por usar nuestra aplicacion!!")
                    break

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
        while (True):
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
        while (True):
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
        resultado: str = f"{nueva_op.operando_1} + {nueva_op.operando_2} = {nueva_op.operando_1 + nueva_op.operando_2}"
        nueva_op.resultado_op = resultado
        print(nueva_op.resultado_op)
        return nueva_op

    @classmethod
    def resta(cls, nueva_op: "Operacion") -> "Operacion":
        """Operacion donde se realiza y devuelve el resultado de la resta"""
        limpiar_pantalla()
        resultado: str = f"{nueva_op.operando_1} - {nueva_op.operando_2} = {nueva_op.operando_1 - nueva_op.operando_2}"
        nueva_op.resultado_op = resultado
        print(nueva_op.resultado_op)
        return nueva_op

    @classmethod
    def division(cls, nueva_op: "Operacion") -> "Operacion":
        """Operacion donde se realiza y devuelve el resultado de la división"""
        limpiar_pantalla()
        while True:
            try:
                resultado: str = f"{nueva_op.operando_1} / {nueva_op.operando_2} = {nueva_op.operando_1 / nueva_op.operando_2}"
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
        resultado: str = f"{nueva_op.operando_1} * {nueva_op.operando_2} = {nueva_op.operando_1 * nueva_op.operando_2}"
        nueva_op.resultado_op = resultado
        print(nueva_op.resultado_op)
        return nueva_op

    @classmethod
    def op_modif(cls) -> None:
        """Funcion que pregunta que operacion desea modificar y llama a las funciones base"""
        limpiar_pantalla()
        opcion = questionary.select(
            "¿Cual operación desea modificar?",

            choices=[
                "Suma",
                "Resta",
                "División",
                "Multiplicación",
            ], use_arrow_keys=True,
            instruction="Usar Flechas",
            style=estilo_personalizado()
        ).ask()
        match opcion:
            case "Suma":
                op_nums: "Operacion" = cls.seleccion_numeros()
                tratamiento_opc_cambiar_op(cls.suma, op_nums)
            case "Resta":
                op_nums: "Operacion" = cls.seleccion_numeros()
                tratamiento_opc_cambiar_op(cls.resta, op_nums)
            case "División":
                op_nums: "Operacion" = cls.seleccion_numeros()
                tratamiento_opc_cambiar_op(cls.division, op_nums)
            case "Multiplicación":
                op_nums: "Operacion" = cls.seleccion_numeros()
                tratamiento_opc_cambiar_op(cls.multiplicacion, op_nums)
