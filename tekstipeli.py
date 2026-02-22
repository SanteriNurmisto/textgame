class Huone:
    tavaraluettelo = []
    def __init__(self, kuvaus):
        self.kuvaus = kuvaus

        self.tavaraluettelo.append(Kirja("Kirja", 1))
        self.tavaraluettelo.append(Vasara("Vasara", 3))
        self.tavaraluettelo.append(Rautakanki("Rautakanki", 5))
        self.tavaraluettelo.append(Tuoli("Tuoli", 7))
        self.tavaraluettelo.append(Alasin("Alasin", 9))
        self.tavaraluettelo.append(Ovi("Ovi", None))
        self.tavaraluettelo.append(Kynttila("Kynttilä", 0.1))
        self.tavaraluettelo.append(Tulitikut("Tulitikut", 0.01))

    def katso(self):
        tavarat = ""
        for tavara in self.tavaraluettelo:
            if tavara.nimi.lower() == "ovi":
                tavarat += tavara.hae_ovi() + "\n"
            else:
                tavarat += tavara.nimi + "\n"

        return self.kuvaus+ ".\nSisältää seuraavat tavarat: \n" + tavarat

class Pelaaja:
    tavaraluettelo = []
    def __init__(self, nimi, kantokyky):
        self.nimi = nimi
        self.kantokyky = kantokyky

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
        for tavara in huone.tavaraluettelo:
            if tavara.nimi.lower() == kohde and tavara.nimi.lower() == "ovi":
                if tavara.auki:
                    return "Ovi on jo auki"
                else:
                    tavara.auki = True
                    return "Ovi avautuu narahtaen"
        return "Ei ole mitään avattavaa"

    def sulje(self,kohde):
        for tavara in huone.tavaraluettelo:
            if tavara.nimi.lower() == kohde and tavara.nimi.lower() == "ovi":
                if not tavara.auki:
                    return "Ovi on jo kiinni"
                else:
                    tavara.auki = False
                    return "Ovi sulkeutuu narahtaen"
        return "Ei ole mitään suljettavaa"

class Esine:

    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

    def siirra(self, lahde, kohde):
        lahde.tavaraluettelo.remove(self)
        kohde.tavaraluettelo.append(self)
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
        #return "Tämä kirja on Taru sormusten herrasta"
        #print(pelaaja.lue(kohde))
        if self.luettu:
            return "Tämä kirja on taru sormusten herrasta"
        else:
            self.luettu = True
            huone.tavaraluettelo.append(Muistilappu("Muistilappu", 0))
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

        # Jos ei ole mitään tavaroita, ei voi myöskään sytyttää mitään.
        if not tavaraluettelo:
            return "Et voi sytyttää kynttilää."
        
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
    def __init__(self, nimi, paino):
        super().__init__(nimi, paino)
        self.auki = False

    def siirra(self, kohde, huone):
        return "Ovea ei saa irti"

    def hae_ovi(self):
        if self.auki:
            return self.nimi + " (auki)"
        else:
            return self.nimi + " (kiinni)"
    

pelaaja = Pelaaja("Jaska", 10)
huone = Huone("Kellarivarasto")

def parseri(syote):
    sanat = syote.split(" ")
    if len(sanat) > 1:
        return sanat[0].lower(), sanat[1].lower()
    else:
        return syote.lower(), None
    
while True:
    syote = input("Mitä haluaisit tehdä? ")
    komento, kohde = parseri(syote)
    if komento == "exit":
        break
    elif komento == "ota":
        print(pelaaja.ota(kohde, huone))   

    elif komento == "pudota":
        print(pelaaja.pudota(kohde, huone))

    elif komento == "katso":
        print(huone.katso())

    elif komento == "inv":
        print(pelaaja.inv())

    #elif komento == "lue" and kohde == "kirja":
        #print(pelaaja.lue(kohde))
        #print("Kirjan välistä näyttänee tippuneen joku lappu")
        #huone.tavaraluettelo.append(Muistilappu("Muistilappu", 0))

    elif komento == "lue":
        print(pelaaja.lue(kohde))
    elif komento == "sytytä":
        print(pelaaja.sytyta(kohde))
    elif komento == "sammuta":
        print(pelaaja.sammuta(kohde))
    elif komento == "avaa":
        print(pelaaja.avaa(kohde))
    elif komento == "sulje":
        print(pelaaja.sulje(kohde))
    else:
        print("En ymmärrä mitä haluat tehdä")