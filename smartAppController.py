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
pprint.pp(data[0])

cvInput = int(input("Van welke dag wil je informatie zien? "))

def CV():
    inputUser = data[cvInput -1]
    setpoint = float(inputUser["setPoint"])
    buitentemp = float(inputUser["buitenTemperatuur"])
    reken = setpoint - buitentemp
    if reken >= 20:
        return 100
    elif reken >= 10 and reken < 20:
        return 50
print(f"Er staan {aantalRegels} regels in het bestand.")


print(CV())