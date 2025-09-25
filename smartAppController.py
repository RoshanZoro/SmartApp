from datetime import datetime
import pprint
nu = datetime.now()
bestand = open("gegevens.txt", "a")
with open("gegevens.txt", "r") as data:
    regels = data.readlines()
aantalRegels = len(regels) - 1

with open("gegevens.txt", "r") as f:
    kolommen = f.readline().strip().split(", ")
    data = []
    for lijn in f:
        waarden = lijn.strip().split(", ")
        row = dict(zip(kolommen, waarden))
        data.append(row)
# pprint.pp(data[0])

# cvInput = int(input("Van welke dag wil je informatie zien? "))

def cv():
    resultaat = []
    for row in data:
        setpoint = float(row["setPoint"])
        buitentemp = float(row["buitenTemperatuur"])
        reken = setpoint - buitentemp
        if reken >= 20:
            resultaat.append(100)
        elif reken >= 10 and reken < 20:
            resultaat.append(50)
        elif reken < 10:
            resultaat.append(0)
    return resultaat


def ventilatie():
    resultaat = []
    for row in data:
        aantalp = float(row["aantalPersonen"])
        stand = aantalp + 1
        if stand > 4:
            resultaat.append(4)
        else:
            resultaat.append(stand)
    return resultaat
def bewatering():
    resultaat = []
    for row in data:
        neerslag = float(row["neerslagMM"])
        if neerslag < 3:
            resultaat.append(True)
        elif neerslag >= 3:
            resultaat.append(False)
    return resultaat
ventilatieResultaten = ventilatie()
cvResultaten = cv()
bewateringResultaten = bewatering()
with open("uitvoerbestand.txt", "w") as f:
    f.write("datum, cvWaarde, ventilatieWaarde, bewateringWaarde \n")
    for i, row in enumerate(data):
        datum = str(row["datum"])
        cvWaarde = cvResultaten[i]
        ventilatieWaarde = ventilatieResultaten[i]
        bewateringWaarde = bewateringResultaten[i]
        f.write(f"{datum} {cvWaarde} {ventilatieWaarde} {bewateringWaarde}\n")

print(f"Er staan {aantalRegels} regels in het bestand.")
with open("uitvoerbestand.txt", "r") as f:
    uitvoerkolommen = f.readline().strip().split(", ")
    uitvoerdata = []
    for lijn in f:
        uitvoerwaarden = lijn.strip().split(", ")
        uitvoerrow = dict(zip(uitvoerkolommen, uitvoerwaarden))
        uitvoerdata.append(uitvoerrow)
# pprint.pp(uitvoerdata[0])
datumInput = int(input("Kies een datum [bv 1]: "))
datumuitvoer = uitvoerdata[datumInput]
pprint.pp(datumuitvoer)
