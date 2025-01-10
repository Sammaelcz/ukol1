from predmet import Predmet
from lokace import Lokace
from osoba import Osoba

def main():

    utopenec = Predmet("Utopenec", 50, 100)
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

    #Začátek - vstupy:
    osoba = Osoba(100, hradcany)

    #Hlavní smyčka:
    aktualni_den = 1
    konec_hry = 15

    while aktualni_den < konec_hry:
        print(f"Je den {aktualni_den}.")
        print(f"V portmonce máš: {osoba.hotovost},- Kč")
        print(f"Nacházíš se v lokaci: {osoba.aktualni_lokace.jmeno}")
        print("Dostupné lokace:")
        print("1 - Hradčany")
        print("2 - Václavák")
        print("3 - Holešovice")
        volba = input("Zadej číslo lokace: ")
        if volba == "1":
            osoba.zmen_lokaci(hradcany)
        elif volba == "2":
            osoba.zmen_lokaci(vaclavak)
        elif volba == "3":
            osoba.zmen_lokaci(holesovice)
        else:
            print("Neplatná volba")
            continue
   #     Co chceš dělat?
    #    Přesun lokace
        input()
        aktualni_den += 1

    print(f"Konec hry. Máš {osoba.hotovost}, jsi hotový boháč!")
main()










'''
    print()
    print(vaclavak.predmety[0].aktualni_cena)
    print(holesovice.predmety[0].aktualni_cena)
    print(osoba.aktualni_lokace)

    osoba.aktualni_lokace = vaclavak.jmeno #zmena lokace

    print(osoba.aktualni_lokace)
'''