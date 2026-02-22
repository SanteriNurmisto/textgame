import esine

class Huone:

    # Esineillä, pelaajilla ja huoneilla on relaatio game-olioon
    game = None

    def __init__(self, game, kuvaus):
        self.tavaraluettelo = []
        self.game = game
        self.kuvaus = kuvaus

    def katso(self):
        tavarat = ""
        for tavara in self.tavaraluettelo:
            tavarat += tavara.pitka_nimi + "\n"
        return self.kuvaus+ ".\nSisältää seuraavat tavarat: \n" + tavarat

class Kellarivarasto(Huone):
    def __init__(self, game, kuvaus):
        super().__init__(game, kuvaus)
        self.tavaraluettelo.append(esine.Kirja(self, "Kirja", "Kovakantinen kirja", 1))
        self.tavaraluettelo.append(esine.Vasara(self, "Vasara", "", 3))
        self.tavaraluettelo.append(esine.Rautakanki(self, "Rautakanki", "Ruosteinen rautakanki", 5))
        self.tavaraluettelo.append(esine.Tuoli(self, "Tuoli", "", 7))
        self.tavaraluettelo.append(esine.Alasin(self, "Alasin", "", 9))
        self.tavaraluettelo.append(esine.Ovi(self, "Ovi", "Ovi pohjoiseen (kiinni)", None))
        self.tavaraluettelo.append(esine.Kynttila(self, "Kynttilä", "", 0.1))
        self.tavaraluettelo.append(esine.Tulitikut(self, "Tulitikut", "", 0.01))