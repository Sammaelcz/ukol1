from predmet import Predmet
from lokace import Lokace
from osoba import Osoba

# Funkce

def intro_print():
    print("")
    print("Hra začíná!")
    print("")

def neplatna_volba():
    print("")
    print("Neplatná volba!")
    input(".. pro pokračování zmáčkni 'Enter'")
    print("")

def potvrd_akci():
    input(".. pro pokračování zmáčkni 'Enter'")
    print("")

# Hlavní program
def main():

    # Predmety
    utopenec = Predmet("Utopenec", 50, 100)
    med = Predmet("Med", 100, 200)
    palava = Predmet("Pálava", 200, 500)
    kabat = Predmet("Kabát", 150, 150)
    batoh = Predmet("Batoh", 400, 400)
    predmety_spolecne = [utopenec, med, palava]
    predmety_vecerka = [kabat, batoh]

    # Lokace s nastavením cen předmětů
    hradcany = Lokace("Hradčany", predmety_spolecne)
    vaclavak = Lokace("Václavák", predmety_spolecne)
    holesovice = Lokace("Holešovice", predmety_spolecne)
    vecerka = Lokace("Večerka", predmety_vecerka)
    vecerka.special = True # Lokace.special neprochází funkcí změny cen

    #Začátek - vstupy:
    hrac1 = Osoba(input("Napiš jméno hráče: "),
                  100, #definuj počáteční hotovost
                  hradcany) # definuj počáteční lokaci

    #Hlavní smyčka:
    konec_hry = 15

    #Vypsání intra
    intro_print()
    while hrac1.aktualni_den < konec_hry:

        #Proměnné akce:
        lokace_zmena = False
        predmet_koupit = False
        predmet_prodat = False

        #Cyklus akce:
        while (lokace_zmena == False
            and predmet_koupit == False
            and predmet_prodat == False):

            # Vypsání textu
            print(f"Je den {hrac1.aktualni_den}.\n")
            print(f"Nacházíš se v lokaci: {hrac1.aktualni_lokace.jmeno}\n"
                  f"Aktuální ceny předmětů:")
            hrac1.aktualni_lokace.vypis_predmety()
            print("")
            hrac1.vypis_hotovost()
            hrac1.vypis_inventar()
            print("")
            print(f"Napiš číslo, co chceš udělat:")
            print(f"Změnit lokaci: 1")
            print(f"Nakoupit předmět: 2")
            print(f"Prodat předmět: 3")

            # Volba akce
            volba_akce = (input(""))
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

            # Vypsání textu
            print(f"Macházíš se v lokaci: {hrac1.aktualni_lokace.jmeno}")
            print("Seznam lokací:")
            print("1 - Hradčany")
            print("2 - Václavák")
            print("3 - Holešovice")
            print("4 - Večerka")
            print("5 - Chci zpět do předchozího menu")
            print("")
            print("Napiš číslo lokace, kam se chceš přesunout:")

            # Volba nové lokace
            lokace_volba = input("")
                # Nepoužiji int(). Program by skočil do ValueError místo neplatné volby.
            if (lokace_volba == "1"
                    and hrac1.aktualni_lokace != hradcany):
                hrac1.zmen_lokaci(hradcany)
                potvrd_akci()
                lokace_zmena = False
            elif (lokace_volba == "2"
                  and hrac1.aktualni_lokace!=vaclavak):
                hrac1.zmen_lokaci(vaclavak)
                potvrd_akci()
                lokace_zmena = False
            elif (lokace_volba == "3"
                  and hrac1.aktualni_lokace!=holesovice):
                hrac1.zmen_lokaci(holesovice)
                potvrd_akci()
                lokace_zmena = False
            elif (lokace_volba == "4"
                  and hrac1.aktualni_lokace!=vecerka):
                hrac1.zmen_lokaci(vecerka)
                potvrd_akci()
                lokace_zmena = False
            elif lokace_volba == "5":
                lokace_zmena = False
            else:
                neplatna_volba()

        #2. Koupě předmětu
        while predmet_koupit == True:

            # Vypsání textu
            hrac1.vypis_hotovost()
            hrac1.vypis_inventar()
            print("")
            hrac1.aktualni_lokace.vypis_predmety_index()
            print("Pro zrušení nakupování napiš: 4")
            print("")

            # Výběr kupovaného předmětu
            vyber_predmet = input("Co chceš koupit? Napiš číslo: ")
                # Nepoužiji int(). Program by skočil do ValueError místo neplatné volby.
            if  vyber_predmet == "1":
                predmet_jmeno = utopenec.jmeno
                predmet_cena = utopenec.aktualni_cena
                hrac1.koupit_predmet(predmet_jmeno, predmet_cena)
                predmet_koupit = False
            elif vyber_predmet == "2":
                predmet_jmeno = med.jmeno
                hrac1.koupit_predmet(predmet_jmeno)
                predmet_koupit = False
            elif vyber_predmet == "3":
                predmet_jmeno = palava.jmeno
                hrac1.koupit_predmet(predmet_jmeno)
                predmet_koupit = False
            elif vyber_predmet == "4":
                predmet_koupit = False
            else:
                neplatna_volba()

    print(f"Konec hry. Máš {hrac1.hotovost}, jsi hotový boháč!")

main()
