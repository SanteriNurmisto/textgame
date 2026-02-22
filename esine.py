class Esine():

    # Esineillä, pelaajilla ja huoneilla on relaatio game-olioon
    game = None

    def __init__(self, nimi, paino, huone):
        self.nimi = nimi
        self.paino = paino
        # Kustakin esineestä tiedetään, missä huoneessa se sijaitsee
        self.huone = huone
        self.game = huone.game

    def siirra(self, lahde, kohde):
        lahde.tavaraluettelo.remove(self)
        kohde.tavaraluettelo.append(self)

        # Vaihdetaan esineen huone. Jos esine on siirretty pelaajan inventaarioon, huoneeksi asetetaan None
        if type(kohde).__name__ == "Pelaaja":
            self.huone = None
        else:
            self.huone = kohde

        return "Tehty työtä käskettyä"
    
    def lue(self):
        return "Tätä ei voi lukea"
    
    def sytyta(self, tavaraluettelo=None):
        return "Et voi sytyttää tätä."
    
    def sammuta(self):
        return "Ei ole mitään sammutettavaa."

class Kirja(Esine):
    luettu = False
    def lue(self):
        if self.luettu:
            return "Tämä kirja on taru sormusten herrasta"
        else:
            self.luettu = True
            self.game.pelaaja.huone.tavaraluettelo.append(Muistilappu("Muistilappu", 0, self.game.pelaaja.huone))
            return "Kirjan välistä näyttänee tippuneen joku lappu"
    
class Muistilappu(Esine):
    def lue(self):
        return "PIN-koodi 7752"

class Vasara(Esine):
    pass
    
class Rautakanki(Esine):
    pass

class Tuoli(Esine):
    pass

class Alasin(Esine):
    pass

class Kynttila(Esine):

    palaa = False

    def sytyta(self, tavaraluettelo=None):

        # Palaako jo?
        if self.palaa:
            return "Kynttilä palaa jo, et voi sytyttää sitä uudelleen."

        # Kynttilä voidaan sytyttää, jos pelaajalla on tulitikut.
        for tavara in tavaraluettelo:
            if tavara.nimi == "Tulitikut":
                self.palaa = True
                return "Kynttilä on sytytetty."
            
        return "Ei minulla ole mitään millä sytyttää."
   
    def sammuta(self):

        if self.palaa:
            self.palaa = False
            return "Kynttilä on sammutettu."
        else:
            return "Et voi sammuttaa kynttilää, joka ei pala."

class Tulitikut(Esine):
    pass

class Ovi(Esine):
    
    auki = False

    def siirra(self, kohde, huone):
        return "Ovea ei saa irti"

    def hae_ovi(self):
        if self.auki:
            return self.nimi + " (auki)"
        else:
            return self.nimi + " (kiinni)"