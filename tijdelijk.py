from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aardbei":3,
        "vannille":4,
        "chocolade":5
    }
    aanbieding = prijzen["aardbei"] * 0.8
    reclame_tekst ="Vandaag in de aanbieding : vanille-ijs, 1 liter - slechts €"+str(aanbieding) 

    reclame_tekst2 = reclame_tekst[:62]

    reclame_tekst3 = reclame_tekst2.upper()

    reclame_tekst4 = reclame_tekst3.split(" ")

    for el in reclame_tekst4 :
        if len(el)<5:
            print(el.lower())
        else:
            print(el.upper())

decoreer("aanbieding")
print_aanbieding()        