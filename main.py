import lokace
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

    print("\nHra začíná", end="\n\n")
    while aktualni_den < konec_hry:
        #Začátek
        print(f"Je den {aktualni_den}.\n")

        '''# Vypsání předmětů
        print(f"Nacházíš se v lokaci: {osoba.aktualni_lokace.jmeno}\n"
                  f"Aktuální ceny předmětů:")
        if osoba.aktualni_lokace == hradcany:
            hradcany.vypis_predmety()
        elif osoba.aktualni_lokace == vaclavak:
            vaclavak.vypis_predmety()
        elif osoba.aktualni_lokace == holesovice:
            holesovice.vypis_predmety()
        else:
            print("předměty se nezobrazují")'''

        # Vypsání předmětů
        print(f"Nacházíš se v lokaci: {osoba.aktualni_lokace.jmeno}\n"
                f"Aktuální ceny předmětů:")
        osoba.aktualni_lokace.vypis_predmety()
        print(f"\nV portmonce máš: {osoba.hotovost},- Kč\n"
              f"V inventáří máš {osoba.inventar}\n")

        #Proměnné akce:
        lokace_zmena = False
        predmet_koupit = False
        predmet_prodat = False

        #Volba akce:
        while (lokace_zmena == False
               and predmet_koupit == False
               and predmet_prodat == False):
            print(f"Napiš číslo, co chceš udělat: \n"
                  f"Změnit lokaci: 1\n"
                  f"Nakoupit předmět: 2\n"
                  f"Prodat předmět: 3")
            volba_akce = input("")
            if volba_akce == "1":
                lokace_zmena = True
            elif volba_akce == "2":
                predmet_koupit = True
            elif volba_akce == "3":
                predmet_prodat = True
            else:
                print("\n!!!!!! ______ Neplatná volba ______ !!!!!!", end="\n\n")

        # 1. Změna lokace
        while lokace_zmena == True:
            print(f"Macházíš se v lokaci: {osoba.aktualni_lokace.jmeno}\n"
                  f"Napiš číslo lokace, kam se chceš přesunout:\n"
                  f"1 - Hradčany\n"
                  f"2 - Václavák\n"
                  f"3 - Holešovice")
            lokace_volba = input("")
            if (lokace_volba == "1"
                    and osoba.aktualni_lokace != hradcany):
                osoba.zmen_lokaci(hradcany)
                #osoba.aktualni_lokace.vypis_predmety()
                hradcany.zmen_ceny()
                #osoba.aktualni_lokace.vypis_predmety()
                lokace_zmena = False
            elif (lokace_volba == "2"
                  and osoba.aktualni_lokace!=vaclavak):
                osoba.zmen_lokaci(vaclavak)
                vaclavak.zmen_ceny()
                lokace_zmena = False
            elif (lokace_volba == "3"
                  and osoba.aktualni_lokace!=holesovice):
                osoba.zmen_lokaci(holesovice)
                holesovice.zmen_ceny()
                lokace_zmena = False
            else:
                print("\n!!!!!! ______ Neplatná volba ______ !!!!!!", end="\n\n")

        #2. Koupení předmětu
        while predmet_koupit == True:
            print(f"Aktuálně nabízené předměty:")
            osoba.aktualni_lokace.vypis_predmety_index()
            print(f"\nV portmonce máš: {osoba.hotovost},- Kč\n"
                  f"V inventáří máš {osoba.inventar}\n")
            predmet_jmeno = input("Co chceš koupit? Napiš číslo:")
            predmet_jmeno_valid = False
            while predmet_jmeno_valid == False:
                if predmet_jmeno == "1":
                    predmet_jmeno = utopenec.jmeno
                    predmet_jmeno_valid = True
                elif predmet_jmeno == "2":
                    predmet_jmeno = med.jmeno
                    predmet_jmeno_valid = True
                elif predmet_jmeno == "3":
                    predmet_jmeno = palava.jmeno
                    predmet_jmeno_valid = True
                else:
                    print("\n!!!!!! ______ Neplatná volba ______ !!!!!!", end="\n\n")

            predmet_mnozstvi = int(input("Napiš množství:"))
            osoba.koupit_predmet(predmet_jmeno, predmet_mnozstvi)

        input("enter pro další den")
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