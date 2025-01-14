from predmet import Predmet
from lokace import Lokace
from osoba import Osoba

# Funkce
def neplatna_volba():
    print("\n!!!!!! ______ Neplatná volba ______ !!!!!!", end="\n\n")

def vypis_lokaci(aktualni_lokace):
    print(f"Macházíš se v lokaci: {aktualni_lokace}\n"
          f"Napiš číslo lokace, kam se chceš přesunout:\n"
          f"1 - Hradčany\n"
          f"2 - Václavák\n"
          f"3 - Holešovice")

def vypis_akci():
    print(f"Napiš číslo, co chceš udělat: \n"
          f"Změnit lokaci: 1\n"
          f"Nakoupit předmět: 2\n"
          f"Prodat předmět: 3")

# Hlavní program
def main():

    # Predmety
    utopenec = Predmet("Utopenec", 50, 100)
    med = Predmet("Med", 100, 200)
    palava = Predmet("Pálava", 200, 500)

    # Lokace s nastavením cen předmětů
    hradcany = Lokace("Hradčany",[
        Predmet("Utopenec", 50, 100),
        Predmet("Med", 100, 200),
        Predmet("Láhev Pálavy", 200, 500)
    ])
    vaclavak = Lokace("Václavák", [
        Predmet("Utopenec", 50, 100),
        Predmet("Med", 100, 200),
        Predmet("Láhev Pálavy", 200, 500)
    ])
    holesovice = Lokace("Holešovice", [
        Predmet("Utopenec", 50, 100),
        Predmet("Med", 100, 200),
        Predmet("Láhev Pálavy", 200, 500)
    ])

    #Začátek - vstupy:
    hrac1 = Osoba(input("Napiš jméno hráče: "),
                  100, #definuj počáteční hotovost
                  hradcany) # definuj počáteční lokaci

    #Hlavní smyčka:
    konec_hry = 15

    print("\nHra začíná", end="\n\n")
    while hrac1.aktualni_den < konec_hry:

        #Začátek
        print(f"Je den {hrac1.aktualni_den}.\n")

        # Vypsání předmětů
        print(f"Nacházíš se v lokaci: {hrac1.aktualni_lokace.jmeno}\n"
                f"Aktuální ceny předmětů:")
        hrac1.aktualni_lokace.vypis_predmety()
        print("")
        hrac1.vypis_hotovost()
        hrac1.vypis_inventar()
        print("")

        #Proměnné akce:
        lokace_zmena = False
        predmet_koupit = False
        predmet_prodat = False

        #Volba akce:
        while (lokace_zmena == False
               and predmet_koupit == False
               and predmet_prodat == False):
            vypis_akci()
            volba_akce = input("")
            if volba_akce == "1":
                lokace_zmena = True
            elif volba_akce == "2":
                predmet_koupit = True
            elif volba_akce == "3":
                predmet_prodat = True
            else:
                neplatna_volba()

        # 1. Změna lokace
        while lokace_zmena == True:
            vypis_lokaci(hrac1.aktualni_lokace.jmeno)
            lokace_volba = input("")
            if (lokace_volba == "1"
                    and hrac1.aktualni_lokace != hradcany):
                hrac1.zmen_lokaci(hradcany)
                lokace_zmena = False
            elif (lokace_volba == "2"
                  and hrac1.aktualni_lokace!=vaclavak):
                hrac1.zmen_lokaci(vaclavak)
                lokace_zmena = False
            elif (lokace_volba == "3"
                  and hrac1.aktualni_lokace!=holesovice):
                hrac1.zmen_lokaci(holesovice)
                lokace_zmena = False
            else:
                neplatna_volba()

        #2. Koupení předmětu
        while predmet_koupit == True:
            hrac1.vypis_hotovost()
            hrac1.vypis_inventar()
            print("")
            hrac1.aktualni_lokace.vypis_predmety_index()
            print("")

            napis_predmet = input("Co chceš koupit? Napiš číslo:")
            if  napis_predmet == "1":
                predmet_jmeno = utopenec.jmeno
                hrac1.koupit_predmet(predmet_jmeno)
                predmet_koupit = False
            elif napis_predmet == "2":
                predmet_jmeno = med.jmeno
                hrac1.koupit_predmet(predmet_jmeno)
                predmet_koupit = False
            elif napis_predmet == "3":
                predmet_jmeno = palava.jmeno
                hrac1.koupit_predmet(predmet_jmeno)
                predmet_koupit = False
            else:
                neplatna_volba()


    print(f"Konec hry. Máš {hrac1.hotovost}, jsi hotový boháč!")

main()










'''
    print()
    print(vaclavak.predmety[0].aktualni_cena)
    print(holesovice.predmety[0].aktualni_cena)
    print(hrac1.aktualni_lokace)

    hrac1.aktualni_lokace = vaclavak.jmeno #zmena lokace

    print(hrac1.aktualni_lokace)
'''