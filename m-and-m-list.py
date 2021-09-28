import random

#lijst met M&M kleuren
kleuren = ["oranje", "blauw", "groen", "bruin"]

#kleuren in de zak stoppen met bepaald aantal
def genereerZak(aantal:int):
    zak = []
    for i in range (int(aantal)):
        zak.append(random.choice(kleuren))
    return zak

x = input("Hoeveel M&M's wil je in de zak? ")
print(sorted(genereerZak(x)))