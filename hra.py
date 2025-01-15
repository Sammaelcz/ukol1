from predmet import Predmet
from lokace import Lokace
from osoba import Osoba
# Hlavní program
def main():

    # Predmety
    utopenec = Predmet("Utopenec", 50, 100)
    med = Predmet("Med", 100, 200)
    palava = Predmet("Pálava", 200, 500)
    kabat = Predmet("Kabát", 150, 150)
    batoh = Predmet("Batoh", 400, 400)

    predmety = [utopenec, med, palava, kabat, batoh]
    #predmety_spolecne = [utopenec, med, palava]
    #predmety_vecerka = [kabat, batoh]

    '''Lokace s nastavením cen předmětů
    hradcany = Lokace("Hradčany", predmety_spolecne)
    vaclavak = Lokace("Václavák", predmety_spolecne)
    holesovice = Lokace("Holešovice", predmety_spolecne)
    vecerka = Lokace("Večerka", predmety_vecerka)'''

    # Lokace s predměty s aktuální cenou v {}, aby se listovat přes items()
    hradcany = Lokace("Hradčany",{
                    utopenec.jmeno: utopenec.aktualni_cena,
                    med.jmeno: med.aktualni_cena,
                    palava.jmeno: palava.aktualni_cena})
    vaclavak = Lokace("Václavák",{
                    utopenec.jmeno: utopenec.aktualni_cena,
                    med.jmeno: med.aktualni_cena,
                    palava.jmeno: palava.aktualni_cena})
    holesovice = Lokace("Holešovice",{
                    utopenec.jmeno: utopenec.aktualni_cena,
                    med.jmeno: med.aktualni_cena,
                    palava.jmeno: palava.aktualni_cena})
    vecerka = Lokace("Večerka", {
                    kabat.jmeno: kabat.aktualni_cena,
                    batoh.jmeno: batoh.aktualni_cena,})

    lokace_seznam = [hradcany.jmeno, vaclavak.jmeno, holesovice.jmeno, vecerka.jmeno]

    vecerka.special = True # Lokace.special neprochází funkcí změny cen

    #Začátek - vstupy:
    hrac1 = Osoba(input("Napiš jméno hráče: "),
                  1000, #definuj počáteční hotovost
                  hradcany) # definuj počáteční lokaci

    #Hlavní smyčka:
    konec_hry = 15
    while hrac1.aktualni_den < konec_hry:

        # Vypsání textu
        print(f"Nacházíš se v lokaci: {hrac1.aktualni_lokace.jmeno}")
        print(f"Dny: {hrac1.aktualni_den}, Peníze: {hrac1.hotovost} Kč")
        print("Aktuální ceny předmětů:")
        #hrac1.aktualni_lokace.vypis_predmety()
        for predmet, cena in hrac1.aktualni_lokace.predmety.items():
            print(f"{predmet} {cena}")
        #hrac1.vypis_hotovost()
        print("Inventář:")
        for predmet, mnozstvi in hrac1.inventar.items():
            print(f"{predmet.jmeno} {mnozstvi}")
        #hrac1.vypis_inventar()
        print(f"Napiš číslo, co chceš udělat:")
        print(f"Změnit lokaci: 1")
        print(f"Nakoupit předmět: 2")
        print(f"Prodat předmět: 3")

        # Volba akce
        try:
            volba_akce = int(input("Zvolte akci: "))

            # 1. Změna lokace
            if volba_akce == 1:

                # Vypsání textu
                print(f"Macházíš se v lokaci: {hrac1.aktualni_lokace.jmeno}")
                print("Lokace na výběr:")
                for index, lokace_jmeno in enumerate(lokace_seznam):
                    print(f"{index + 1}. {lokace_jmeno}")
                print("")

                # Volba nové lokace
                    # Tohle řešení je lepší, ale v lokace_volba přijde místo: hradcany - Hradčany, tím pádem
                        # to rozbije Osoba.zmen_lokaci a Lokace.zmen_cenu
                        # dodělat později
                '''lokace_volba = int(input("Napiš číslo lokace, kam se chceš přesunout: ")) - 1
                if 0 <= lokace_volba < len(lokace_seznam):
                    nova_lokace = lokace_seznam[lokace_volba]
                    hrac1.zmen_lokaci(nova_lokace) #

                else:
                    print("Neplatná volba.")'''

                # Volba nové lokace
                lokace_volba = int(input())
                if (lokace_volba == 1
                        and hrac1.aktualni_lokace != hradcany):
                    hrac1.zmen_lokaci(hradcany)
                elif (lokace_volba == 2
                      and hrac1.aktualni_lokace!=vaclavak):
                    print(vaclavak.predmety)
                    print(vaclavak.predmety['Utopenec'])
                    print(vaclavak.predmety.items())
                    #print(vaclavak.predmety[utopenec].aktualni_cena)
                    #print(vaclavak.predmety[utopenec.aktualni_cena])
                    input()
                    hrac1.zmen_lokaci(vaclavak)
                elif (lokace_volba == 3
                      and hrac1.aktualni_lokace!=holesovice):
                    hrac1.zmen_lokaci(holesovice)
                elif (lokace_volba == 4
                      and hrac1.aktualni_lokace!=vecerka):
                    hrac1.zmen_lokaci(vecerka)

            # 2. Koupě předmětu
            elif volba_akce == 2:

                # Vypsání textu

                print("Předměty k nákupu:")
                for index, (predmet, cena) in enumerate(hrac1.aktualni_lokace.predmety.items()):
                    if hrac1.aktualni_lokace == vecerka:
                        print(f"{index + 4}. {predmet.jmeno}: {cena} Kč")
                    else:
                        print(f"{index + 1}. {predmet.jmeno}: {cena} Kč")
                print(f"Máš: {hrac1.hotovost} Kč")
                print("Inventář:")
                for predmet, mnozstvi in hrac1.inventar.items():
                    print(f"{predmet} {mnozstvi}")
                print()

                """hrac1.vypis_hotovost()
                hrac1.vypis_inventar()
                print("")
                hrac1.aktualni_lokace.vypis_predmety_index()
                print("")
                print("Co chceš koupit? Napiš číslo: ")"""


                # Výběr kupovaného předmětu
                vyber_predmet = int(input("Co chceš koupit? Napiš číslo: ")) - 1
                if 0 <= vyber_predmet < len(predmety):
                    predmet = predmety[vyber_predmet]
                    hrac1.koupit_predmet_1(predmet)

                # Verze pro list
                '''print(hrac1.aktualni_lokace.predmety)
                predmet = hrac1.aktualni_lokace.predmety[int(vyber_predmet)-1]
                hrac1.koupit_predmet_1(predmet)'''

                '''if  vyber_predmet == "1":       #tady přijde enumerate a nefunguje kabát, batoh
                    predmet_jmeno = utopenec.jmeno #varianta 1
                    predmet_cena = utopenec.aktualni_cena
                    hrac1.koupit_predmet(predmet_jmeno, predmet_cena)
                    predmet = utopenec
                    hrac1.koupit_predmet_1(predmet)
                    predmet_koupit = False
                elif vyber_predmet == "2":
                    predmet_jmeno = med.jmeno
                    predmet_cena = med.aktualni_cena
                    hrac1.koupit_predmet(predmet_jmeno, predmet_cena)
                    predmet_koupit = False
                elif vyber_predmet == "3":
                    predmet_jmeno = palava.jmeno
                    predmet_cena = palava.aktualni_cena
                    hrac1.koupit_predmet(predmet_jmeno, predmet_cena)
                    predmet_koupit = False
                elif vyber_predmet == "":
                    predmet_koupit = False##
                else:
                    neplatna_volba()'''

            # 3. Prodej předmětu
            elif volba_akce == 3:

                # Vypsání textu

                print("Aktuální ceny předmětů:")
                hrac1.aktualni_lokace.vypis_predmety() #vypsat pouze ty, které jsou v inventáři
                print("")
                hrac1.vypis_inventar() # nutno vypsat indexy pod kterými prodávat
                print("")
                print("Co chceš prodat? Napiš číslo: ")

                # Výběr prodávaného předmětu
                print("Předměty k prodeji:")
                for i, (predmet, mnozstvi) in enumerate(hrac1.inventar.items()):
                    if mnozstvi > 0:
                        print(f"{i + 1}. {predmet}: {mnozstvi} ks (Cena: {hrac1.aktualni_lokace.predmety.aktualni_cena} Kč)")
                vyber_predmet = input()
                    # Nepoužiji int(). Program by skočil do ValueError místo neplatné volby.
                predmet = hrac1.aktualni_lokace.predmety[int(vyber_predmet)-1]
                print(predmet)
                hrac1.koupit_predmet_1(predmet)
                predmet_koupit = False
                '''vyber_predmet = input()
                    # Nepoužiji int(). Program by skočil do ValueError místo neplatné volby.
                if  vyber_predmet == "1": #tady přijde enumerate
                    predmet_prodat = False
                elif vyber_predmet == "":
                    predmet_prodat = False
                else:
                    neplatna_volba()'''

        except ValueError:
            print("Neplatný vstup. Zadejte číslo.")

    print(f"Konec hry. Máš {hrac1.hotovost}, jsi hotový boháč!")

main()
