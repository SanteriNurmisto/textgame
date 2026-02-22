import huone
from pelaaja import Pelaaja
import esine

class Game:

    huoneet = []
    pelaaja = None

    def __init__(self):
        self.huoneet.append(huone.Kellarivarasto(self, "Kellarivarasto"))
        self.pelaaja = Pelaaja(self, "Jaska", 10, self.huoneet[0])

    def parseri(self, syote):
        syote = syote.strip()
        sanat = syote.split(" ", maxsplit=1)
        if len(sanat) > 1:
            return sanat[0].lower(), sanat[1].lower()
        else:
            return syote.lower(), None

game = Game()

while True:
    syote = input("Mitä haluaisit tehdä? ")
    komento, kohde = game.parseri(syote)
    if komento == "exit":
        break
    elif komento == "ota":
        print(game.pelaaja.ota(kohde))   
    elif komento == "pudota":
        print(game.pelaaja.pudota(kohde))
    elif komento == "katso":
        print(game.pelaaja.huone.katso())
    elif komento == "inv":
        print(game.pelaaja.inv())
    elif komento == "lue":
        print(game.pelaaja.lue(kohde))
    elif komento == "sytytä":
        print(game.pelaaja.sytyta(kohde))
    elif komento == "sammuta":
        print(game.pelaaja.sammuta(kohde))
    elif komento == "avaa":
        print(game.pelaaja.avaa(kohde))
    elif komento == "sulje":
        print(game.pelaaja.sulje(kohde))
    else:
        print("En ymmärrä mitä haluat tehdä")