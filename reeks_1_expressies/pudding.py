aantalStuks = int(input())
kostprijsStuk = float(input())
aantalBarcodes = int(input())
aantalMijnen = int(input())

gespendeerdeDollars = aantalStuks * kostprijsStuk
aantalFrequentFlyerMijlen = (aantalStuks // aantalBarcodes) * aantalMijnen

print(f"Phillips spendeerde ${gespendeerdeDollars} voor {aantalFrequentFlyerMijlen} frequent flyer mijlen.")