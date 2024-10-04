message = "Helloo Python world!!"
print(message)
message = "Hello Python Crash Course world"
print(message)
first_name="Ida"
last_name="Lilkaer"
full_name=f"{first_name} {last_name}"
print(full_name)
print(f"Hej, {full_name.title()}!")
message=f"Hej, {full_name.title()}!"
print(message)
print("\tPython") #Laver et indhak til koden at indsætte \t
print("Languages:\n\tPython\n\tC\n\tJavascript") # \n skaber et linjeskift, tilsvarende \newline i latex

print(full_name.lower()) #skriver full_name med små bogstaver
print(full_name.upper()) #skriver full_name med STORE bogstaver
print(full_name.title()) #Skriver full_name med store begyndelsesbogstaver til hvert ord
print(f"Hej {first_name}, du er skøn") #En variabel inkluderet i en string udføres med f"
print('Albert Einstein sagde engang, “En person som aldrig har lavet en fejl, har aldrig prøvet noget nyt.”') #Brug af citationstegn uden at ødelægge koden, ved at bruge apostrof istedet. virker også vice versa
berømt_person="Albert Einstein " #Her gemmer jeg Einstein som en variabel "berømt person"
besked=f'{berømt_person} sagde engang, "En person som aldrig har lavet en fejl, har aldrig prøvet noget nyt."' #Her er citatet i gemt i variablen "besked
print(besked) #Her bliver beskeden printet, vha. det tilknyttede citat

navn="\tJohn Doe\n" #gemmer navn med ekstra mellemrum i begyndelsen og slutningen
print(navn) #print af det ekstra mellemrum navn
print(navn.lstrip()) # Navnet med fjernet startmellemrum (venstre)
print(navn.rstrip()) #Navnet med fjernet slutmellemrum (højre)

filnavn = "python_notes.txt" # Gem filnavn i en variabel
filnavn_uden_udvidelse = filnavn.removesuffix('.txt') # Brug removesuffix() til at fjerne filudvidelsen
print(f"Filnavn uden udvidelse: {filnavn_uden_udvidelse}") # Print filnavnet uden udvidelse

print(5+3) #addition som giver 8
print(10-2) #subtraktion som giver 8
print(4*2) #Multiplikation som giver 8
print(16/2) #Division som giver 8
print("888 KESIIII") #lmao 888 er kesi jo

favorit_tal=7 #variabel der har gemt mit favorittal
favorittal_leak=f"Mit favorittal er {favorit_tal}." #Kæmpe leak af mit favorittal vha. variablen. HUSK f" i starten når der er en variabel i
print(favorittal_leak)

#OPGAVESÆT 3: LISTER

names=["Daniel","Marcus", "Victor"] #Liste over gode homies

for navne in names: #"for" gør det muligt at udføre en blok af kode flere gange, ved hvert element, så i dette tilfælde hvert navn. "in" vælger hvilken liste det skal være for - i dette tilfælde names.
    print(navne)

for name in names:
    print(f"Hej {name}! Du er sgu en god ven") #Her er der en hilsen til hver ven i listen "names", fra kommandoen "for name in names:"

transportmidler=["motorcykel","bil","cykel"] #Her har jeg lavet min egen liste
for transport in transportmidler:
    print(f"Jeg kunne godt tænke mig at køre på en {transport}")

gaesteliste = ["Ronaldo", "XQC", "Juice Wrld"] #En liste med gæster jeg gerne vil invitere til houseparty

for gaester in gaesteliste: #Her vælger den alle gæster i gæstelisten vha. "for" og "in"
    print(f"Kære {gaester}, det ville være en crazy fest hvis i 3 havde en samtale, kom glad.")


print("\nDesværre har Juice Wrld meddelt, at han ikke kan komme til festen.") # Udskriv en besked om, at en af gæsterne ikke kan komme, (RIP JUICE)


gaesteliste[2] = "Travis Scott" # Erstat "Juice Wrld" med "Travis Scott" - god mand. VIST AT DET ER EN NY LISTE MED "[2]"


print("\nHer er de nye invitationer til den opdaterede gæsteliste:") # Udskriv en ny runde invitationer til den opdaterede gæsteliste
for gaester in gaesteliste:
    print(f"Kære {gaester}, du er stadig inviteret til mit houseparty. Det bliver legendarisk!")

# Udskriv en besked om, at vi har fundet et større bord
print("\nGod nyhed! Jeg har fundet et større bord, så vi kan invitere flere gæster.")

# Tilføj en ny gæst til begyndelsen af listen
gaesteliste.insert(0, "Billie Eilish")

# Tilføj en ny gæst til midten af listen (indekset vil være længden af listen divideret med 2)
midten = len(gaesteliste) // 2
gaesteliste.insert(midten, "Elon Musk")

# Tilføj en ny gæst til slutningen af listen
gaesteliste.append("Oprah Winfrey")

# Udskriv en ny runde invitationer til den udvidede gæsteliste
print("\nHer er de nye invitationer til den opdaterede gæsteliste:")
for gaester in gaesteliste:
    print(f"Kære {gaester}, du er inviteret til mit houseparty. Det bliver endnu vildere nu!")

# Start med den gæsteliste fra opgave 3-6
gaesteliste = ["Billie Eilish", "Ronaldo", "XQC", "Elon Musk", "Travis Scott", "Oprah Winfrey"]

# Udskriv en besked om, at vi kun kan invitere to gæster
print("\nDesværre vil det nye bord ikke komme i tide, så jeg kan kun invitere to gæster til middagen.")

# Brug pop() til at fjerne gæster én ad gangen og udskriv en besked
while len(gaesteliste) > 2:
    fjernet_gaest = gaesteliste.pop()  # Fjerner den sidste gæst på listen
    print(f"Beklager, {fjernet_gaest}, jeg kan desværre ikke invitere dig til middagen.")

# Udskriv en besked til de to gæster, der stadig er inviteret
for gaester in gaesteliste:
    print(f"Kære {gaester}, du er stadig inviteret til middagen.")

# Brug del til at fjerne de sidste to gæster og tømme listen
del gaesteliste[0]
del gaesteliste[0]

# Bekræft at listen er tom
print(f"\nDen endelige gæsteliste er nu tom: {gaesteliste}")



# Opgave 3-8

steder_at_se=["Zakynthos","Japan","USA"] #Liste over steder jeg gerne vil se

print(steder_at_se) #udskriv stederne

print(sorted(steder_at_se)) #stederne udskrevet i rækkefølge med "sorted"

print(steder_at_se) #den originale forbliver usorteret

steder_at_se.reverse() #sorterer listen til omvendt rækkefølge af original
print(steder_at_se) #viser den omvendte udprintet

steder_at_se.sort(reverse=True) #Her får jeg den til at sortere baglæns.
print(steder_at_se) #og igen - printet

print(len(gaester)) #her kan jeg se hvor mange gæster der var på gæstelisten fra før

