import questionary
from questionary import Style


def estilo_personalizado():
        return Style([
        ("questionmark", "bold blue"),
        ("selected", "bg:#00ffff white"),
        ("pointer", "bold cyan"),
        ("answer", "bold green"),
        ("question", "bold magenta")])

