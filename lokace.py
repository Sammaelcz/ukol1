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
        print("Aktuálně nabízené předměty:")
        for polozka in self.predmety:
            print(f"{vypis_predmety_index} - {polozka.jmeno} {polozka.aktualni_cena},- Kč")
            vypis_predmety_index += 1

    def zmen_cenu(self):
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
            pass
