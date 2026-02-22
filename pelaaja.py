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

    def inv(self):
        if len(self.tavaraluettelo) == 0:
            return "Tavaraluettelossasi ei ole mitään"
        else:
            tavarat = ""
            for tavara in self.tavaraluettelo:
                tavarat += tavara.nimi + "\n"
            return tavarat
        
    def ota(self, kohde, huone):

        nykyinen_paino = 0
        for tavara in self.tavaraluettelo:
            nykyinen_paino += tavara.paino

        for tavara in huone.tavaraluettelo:
            if tavara.nimi.lower() == kohde:

                if nykyinen_paino + tavara.paino > self.kantokyky:
                    return "Et jaksa kantaa enempää tavaraa"

                return tavara.siirra(huone, self)

        return "Sellaista tavaraa ei löytynyt"
    
    def pudota(self, kohde, huone):
        for tavara in self.tavaraluettelo:
            if tavara.nimi.lower() == kohde:
                return tavara.siirra(self, huone)
        return "Sinulla ei ole pudotettavaa"
    
    def lue(self, kohde):
        for tavara in self.tavaraluettelo:
            if tavara.nimi.lower() == kohde:
                return tavara.lue()
        return "Sinulla ei ole sellaista esinettä"
    
    def kerro_paino(self, kohde):
        pass

    def sytyta(self, kohde):
        for tavara in self.tavaraluettelo:
            if tavara.nimi.lower() == kohde:
                return tavara.sytyta(self.tavaraluettelo)
        return "En voi sytyttää sellaista mitä minulla ei ole."
    
    def sammuta(self, kohde):
        for tavara in self.tavaraluettelo:
            if tavara.nimi.lower() == kohde:
                return tavara.sammuta()
        return "En voi sammuttaa sellaista mitä minulla ei ole."
        
    def avaa(self, kohde):    
        for tavara in self.huone.tavaraluettelo:
            if tavara.nimi.lower() == kohde and tavara.nimi.lower() == "ovi":
                if tavara.auki:
                    return "Ovi on jo auki"
                else:
                    tavara.auki = True
                    return "Ovi avautuu narahtaen"
        return "Ei ole mitään avattavaa"

    def sulje(self,kohde):
        for tavara in self.huone.tavaraluettelo:
            if tavara.nimi.lower() == kohde and tavara.nimi.lower() == "ovi":
                if not tavara.auki:
                    return "Ovi on jo kiinni"
                else:
                    tavara.auki = False
                    return "Ovi sulkeutuu narahtaen"
        return "Ei ole mitään suljettavaa"