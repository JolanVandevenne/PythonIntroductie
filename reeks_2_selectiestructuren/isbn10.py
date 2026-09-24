lijst = [None] * 9

for i in range(len(lijst)):
    lijst[i] = int(input()) * (i + 1)

controleGetal = int(input())
sum = sum(lijst) % 11

if controleGetal == sum:
    print("OK")
else:
    print("FOUT")