prijzen = {
    "aardbei":3,
    "vannille":4,
    "chocolade":5
}
aanbieding = prijzen["vannille"] * 0.8
reclame_tekst ="Vandaag in de aanbieding : vanille-ijs, 1 liter - slechts €"+str(aanbieding) 

reclame_tekst2 = reclame_tekst[:62]

reclame_tekst3 = reclame_tekst2.upper()
print(reclame_tekst3)