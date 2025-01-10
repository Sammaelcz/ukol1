from asyncio import all_tasks


class Osoba:
    def __init__(self, hotovost, aktualni_lokace):
        self.hotovost = hotovost
        self.aktualni_lokace = aktualni_lokace
        self.kupene_predmety = {}

    def zmen_lokaci(self, nova_lokace):
        print(f"Nacházíš se v: {self.aktualni_lokace.jmeno}")
        self.aktualni_lokace = nova_lokace
        print(f"Přesunul si se do: {self.aktualni_lokace.jmeno}")


