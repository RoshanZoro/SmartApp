
#8.2 Het creëren van functies
def gevoelsTemp (tempCel, vocht, windSnel):
    return tempCel - (vocht / 100) * windSnel
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
        tempCel = int(input(f"Wat is de temperatuur op dag {dagen + 1}? [C] ") )
        if tempCel == "":
            print("Je moet nog een getal invoeren!")
        else:
            windSnel = int( input("Wat is de windsnelheid? [m/s]"))
        if windSnel == "":
            print("Je moet nog een getal invoeren!")
        else:
            vocht = int( input("Wat is de vochtigheid percentage? [%] "))

        temp = float(tempCel)
        fahrenheit = tempFahr(tempCel)

    print(f"Het is momenteel {tempCel} graden celcius.")
    print(f"Het is momenteel {fahrenheit} graden fahrenheit.")
    print(f"De gevoelstemperatuur is momenteel {gevoelsTemp} graden.")
    print(airco)
    #if
     #   break
    dagen += 1

