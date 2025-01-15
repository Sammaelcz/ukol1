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

    predmety_spolecne = [utopenec, med, palava]
    predmety_vecerka = [kabat, batoh]

    '''Lokace s nastavením cen předmětů
    hradcany = Lokace("Hradčany", predmety_spolecne)
    vaclavak = Lokace("Václavák", predmety_spolecne)
    holesovice = Lokace("Holešovice", predmety_spolecne)
    vecerka = Lokace("Večerka", predmety_vecerka)'''

    # Lokace s predměty s aktuální cenou v {}, aby se listovat přes items()
    hradcany = Lokace("Hradčany",{
                    utopenec: utopenec.aktualni_cena,
                    med: med.aktualni_cena,
                    palava: palava.aktualni_cena})
    vaclavak = Lokace("Václavák",{
                    utopenec: utopenec.aktualni_cena,
                    med: med.aktualni_cena,
                    palava: palava.aktualni_cena})
    holesovice = Lokace("Holešovice",{
                    utopenec: utopenec.aktualni_cena,
                    med: med.aktualni_cena,
                    palava: palava.aktualni_cena})
    vecerka = Lokace("Večerka", {
                    kabat: kabat.aktualni_cena,
                    batoh: batoh.aktualni_cena,})

    vecerka.special = True # Lokace.special neprochází funkcí změny cen

    #Začátek - vstupy:
    hrac1 = Osoba(input("Napiš jméno hráče: "),
                  100, #definuj počáteční hotovost
                  hradcany) # definuj počáteční lokaci

    #Hlavní smyčka:
    konec_hry = 15
    while hrac1.aktualni_den < konec_hry:

        # Vypsání textu
        print(f"Je den {hrac1.aktualni_den}.")
        print(f"Nacházíš se v lokaci: {hrac1.aktualni_lokace.jmeno}")
        print("Aktuální ceny předmětů:")
        #hrac1.aktualni_lokace.vypis_predmety()
        for predmet, cena in hrac1.aktualni_lokace.predmety.items():
            print(f"{predmet.jmeno} {cena}")
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
                print("Seznam lokací:")
                print("1 - Hradčany")
                print("2 - Václavák")
                print("3 - Holešovice")
                print("4 - Večerka")
                print("")
                print("Napiš číslo lokace, kam se chceš přesunout:")

                # Volba nové lokace
                lokace_volba = int(input())
                if (lokace_volba == 1
                        and hrac1.aktualni_lokace != hradcany):
                    hrac1.zmen_lokaci(hradcany)
                elif (lokace_volba == 2
                      and hrac1.aktualni_lokace!=vaclavak):
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
                hrac1.vypis_hotovost()
                hrac1.vypis_inventar()
                print("")
                hrac1.aktualni_lokace.vypis_predmety_index()
                print("")
                print("Co chceš koupit? Napiš číslo: ")

                # Výběr kupovaného předmětu
                vyber_predmet = input()
                    # Nepoužiji int(). Program by skočil do ValueError místo neplatné volby.
                predmet = hrac1.aktualni_lokace.predmety[int(vyber_predmet)-1]
                print(predmet)
                hrac1.koupit_predmet_1(predmet)
                predmet_koupit = False
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
