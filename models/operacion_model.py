

class Operacion:
    all = []

    def __init__(self, operando_1: float, operando_2: float, resultado_op: str = 0) -> None:

        self.operando_1 = operando_1
        self.operando_2 = operando_2
        #!Vamos a definir resultado con un setter dependiendo del metodo que se ejecute, suma,resta,etc. creo
        self._resultado_op = resultado_op
    """Usar getters y setter en todos porque tienen que seleccionar la operacion y ejecutar cambiando los operandos o la misma"""
    @property
    def resultado_op(self):
        return self._resultado_op

    @resultado_op.setter
    def resultado_op(self, resultado_op: str):
        self._resultado_op = resultado_op
