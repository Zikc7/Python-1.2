
from core.historial_operaciones import modificar_op
# from controller.operacion_controller import OperacionModel


def tratamiento_opc_cambiar_op(operaciones_varias, seleccion_num_op) -> None:
    """Funcion encargada de recibir la modificacion de una operacion y tratar sus posibles errores"""
    try:
        modificar_op(operaciones_varias(seleccion_num_op))
    except ValueError as ex:
        print(f"{ex}: Error al modificar la operación. Ingrese un número válido.")
        tratamiento_opc_cambiar_op(operaciones_varias, seleccion_num_op)
    except IndexError as ex:
        print(
            f"{ex}: Error al modificar la operación. Ingrese un número de operacion valido válido.")
        tratamiento_opc_cambiar_op(operaciones_varias, seleccion_num_op)
