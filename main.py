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

    osoba = Osoba(100, hradcany.jmeno)
'''
    print()
    print(vaclavak.predmety[0].aktualni_cena)
    print(holesovice.predmety[0].aktualni_cena)
    print(osoba.aktualni_lokace)

    osoba.aktualni_lokace = vaclavak.jmeno #zmena lokace

    print(osoba.aktualni_lokace)
'''

main()

