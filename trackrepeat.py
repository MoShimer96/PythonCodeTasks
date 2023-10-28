class TrackRepeat:
    def __init__(self):
        # Sanakirja, jossa pidetään lukujen lukumäärät
        self.counts = {} 

    # pyydetty add funktion
    def add(self, x, k):
        #Tarkistaa aluksi löytyykö luku sanakirjasta
        if x in self.counts:
            self.counts[x] += k
        #Jos ei löydy niin k ei ole tarpeen korottaa lainkaan vaan syötetään sen sinne key value pairiin samalaisena kun se on ollut    
        else:
            self.counts[x] = k

    def check(self):
        #Laskee kaikki uniiqi arvot counts sanakirjassa. Valmis metodi on olemassa niin mitä pyörää uudelleen keksimään! 
        unique_counts = set(self.counts.values())
        return len(unique_counts) == len(self.counts)

if __name__ == "__main__":

    #Käytetään tehtävänannossa oleva luokka 
    t = TrackRepeat()
    print(t.check()) # True
    t.add(1, 3)
    print(t.check()) # True
    t.add(2, 3)
    print(t.check()) # False
    t.add(2, 2)
    print(t.check()) # True
    t.add(3, 1)
    print(t.check()) # True
    t.add(3, 4)
    print(t.check()) # False

#Ainakin tarkastus menee läpi niin, että tää palauttaa oikeat arvot.