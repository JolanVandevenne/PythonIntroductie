getallen = []
for getal in range(9):
    getallen.append(int(input()))
controlecijfer = int(input())
controle = 0
for i in getallen:
    controle = controle + (i+ 1 * getallen[i])
print(controle)
if (controle % 11 == controlecijfer):
    controleOK = "OK"
else:
    controleOK = "FOUT"

print(controleOK)

#------------------------------------
x = [None] * 3

for i in range(len(x)):
    x[i] = int(input())

sum = sum([i*val for i, val in enumerate(x) if i < len(x) - 1])

if sum % 11 == x[len(x) -1]:
    print("OK")
else:
    print("FOUT")