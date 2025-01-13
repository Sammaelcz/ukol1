from lokace import Lokace

class Osoba:
    def __init__(self, hotovost, aktualni_lokace):
        self.hotovost = hotovost
        self.aktualni_lokace = aktualni_lokace
        self.inventar = {}

    def zmen_lokaci(self, nova_lokace):
#        print(f"Nacházíš se v: {self.aktualni_lokace.jmeno}")
        self.aktualni_lokace = nova_lokace
        print(f"Přesunul si se do: {self.aktualni_lokace.jmeno}")

    def koupit_predmet(self, predmet_jmeno, predmet_mnozstvi = 1):
        self.inventar[predmet_jmeno] = predmet_mnozstvi
        print(f"{self.inventar} print funkce")
'''
hero = Osoba(100, "tu")
hero.koupit_predmet("med", 2)
print(f"{hero.inventar}print tělo")
'''