
#8.2 Het creëren van functies
def gevoelsTemp (tempCel, vocht, windSnel):
    return round ( (tempCel - (vocht / 100) * windSnel), 2 )
def tempFahr (tempCel):
    return 1.8 * int(tempCel) + 32
def airco(tempCel):
    if int(tempCel) > 25:
        return "Het is warm. De airco kan aan."
    else:
        return "Het is niet warm."

dagen = 0
#f-string, 44 Eenvoudige Functies

while True: #7.5 De loop-en-een-half 89
    tempCel = input(f"Wat is de temperatuur op dag {dagen + 1}? [C] ")
    if tempCel == "":
        print("Je moet nog een getal invoeren!")
    else:
        tempCel = float(tempCel)

        windSnel = input("Wat is de windsnelheid? [m/s]")
        if windSnel == "":
            print("Je moet nog een getal invoeren!")
        else:
            windSnel = float(windSnel)

        vocht = input("Wat is de vochtigheid percentage? [%] ")
        if vocht == "":
            print("Je moet nog een getal invoeren!")
        else:
            vocht = int(vocht)

        temp = float(tempCel)
        fahrenheit = tempFahr(tempCel)
    tempCel = float(tempCel)
    windSnel = float(windSnel)
    vocht = float(vocht)
    print(f"Het is momenteel {tempCel} graden celcius.")
    print(f"Het is momenteel {fahrenheit} graden fahrenheit.")
    print(f"De gevoelstemperatuur is momenteel {gevoelsTemp(tempCel, vocht, windSnel)} graden.")
    print(airco(tempCel))
    if input():
       break
    dagen += 1

