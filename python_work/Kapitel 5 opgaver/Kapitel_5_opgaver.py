cars = ['audi', 'bmw', 'subaru','toyota'] # En liste over biler

for car in cars: #Starter en kommando med listen
    if car in cars: #Hvis bilen på listen med biler:
        if car == 'bmw': #Hvis bilen på listen er bmw gælder:
            print(car.upper()) #At bogstaverne skal skrives med stort "BMW"
        else:
            print(car.title()) #For de andre biler skal forbogstavet være stort
car ='bmw' #Værdien car=bmw
car =='bmw' #Tjek om værdien af car er bmw
print(car=='bmw') #Her printes enten true eller false, som i dette tilfælde er TRUE

car = 'audi' #bærdien car=audi
car == 'bmw' 
print(car=='bmw') #Her er det falsk fordi audi ikke skal være = bmw på listen.

car = 'Audi'
car == 'audi'
print(car=='audi')

requested_topping = 'mushrooms' 
if requested_topping != 'anchovies': #Her bliver der spurgt "Er mushrooms ikke lig anchovies?" Da mushrooms og anchovies er forskellige er dette true
    print("Hold the anchovies!") #Derfor eksekveres koden

answer = 17 #Samme koncept her, bare med tal
if answer != 42: #Hvis answer ikke er =42, eksekveres nedestående print, og det er det ikke, det er 17!
    print("That is not the correct answer. Please try again!")

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
True
age_0 = 18
age_0 >= 21 or age_1 >= 21
False

banned_users = ['andrew', 'carolina', 'david'] #En variabel med 3 strings gemt som bannede brugere
user = 'marie' #definerer user til at være marie
if user not in banned_users: #Hvis brugeren ikke er i banned_users, eksekveres nedenstående kode
    print(f"{user.title()}, you can post a response if you wish.") #Dette printes, da user "marie" IKKe er banned

#OPGAVE 5-1 CONDITIONAL TESTS:
# Tildel en værdi til variablen 'car'
car = 'subaru'

# Første test: Er bilen en Subaru? (True)
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # Denne sammenligning bør være sand (True)

# Anden test: Er bilen en Audi? (False)
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # Denne sammenligning bør være falsk (False)

# Tredje test: Er bilen ikke en Toyota? (True)
print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')  # Denne sammenligning bør være sand (True)

# Fjerde test: Er bilen en Honda? (False)
print("\nIs car == 'honda'? I predict False.")
print(car == 'honda')  # Denne sammenligning bør være falsk (False)

# Femte test: Er bilens navn længere end 3 tegn? (True)
print("\nIs the length of car > 3? I predict True.")
print(len(car) > 3)  # Denne sammenligning bør være sand (True)

# Sjette test: Er bilens navn i små bogstaver? (True)
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')  # Denne sammenligning bør være sand (True)

# Syvende test: Er bilens navn i store bogstaver? (False)
print("\nIs car.upper() == 'SUBARU'? I predict False.")
print(car.upper() == 'subaru')  # Denne sammenligning bør være falsk (False)

# Ottende test: Er bilens navn startet med 's'? (True)
print("\nDoes car start with 's'? I predict True.")
print(car.startswith('s'))  # Denne sammenligning bør være sand (True)

# Niende test: Er bilens navn slut med 'o'? (False)
print("\nDoes car end with 'o'? I predict False.")
print(car.endswith('o'))  # Denne sammenligning bør være falsk (False)




age = 17
if age >= 18:
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


#"elif" anvendelse

age = 12 #En alder er defineret

if age < 4: #Hvis alder er under 4 printes denne:
    print("Your admission cost is $0.")
elif age < 18: #Hvis alder er over 4 men under 18 printes denne:
    print("Your admission cost is $25.")
else: #For resten af de forskellige mulige aldre (<18) printes:
    print("Your admission cost is $40.")

#Dette kan forenkles ved at sætte priser direkte ind i koden:
age = 20

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")






