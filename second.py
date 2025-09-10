
#8.2 Het creëren van functies
def gevoelsTemp (tempCel, vocht, windSnel):
    return round ( (tempCel - (vocht / 100) * windSnel), 2 )
def tempFahr (tempCel):
    return round ( (1.8 * int(tempCel) + 32), 2 )
def airco(gevoelsTemp):
    if int(gevoelsTemp) > 25:
        return "Het is warm. De airco kan aan."
    else:
        return "Het is niet warm."

dagen = 0
stopProgramma = False
#f-string, 44 Eenvoudige Functies

while not stopProgramma: #7.5 De loop-en-een-half 89
    while True:
        tempCel = input(f"Wat is de temperatuur op dag {dagen + 1}? [C] ")
        if tempCel == "":
            print("Je moet nog een getal invoeren!")
            continue
        elif tempCel.lower() == "stop":
            stopProgramma = True
            break
        else:
            tempCel = float(tempCel)
            break
    while True:
        windSnel = input("Wat is de windsnelheid? [m/s]")
        if windSnel == "":
            print("Je moet nog een getal invoeren!")
            continue
        elif windSnel.lower() == "stop":
            stopProgramma = True
            break
        else:
            windSnel = float(windSnel)
            break
    while True:
        vocht = input("Wat is de vochtigheid percentage? [%] ")
        if vocht == "":
            print("Je moet nog een getal invoeren!")
            continue
        elif vocht.lower() == "stop":
            stopProgramma = True
            break
        else:
            vocht = float(vocht)
            break
#temp = float(tempCel)
    fahrenheit = tempFahr(tempCel)
#tempCel = float(tempCel)
#windSnel = float(windSnel)
#vocht = float(vocht)
    gevoel = gevoelsTemp(tempCel, vocht, windSnel)

    print(f"Het is momenteel {tempCel} graden celcius.")
    print(f"Het is momenteel {fahrenheit} graden fahrenheit.")
    print(f"De gevoelstemperatuur is momenteel {gevoelsTemp(tempCel, vocht, windSnel)} graden.")
    print(airco(gevoel))
    print("-" * 40)
    #if input():
     #  break
    dagen += 1

