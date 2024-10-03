import os

def limpiar_pantalla():
    """Funcion que limpia la pantalla,
    segun el sistema operativo"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')