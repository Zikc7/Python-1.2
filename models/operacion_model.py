

class Operacion:
    all = []

    def __init__(self, operando_1: float, operando_2: float, resultado_op: str = 0) -> None:

        self.operando_1 = operando_1
        self.operando_2 = operando_2
        self._resultado_op = resultado_op
    @property
    def resultado_op(self):
        return self._resultado_op

    @resultado_op.setter
    def resultado_op(self, resultado_op: str):
        self._resultado_op = resultado_op
