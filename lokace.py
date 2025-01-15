import random

class Lokace:
    def __init__(self, jmeno, predmety):
        self.jmeno = jmeno
        self.predmety = predmety
        self.special = False # atribut special neprochází zmen_cenu(self)

    def __repr__(self):
        return f"{self.jmeno} {self.predmety}"

    def vypis_predmety(self):
        for polozka in self.predmety:
            print(f"{polozka.jmeno} {polozka.aktualni_cena},- Kč")

    def vypis_predmety_index(self):
        vypis_predmety_index = 1
        print("Aktuální ceny předmětů:")
        for polozka in self.predmety:
            print(f"{vypis_predmety_index} - {polozka.jmeno} {polozka.aktualni_cena},- Kč")
            vypis_predmety_index += 1

    '''def zmen_cenu(self):
        for x in self.predmety:
            zmena = random.randint(-5, 5)
            nova_cena = self.predmety[x] + zmena
            self.predmety[x] = max(x.min_cena, min(x.max_cena, nova_cena))'''

    def zmen_cenu(self):
        if self.special == False:
            for x in self.predmety.values():
                zmena = random.randint(-5,5)
                nova_cena = self.predmety[x] + zmena
                if nova_cena < x.min_cena:
                 nova_cena = x.min_cena[x.aktualni_cena]
                elif nova_cena > x.max_cena:
                    nova_cena = x.max_cena
                self.predmety[x] = nova_cena
        else:
            pass

    '''def zmen_cenu(self):
        if self.special == False:
            for predmet in self.predmety:
                zmena = random.randint(-5,5)
                nova_cena = predmet.aktualni_cena + zmena
                if nova_cena < predmet.min_cena:
                 nova_cena = predmet.min_cena[predmet]
                elif nova_cena > predmet.max_cena:
                    nova_cena = predmet.max_cena
                predmet.aktualni_cena = nova_cena
        else:
            pass'''
##