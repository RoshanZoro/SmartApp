tempCel = int( input("Wat is de temperatuur? ") )
windSnel = int( input("Wat is de windsnelheid? "))
vocht = int( input("Wat is de vochtigheid percentage? "))
tempFahr = 1.8 * tempCel + 32
gevoelsTemp = tempCel - (vocht / 100) * windSnel
print(f"Het is momenteel {tempCel} graden celcius.")
print(f"Het is momenteel {tempFahr} graden fahrenheit.")
print(f"De gevoelstemperatuur is momenteel {gevoelsTemp} graden.")