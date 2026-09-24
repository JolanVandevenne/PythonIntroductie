from datetime import datetime

beginUur = int(input())
beginMin = int(input())
eindUur = int(input())
eindMin = int(input())

minBeginUur = datetime.strptime("18:00", "%H:%M")
maxEindUur = datetime.strptime("00:00", "%H:%M")

beginTijd = datetime.strptime(f"{beginUur}:{beginMin}", "%H:%M")
eindTijd = datetime.strptime(f"{eindUur}:{eindMin}", "%H:%M")

tariefWissel = datetime.strptime("21:30", "%H:%M")

eerste = ((tariefWissel - beginTijd).seconds / 60 / 60) * 2
tweede = ((eindTijd - tariefWissel).seconds / 60 / 60) * 4

if (beginUur < minBeginUur or (eindUur > maxEindUur or eindUur < minBeginUur)):
    print("ongeldige invoer")

print(eerste + tweede)

