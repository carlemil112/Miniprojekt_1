#Opgave 1: Find maksimumværdien i en liste
#Skriv en funktion, der tager en liste af tal som input og returnerer det største tal i listen. Tip: Overvej at bruge en indbygget Python-funktion til at finde maksimumværdien.

def tal_input():
    indtastet = input("Indtast en liste af tal, adskilt med mellemrum").split()
    
    tal_liste = [int(tal) for tal in indtastet]
   
    print(f"Dit største tal er: {max(tal_liste)}")

#tal_input()






#Opgave 2: Længste ord i en sætning
#Skriv en funktion, der tager en sætning (string) som input og returnerer det længste ord i sætningen.
#Tip: Du kan bruge string-manipulation og en loop til at finde det længste ord.

def longest_sentence():
    sentence = input("Indtast en sætning").split()

    longest_word = max(sentence, key=len)

    print (f"Dit længste ord er: {longest_word}")






#Opgave 3: Tæl forekomsten af et ord
#Skriv en funktion, der tæller, hvor mange gange et bestemt ord optræder i en tekst. Teksten og ordet skal begge gives som input til funktionen. Tip: Se, om der er en måde at bruge Python's string metoder til dette.


def word_repeated():
    # Få sætningen og det ord, der skal tælles
    sætning = input("Indtast en sætning: ").split()
    ord_at_tælle = input("Hvilket ord vil du tælle?: ")
    
    # Brug .count() til at tælle forekomster af ordet i sætningen
    gentagelser = sætning.count(ord_at_tælle)
    
    print(f"Ordet '{ord_at_tælle}' optræder {gentagelser} gang(e) i sætningen.")

# Kald funktionen




#Opgave 4: Gennemsnittet af en liste
#Skriv en funktion, der tager en liste af tal og returnerer gennemsnittet af tallene. Hvis listen er tom, skal den returnere 0. Tip: Overvej, hvordan du håndterer tilfælde med tomme lister, og brug Python's funktioner til at regne summen ud.

def gennemsnit_liste():
    # Få brugerens input og split ved mellemrum
    liste = input("Indtast en liste af tal, opdelt med mellemrum: ").split()
    
    # Konverter input til en liste af heltal
    tal_liste = [int(tal) for tal in liste]
    
    # Beregn gennemsnittet korrekt med decimaltal
    gennemsnit = sum(tal_liste) / len(tal_liste)
    
    print(f"Gennemsnittet er {gennemsnit}")

gennemsnit_liste()





#Opgave 5: Sortering af en liste
#Skriv en funktion, der tager en usorteret liste af tal som input og returnerer en sorteret liste. Tip: Se på Python's indbyggede sorteringsfunktioner, men prøv også at skrive en simpel sorteringsalgoritme selv, som f.eks. boblesortering.

