from predmet import Predmet
from lokace import Lokace

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

