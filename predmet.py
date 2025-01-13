import random

class Predmet:
    def __init__(self, jmeno, min_cena, max_cena):
        self.jmeno = jmeno
        self.min_cena = min_cena
        self.max_cena = max_cena
        self.aktualni_cena = random.randint(min_cena,max_cena)

    def __repr__(self):
        return f"{self.jmeno} {self.min_cena} {self.max_cena} {self.aktualni_cena}"

    def zmen_cenu(self):
            zmena = random.randint(-5,5)
            nova_cena = self.aktualni_cena + zmena
            if nova_cena < self.min_cena:
             nova_cena = self.min_cena
            elif nova_cena > self.max_cena:
                nova_cena = self.max_cena
            self.aktualni_cena = nova_cena

    '''def zmen_ceny(self):
        zmena = random.randint(-5,5)
        nova_cena = self.aktualni_cena + zmena
        if nova_cena < self.min_cena:
            nova_cena = self.min_cena
        elif nova_cena > self.max_cena:
            nova_cena = self.max_cena
        self.aktualni_cena = nova_cena'''

'''
utopenec = Predmet("Utopenec", 50, 100)
med = Predmet("Utopenec", 200, 400)
print(utopenec)
utopenec.zmen_cenu()
print(utopenec)
print(med)
'''