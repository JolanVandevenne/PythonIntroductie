soort = input()
x = input()
boolean = input()

if (soort == "waarde"):
    if (int(x) % 2 == 0 and boolean == "ja"):
        print(f"Juist: kaarten met waarde {x} moeten gedraaid worden.")
    elif (int(x) % 2 != 0 and boolean == "nee"):
        print(f"Juist: kaarten met waarde {x} moeten niet gedraaid worden.")
    elif (int(x) % 2 == 0 and boolean == "nee"):
        print(f"Fout: kaarten met waarde {x} moeten gedraaid worden.")
    elif (int(x) % 2 != 0 and boolean == "ja"):
        print(f"Fout: kaarten met waarde {x} moeten niet gedraaid worden.")
elif (soort == "kleur"):
    if (x == "rood" and boolean == "nee"):
        print(f"Juist: kaarten met kleur {x} moeten niet gedraaid worden.")
    elif (x != "rood" and boolean == "ja"):
        print(f"Juist: kaarten met kleur {x} moeten gedraaid worden.")
    elif (x == "rood" and boolean == "ja"):
        print(f"Fout: kaarten met kleur {x} moeten niet gedraaid worden.")
    elif (x != "rood" and boolean == "nee"):
        print(f"Fout: kaarten met kleur {x} moeten gedraaid worden.")