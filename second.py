# 8.2 Het creëren van functies
stopLijst = ["stop", "exit", "quit", "sotp"]
dagen = 0
stopProgramma = False


def gevoelsTemp(tempCel, vocht, windSnel):
    return round((tempCel - (vocht / 100) * windSnel), 2)


def tempFahr(tempCel):
    return round((1.8 * int(tempCel) + 32), 2)


def airco(gevoelsTemp):
    if int(gevoelsTemp) > 25:
        return "Het is warm. De airco kan aan."
    else:
        return "Het is niet warm."


def vraag(prompt, vochtPercentage=False):
    while True:
        waarde = input(prompt)
        if waarde == "":
            print("Je moet nog een getal invoeren!")
            continue
        if waarde.lower() in stopLijst:
            return None
        try:
            waarde = float(waarde)
        except ValueError:
            print("Dit is geen geldig getal.")
            continue
        if vochtPercentage and waarde > 100:
            print("Het percentage mag niet hoger dan 100 zijn.")
            continue
        return waarde


# f-string, 44 Eenvoudige Functies

while not stopProgramma:  # 7.5 De loop-en-een-half 89
    tempCel = vraag(f"Wat is de temperatuur op dag {dagen + 1}? [C] ")
    if tempCel is None:
        break
    windSnel = vraag("Wat is de windsnelheid? [m/s]")
    if windSnel is None:
        break
    vocht = vraag("Wat is de vochtigheid percentage? [%] ", vochtPercentage=True)
    if vocht is None:
        break
    fahrenheit = tempFahr(tempCel)
    gevoel = gevoelsTemp(tempCel, vocht, windSnel)

    print(f"Het is momenteel {tempCel} graden celcius.")
    print(f"Het is momenteel {fahrenheit} graden fahrenheit.")
    print(f"De gevoelstemperatuur is momenteel {gevoel} graden.")
    print(airco(gevoel))
    print("-" * 40)
# if input():
#  break
    dagen += 1
