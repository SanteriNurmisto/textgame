from random import randint

class Pelaaja:

    # Esineillä, pelaajilla ja huoneilla on relaatio game-olioon
    game = None

    tavaraluettelo = []
    huone = None

    def __init__(self, game, nimi, kantokyky, huone):
        self.nimi = nimi
        self.kantokyky = kantokyky
        self.huone = huone
        self.game = game
        self.oven_pin = str(randint(0,8999) + 1000)

    def inv(self):
        if len(self.tavaraluettelo) == 0:
            return "Tavaraluettelossasi ei ole mitään"
        else:
            tavarat = ""
            for tavara in self.tavaraluettelo:
                tavarat += tavara.pitka_nimi + "\n"
            return tavarat
        
    def ota(self, kohde):

        nykyinen_paino = 0
        for tavara in self.tavaraluettelo:
            nykyinen_paino += tavara.paino

        for tavara in self.huone.tavaraluettelo:
            if tavara.nimi.lower() == kohde:

                if tavara.paino == None:
                    return "Et voi poimia kyseistä tavaraa"

                if nykyinen_paino + tavara.paino > self.kantokyky:
                    return "Et jaksa kantaa enempää tavaraa"

                return tavara.siirra(self.huone, self)

        return "Sellaista tavaraa ei löytynyt"
    
    def pudota(self, kohde):
        for tavara in self.tavaraluettelo:
            if tavara.nimi.lower() == kohde:
                return tavara.siirra(self, self.huone)
        return "Sinulla ei ole pudotettavaa"
    
    def lue(self, kohde):
        for tavara in self.tavaraluettelo:
            if tavara.nimi.lower() == kohde:
                # Kuka lukee? Pelaaja (self) lukee.
                return tavara.lue(self)
        return "Sinulla ei ole sellaista esinettä"
    
    def kerro_paino(self, kohde):
        pass

    def sytyta(self, kohde):
        tavarat = self.tavaraluettelo + self.huone.tavaraluettelo
        for tavara in tavarat:
            if tavara.nimi.lower() == kohde and tavara.sytytettavissa:
                return tavara.sytyta(self.tavaraluettelo)
        return "Ei onnistu"
    
    def sammuta(self, kohde):
        for tavara in self.tavaraluettelo:
            if tavara.nimi.lower() == kohde:
                return tavara.sammuta()
        return "Ei onnistu"
        
    def avaa(self, kohde):    
        for tavara in self.huone.tavaraluettelo:
            if tavara.nimi.lower() == kohde:
                return tavara.avaa()
        return "Ei ole mitään avattavaa"

    def sulje(self,kohde):
        for tavara in self.huone.tavaraluettelo:
            if tavara.nimi.lower() == kohde:
                return tavara.sulje()
        return "Ei ole mitään suljettavaa"
    def tao(self, kohde):
        pass

    def kuumenna(self, kohde):
        for tavara in self.tavaraluettelo:
            if tavara.nimi.lower() == kohde:
                return tavara.kuumenna()
        return "Tavaraa ei voi kuumentaa"
    