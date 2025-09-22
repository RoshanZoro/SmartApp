from datetime import datetime
nu = datetime.now()
bestand = open("gegevens.txt", "a")
with open("gegevens.txt", "r") as data:
    regels = data.readlines()
aantalRegels = len(regels) - 1

with open("gegevens.txt") as bestand:
    data = bestand.readlines()
    datum = []
    aantalPersonen = []
    setPoint = []
    buitenTemperatuur = []
    neerslagMM = []
    currentLine = 0
    #data in lijsten zetten zodat je het makkelijk kan printen
    for lines in data[1:]:
        currentLine += 1
        detail = [x.strip() for x in lines.split(",")]
        datum.append(detail[0])
        aantalPersonen.append(int(detail[1]))
        setPoint.append(float(detail[2]))
        buitenTemperatuur.append(float(detail[3]))
        neerslagMM.append(float(detail[4]))
cvInput = int(input("Van welke dag wil je informatie zien?"))

def CV():
    input = cvInput -1
    if (setPoint[input] - buitenTemperatuur[input]) >= 20:
        return 100

print(f"Er staan {aantalRegels} regels in het bestand.")
print(datum[0], aantalPersonen[0])
print(datum[1], aantalPersonen[1])
print(CV())