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

    '''def koupit_predmet(self, predmet_jmeno, predmet_cena):
        if self.hotovost >= predmet_cena:
            self.hotovost -= predmet_cena
            if predmet_jmeno in self.inventar:
                self.inventar[predmet_jmeno] += 1
            else:
                self.inventar[predmet_jmeno] = 1
        else:
            print("\nNemáš dost peněz!")
            input("... pro pokračování zmáčkni 'Enter'\n")'''


    def koupit_predmet_1(self, predmet):
        print(f"{predmet}") # {Utopenec 50 100 72: 59, Med 100 200 142: 136, Pálava 200 500 377: 481}
        print(f"{predmet.values()}") # dict_values([59, 136, 481])
        print(f"{list(predmet.values())}") # [59, 136, 481]
        input() #vyextrahovat hodnotu ze slovniku
        if predmet.aktualni_cena > self.hotovost: #AttributeError: 'dict' object has no attribute 'aktualni_cena'
        #if predmet > self.hotovost: #TypeError: '>' not supported between instances of 'dict' and 'int'


            print(f"Nemáš dost peněz. Předmět stojí {predmet.aktualni_cena}, ale ty máš jen {self.hotovost}")
            return

        self.hotovost -= predmet.aktualni_cena
        self.inventar[predmet.jmeno] = self.inventar.get(predmet.jmeno, 0) + 1


        print(f"{predmet}")
        print(f"Koupil jsi 1x {predmet.jmeno} za {predmet} Kč.")
        print(f"Zbývá ti v portmonce {self.hotovost}")


    def prodat_predmet(self, predmet_jmeno, cena):

        if predmet_jmeno in self.inventar and self.inventar[predmet_jmeno] > 0:
            self.inventar[predmet_jmeno] -= 1
            self.hotovost += cena
            print(f"Prodal jsi 1x {predmet_jmeno} za {cena} Kč.")
            print(f"Máš v portmonce {self.hotovost}")

            if self.inventar[predmet_jmeno] == 0:
                del self.inventar[predmet_jmeno]

        else:
            print(f"\nNemáš předmět {predmet_jmeno} v inventáři")






