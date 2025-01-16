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
        if self.special == False: #stejný jako napsat: if not self.special:
            for klic in self.predmety: #self.predmety je slovnik {utopenec: 80, med: 150, palava: 450} a probíhá iterace přes klíče
                zmena = random.randint(-5,5)
                nova_cena = self.predmety[klic] + zmena #self.predmety[klic] je hodnota toho klíče např. utopence takže cena 80
                '''print(self.predmety)
                print(self.predmety[klic])
                print(nova_cena)
                print(klic)
                input()'''
                if nova_cena < klic.min_cena:
                 nova_cena = klic.min_cena[klic.aktualni_cena]
                elif nova_cena > klic.max_cena:
                    nova_cena = klic.max_cena
                self.predmety[klic] = nova_cena
                """self.predmety[klic] = max(x.min_cena, min(x.max_cena, nova_cena))"""
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