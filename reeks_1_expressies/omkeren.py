lijst = []
for i in range(3):
    lijst.append(int(input()))
lijst.reverse()
s = ""
for x in range(len(lijst)):
    s = s + f"{lijst[x]}" + " "
print(s)