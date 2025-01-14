import random

class Predmet:
    def __init__(self, jmeno, min_cena, max_cena):
        self.jmeno = jmeno
        self.min_cena = min_cena
        self.max_cena = max_cena
        self.aktualni_cena = random.randint(min_cena,max_cena)

    def __repr__(self):
        return f"{self.jmeno} {self.min_cena} {self.max_cena} {self.aktualni_cena}"