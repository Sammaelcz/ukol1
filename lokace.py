#from predmet import Predmet
import random

class Lokace:
    def __init__(self, jmeno, predmety):
        self.jmeno = jmeno
        self.predmety = predmety

    def __repr__(self):
        return f"{self.jmeno} {self.predmety}"

    def vypis_predmety(self):
        for polozka in self.predmety:
            print(f"{polozka.jmeno} {polozka.aktualni_cena},- Kč")

    def vypis_predmety_index(self):
        vypis_predmety_index = 1
        print("Aktuálně nabízené předměty:")
        for polozka in self.predmety:
            print(f"{vypis_predmety_index} - {polozka.jmeno} {polozka.aktualni_cena},- Kč")
            vypis_predmety_index += 1

    '''def zmen_ceny(self):
        for predmet in self.predmety:
            predmet.zmen_cenu()'''

    def zmen_cenu(self):
        for predmet in self.predmety:
            zmena = random.randint(-5,5)
            nova_cena = predmet.aktualni_cena + zmena
            if nova_cena < predmet.min_cena:
             nova_cena = predmet.min_cena[predmet]
            elif nova_cena > predmet.max_cena:
                nova_cena = predmet.max_cena
            predmet.aktualni_cena = nova_cena

'''utopenec = Predmet("Utopenec", 50, 100)
med = Predmet("Med", 100, 200)
palava = Predmet("Pálava", 200, 500)

hradcany = Lokace("Hradčany",[
    Predmet("Utopenec", 50, 100),
    Predmet("Med", 100, 200),
    Predmet("Pálava", 200, 500)
    ])

vaclavak = Lokace("Václavák", [
    Predmet("Utopenec", 50, 100),
    Predmet("Med", 100, 200),
    Predmet("Pálava", 200, 500)
    ])

holesovice = Lokace("Holešovice", [
    Predmet("Utopenec", 50, 100),
    Predmet("Med", 100, 200),
    Predmet("Pálava", 200, 500)
    ])


print(hradcany.predmety[0].aktualni_cena)
print(vaclavak.predmety[0].aktualni_cena)
print(holesovice.predmety[0].aktualni_cena)'''
