startKm = float(input())
eindKm = float(input())
aantalLBenzine = float(input())

verbruikPer100Km = aantalLBenzine / ((eindKm - startKm) / 100) 

print(verbruikPer100Km)