# 8.2 Het creëren van functies
stopLijst = ["stop", "exit", "quit", "sotp", "stoop"]
tempLijst = [] #Deze moest buiten de loop anders werkte hij niet
dagen = 0
stopProgramma = False


def gevoelsTemp(tempCel, vocht, windSnel):
    return round((tempCel - (vocht / 100) * windSnel), 2)


def tempFahr(tempCel):
    return round((1.8 * int(tempCel) + 32), 2)


def airco(gevoelsTemp):
    if int(gevoelsTemp) > 25:
        return "Het is warm. De airco kan aan."
    elif int(gevoelsTemp) < 0 and windSnel > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif int(gevoelsTemp) < 0 and windSnel <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 < int(gevoelsTemp) < 10 and windSnel > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 < int(gevoelsTemp) < 10 and windSnel < 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 < int(gevoelsTemp) < 22:
        return "Heerlijk weer, niet te koud of te warm."
    return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"


#Def zodat ik niet bij elke vraag het zelfde hoef te zetten
def vraag(prompt, vochtPercentage=False):
    while True:
        waarde = input(prompt)
            #var voor de input en de input tekst (prompt)
            #https://www.w3schools.com/python/ref_func_input.asp
        if waarde == "":
            print("Je moet nog een getal invoeren!")
            continue
            #Als er niks getypt word, tekst printen en herhalen
        if waarde.lower() in stopLijst:
            return None
            #Als de input tekst in mijn lijst staat het programma stoppen met break
        try:
            waarde = float(waarde)
            #input veranderen naar float
        except ValueError:
            print("Dit is geen geldig getal.")
            continue
            #Als de input geen getal is (float in ons geval) dan gooit hij Value Error met een print
            #https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples
        if vochtPercentage and waarde > 100:
            print("Het percentage mag niet hoger dan 100 zijn.")
            continue
            #Snelle vocht percentage check
        return waarde


# f-string, 44 Eenvoudige Functies, in het boek is f-string niet te vinden maar op google wel zoals
#https://www.w3schools.com/python/python_string_formatting.asp

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
    #12.4 List methodes

    tempLijst.append(gevoel)
    gemiddeldeTemp = round ( (sum(tempLijst) / len(tempLijst) ), 2 )
    print("-" * 40)
    print(f"Het is momenteel {tempCel} graden celcius.")
    print(f"Dat is {fahrenheit} graden fahrenheit.")
    print(f"De gevoelstemperatuur is momenteel {gevoel} graden.")
    print(airco(gevoel))
    print(f"De gemiddelde temperatuur is {gemiddeldeTemp} graden.")
    print("-" * 40)
    dagen += 1
    if dagen >= 7:
        break
