import math

maxAppelsKist = 20
maxKistenPallet = 35
aantalAppelsOpPallet = maxAppelsKist * maxKistenPallet

aantalAppels = int(input())

hoeveelVolledigePallets = aantalAppels // aantalAppelsOpPallet
hoeveelOverigeVolleKisten = math.floor((aantalAppels % aantalAppelsOpPallet) / maxAppelsKist)
hoeveelAppelsOver = (aantalAppels % maxAppelsKist)

print(hoeveelVolledigePallets)
print(hoeveelOverigeVolleKisten)
print(hoeveelAppelsOver)
