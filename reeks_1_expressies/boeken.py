boekPrijs = 24.95
inkoopBoekPrijs = boekPrijs * 0.6
eersteVerzendkostBoek = 3
tweedeVerzendkostBoek = 0.75
aantalBoeken = 60

prijs_60_boeken = (inkoopBoekPrijs * aantalBoeken) + eersteVerzendkostBoek + (tweedeVerzendkostBoek * (aantalBoeken - 1))
print(prijs_60_boeken)