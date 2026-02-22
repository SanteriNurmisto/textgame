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
            if tavara.nimi.lower() == "ovi":
                tavarat += tavara.hae_ovi() + "\n"
            else:
                tavarat += tavara.nimi + "\n"

        return self.kuvaus+ ".\nSisältää seuraavat tavarat: \n" + tavarat

class Kellarivarasto(Huone):
    def __init__(self, game, kuvaus):
        super().__init__(game, kuvaus)
        self.tavaraluettelo.append(esine.Kirja("Kirja", 1, self))
        self.tavaraluettelo.append(esine.Vasara("Vasara", 3, self))
        self.tavaraluettelo.append(esine.Rautakanki("Rautakanki", 5, self))
        self.tavaraluettelo.append(esine.Tuoli("Tuoli", 7, self))
        self.tavaraluettelo.append(esine.Alasin("Alasin", 9, self))
        self.tavaraluettelo.append(esine.Ovi("Ovi", None, self))
        self.tavaraluettelo.append(esine.Kynttila("Kynttilä", 0.1, self))
        self.tavaraluettelo.append(esine.Tulitikut("Tulitikut", 0.01, self))