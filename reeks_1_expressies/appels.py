maxAppelsKist = 20
maxKistenPallet = 35
aantalAppelsOpPallet = maxAppelsKist * maxKistenPallet

aantalAppels = int(input())
print(aantalAppels // aantalAppelsOpPallet)
print(maxAppelsKist // (aantalAppels // aantalAppelsOpPallet))