
gelijkspel = False

regels = {
    "schaar": ["hagedis", "blad"],
    "steen": ["hagedis", "schaar"],
    "blad": ["steen", "Spock"],
    "hagedis": ["Spock", "blad"],
    "Spock": ["schaar", "steen"],

}

while True:
    speler1 = input()
    speler2 = input()
    if speler1 == speler2:
        print("gelijkspel")
        break
    elif speler1 in regels[speler2]:
        print("speler2 wint")
        break
    else:
        print("speler1 wint")
        break

    