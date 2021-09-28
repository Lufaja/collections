import random

#lijst met M&M kleuren
kleuren = ["oranje", "blauw", "groen", "bruin"]

#kleuren in de zak stoppen met bepaald aantal
def genereerZak(aantal:int):
    zak = {}
    for i in range (int(aantal)):
        kleur = random.choice(kleuren)
        if kleur in zak:
            zak[kleur] += 1
        else:
            zak.update({kleur : 1})
    return zak

x = input("Hoeveel M&M's wil je in de zak? ")
print(sorted(genereerZak(x).items(), key= lambda kv:kv[1], reverse=True))