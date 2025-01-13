from predmet import Predmet

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
        for polozka in self.predmety:
            print(f"{vypis_predmety_index} - {polozka.jmeno} {polozka.aktualni_cena},- Kč")
            vypis_predmety_index += 1

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
