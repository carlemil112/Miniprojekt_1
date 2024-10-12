# Funktion til at finde maksimum og minimum i en liste af tal
def Min_max(tal_liste):
    # Find max og min
    maksimum = max(tal_liste)
    minimum = min(tal_liste)
    
    # Returner som en tuple
    return maksimum, minimum

# Få input fra brugeren, split det til en liste og konverter til floats
user_input = input("Indtast en række af tal, adskilt med komma: ")
tal_liste = [float(tal) for tal in user_input.split(",")]

# Kald funktionen og få max og min
maks, min = Min_max(tal_liste)

# Udskriv resultatet
print(f"Det højeste tal er {maks} og det mindste tal er {min}.")
