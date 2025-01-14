class Osoba:
    def __init__(self, jmeno, hotovost, aktualni_lokace):
        self.jmeno = jmeno
        self.hotovost = hotovost
        self.aktualni_lokace = aktualni_lokace
        self.aktualni_den = 1
        self.inventar = {}

    def zmen_lokaci(self, nova_lokace):
        self.aktualni_lokace = nova_lokace
        self.aktualni_den += 1
        nova_lokace.zmen_cenu()
        print(f"Přesunul si se do: {self.aktualni_lokace.jmeno}", end="\n\n")

    def vypis_hotovost(self):
        print(f"V portmonce máš: {self.hotovost},- Kč")

    def vypis_inventar(self):
        print("V inventáří máš:")
        for predmet, mnozstvi in self.inventar.items(): #items == py funkce
            print(f"- {predmet}: {mnozstvi} ks")

    def koupit_predmet(self, predmet_jmeno):
        if predmet_jmeno in self.inventar:
            self.inventar[predmet_jmeno] += 1
        else:
            self.inventar[predmet_jmeno] = 1
