import math
from src.logic.exceptions import NoSePuedeCalcular

class Media:
    def __init__(self, elementos=None):
        self.elementos = elementos if elementos is not None else []

    def calcular_media(self):
        if not self.elementos:
            raise NoSePuedeCalcular("No se puede calcular la media: la lista está vacía")
        return sum(self.elementos) / len(self.elementos)

class DesviacionEstandar:
    def __init__(self, elementos=None):
        self.elementos = elementos if elementos is not None else []

    def calcular(self):
        if not self.elementos:
            raise NoSePuedeCalcular("No se puede calcular la desviación estándar: la lista está vacía")
        if len(self.elementos) == 1:
            return 0
        media = Media(self.elementos).calcular_media()
        varianza = sum((x - media) ** 2 for x in self.elementos) / (len(self.elementos) - 1)
        return math.sqrt(varianza)