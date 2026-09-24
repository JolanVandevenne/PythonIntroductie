a = input()
b = input()
c = a+b

regels = {
    "rechtsrechts": [1],
    "rechtslinks": [2],
    "rechtsevenwicht": [3],
    "linksrechts": [4],
    "linkslinks": [5],
    "linksevenwicht": [6],
    "evenwichtrechts": [7],
    "evenwichtlinks": [8],
    "evenwichtevenwicht": [9],
}

print(f"muntstuk #{regels[c][0]} is vervalst")