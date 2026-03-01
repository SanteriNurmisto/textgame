from pelaaja import Pelaaja


class Esine():

    # Esineillä, pelaajilla ja huoneilla on relaatio game-olioon
    game = None

    def __init__(self, huone, nimi, pitka_nimi="", paino=0):
        self.nimi = nimi
        self.sytytettavissa = False
        self.kuuma = False
        self.pitka_nimi = pitka_nimi or self.nimi
        self.paino = paino
        # Kustakin esineestä tiedetään, missä huoneessa se sijaitsee
        self.huone = huone
        self.game = huone.game

    def siirra(self, lahde, kohde):
        lahde.tavaraluettelo.remove(self)
        kohde.tavaraluettelo.append(self)

        # Vaihdetaan esineen huone. Jos esine on siirretty pelaajan inventaarioon, huoneeksi asetetaan None
        if isinstance(kohde, Pelaaja):
            self.huone = None
        else:
            self.huone = kohde

        return "Tehty työtä käskettyä"
    
    def lue(self, pelaaja):
        return "Tätä ei voi lukea"
    
    def sytyta(self, tavaraluettelo=None):
        return "Et voi sytyttää tätä."
    
    def sammuta(self):
        return "Ei ole mitään sammutettavaa."
    
    def avaa(self):
        return "En tiedä mitä tarkoitat kun pitäisi avata "+self.name+"."

    def sulje(self):
        return "En tiedä mitä tarkoitat kun pitäisi sulkea "+self.name+"."

class Kirja(Esine):
    luettu = False
    def lue(self, pelaaja):
        if self.luettu:
            return "Tämä kirja on Taru Sormusten Herrasta"
        else:
            self.luettu = True
            pelaaja.huone.tavaraluettelo.append(Muistilappu(self, "Muistilappu", "Post-It muistilappu", 0))
            return "Tämä kirja on Taru Sormusten Herrasta. Kirjaa lueskellessani sen välistä putosi lattialle muistilappu!"
    
class Muistilappu(Esine):

    #def __init__(self, huone, nimi, pitka_nimi="", paino=0):
    #    super().__init__(huone, nimi, pitka_nimi, paino)
    #    self.random_pin = randint(0,8999) + 1000

    def lue(self, pelaaja):
        return 'Lapulle on kirjoitettu numerosarja "'+str(self.random_pin)+'". Mahtaako se olla jokin PIN-koodi?'
    
class Ahjo(Esine):


    def __init__(self, huone, nimi, pitka_nimi="", paino=0):
        super().__init__(huone, nimi, pitka_nimi, paino)
        self.sytytettavissa = True
        self.kuuma = False

    def siirra(self, lahde, kohde):
        return "Ahjoa ei voi siirtää."

    def sytyta(self, tavaraluettelo=None):

        if self.kuuma:
            return "Ahjo on jo kuuma."

        for tavara in tavaraluettelo:
            if tavara.nimi == "Tulitikut":
                self.kuuma = True
                self.pitka_nimi = "Ahjo (kuuma)"
                return "Sytytit ahjon. Se hehkuu nyt kuumana."

        return "Et voi sytyttää ahjoa ilman tulitikkuja."

class Vasara(Esine):
    pass
    
class Rautakanki(Esine):

    

    def kuumenna(self):
        ahjo = None
        for tavara in self.game.pelaaja.huone.tavaraluettelo:
            if tavara.nimi.lower() == "ahjo":
                ahjo = tavara
        if not ahjo:
            return "Tarvittaisiin kuuma ahjo"
        #Onko huoneessa kuuma ahjo
        #Jos on, niin rautakanki asetetaa kuumaksi
        if ahjo.kuuma:
            self.kuuma = True
            self.pitka_nimi = "Rautakanki (punahehkuinen)"
            return "Rautakanki kuumenee punahehkuiseksi."
        else:
            return "Ahjo ei ole kuuma."

    def tao(self):

        if not self.kuuma:
            return "Rautakanki ei ole tarpeeksi kuuma."

        for tavara in pelaaja.tavaraluettelo:
            if tavara.nimi.lower() == "vasara":

                pelaaja.tavaraluettelo.remove(self)

                miekka = Esine(None, "Miekka", "Terävä miekka", 5)
                pelaaja.tavaraluettelo.append(miekka)

                return "Taot rautakangesta miekan!"

        return "Tarvitset vasaran."

class Tuoli(Esine):
    pass

class Alasin(Esine):
    pass

class Kynttila(Esine):

    def __init__(self, huone, nimi, pitka_nimi="", paino=0):
        super().__init__(huone, nimi, pitka_nimi, paino)
        self.sytytettavissa = True
        self.palaa = False

    def sytyta(self, tavaraluettelo=None):

        # Palaako jo?
        if self.palaa:
            return "Kynttilä palaa jo, et voi sytyttää sitä uudelleen."

        # Kynttilä voidaan sytyttää, jos pelaajalla on tulitikut.
        for tavara in tavaraluettelo:
            if tavara.nimi == "Tulitikut":
                self.palaa = True
                self.pitka_nimi = "Kynttilä (palaa)"
                return "Kynttilä on sytytetty."
            
        return "Ei minulla ole mitään millä sytyttää."
   
    def sammuta(self):

        if self.palaa:
            self.palaa = False
            self.pitka_nimi = "Kynttilä"
            return "Kynttilä on sammutettu."
        else:
            return "Et voi sammuttaa kynttilää, joka ei pala."

class Tulitikut(Esine):
    pass

class Ovi(Esine):
    
    auki = False
    lukittu = True

    def siirra(self, lahde, kohde):
        return "Ovea ei saa irti"

    def avaa(self):
        if self.auki:
            return "Ovi on jo auki"
        elif self.lukittu:
            koodi = input ("Ovi näyttää olevan lukossa. Ovessa on pieni laite jossa on numeronäppäimet sekä pieni näyttö.\nNäytössä lukee SYÖTÄ 4-NUMEROINEN PIN:\n")
            if koodi == self.game.pelaaja.oven_pin:
                self.auki = True
                self.lukittu = False
                self.pitka_nimi = "Ovi pohjoiseen (auki)"
                return "Ovi avautuu narahtaen"
            else:
                return "Näppäimistö päästää ikävän äänen joka kertoo että syötit koodin väärin"
        return "Avaaminen ei onnistu" 

    def sulje(self):
        if not self.auki:
            return "Ovi on jo kiinni"
        else:
            self.auki = False
            self.lukittu = True
            self.pitka_nimi = "Ovi pohjoiseen (kiinni)"
            return "Ovi sulkeutuu narahtaen"
        
    def syota_pin(self, koodi, kohde):
        pass
   
    #def hae_ovi(self):
    #    if self.auki:
    #        return self.pitka_nimi + " (auki)"
    #    else:
    #        return self.pitka_nimi + " (kiinni)"
