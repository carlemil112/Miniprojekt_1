magicians = ['alice', 'david', 'carolina'] #Jeg definerer en liste over magicians, med navnene inde i klememrne
for magician in magicians: #dette får python til at associere et navn i magicians med "magician"
    print(magician) #Denne printer det ovenstående. Kan forståes som “For every magician in the list of magicians, print the magician’s name.”
    #dette kaldes looping

    print(f"{magician.title()}, that was a great trick!") #Her printes den samme sætning for hver magician, da det tidligere er defineret. da der ikke står noget i "title() tager den for alle"
    print(f"I can't wait to see your next trick, {magician.title()}.\n") #Her er det samme, men newline "n" skaber et fint mellemrum mellem hver print kommando.

print("Thank you everyone. That was a great magic show!.\n") #Denne kode er ikke indrykket, og er derfor ikke en del af loopet og vil ikke gentages for alle

#OPGAVE 4-1
pizzaer_jeg_kan_lide = ['pepperoni', 'skinke', 'kebab']
for pizza in pizzaer_jeg_kan_lide:
    print(pizza)

    print(f"Jeg elsker {pizza.title()}")
print("Jeg elsker virkelig pizza!")

#OPGAVE 4-2
kaeledyrerne = ['hund', 'skildpadde', 'fisk']
for kaeledyr in kaeledyrerne:
    print(kaeledyr)

    print(f"En {kaeledyr.title()} ville være et godt kæledyr\n")
print("De ville alle være gode kæledyr!")

#NUMERISKE LISTER

for value in range(1, 5): #Her får jeg python til at gemme alle tal mellem 1-5
    print(value) #Her bliver disse tal printet

even_numbers = list(range(2, 11, 2)) #Her går python fra 2-11, og lægger to til for hvert tal
print(even_numbers) #Her printes resultatet, som er lige tal

squares = [] #tom liste der hedder squares
for value in range(1, 11): #Den tager opløftet tal for alle tal mellem 1-10
    square = value ** 2 #to ** giver opløftet, den tager value og tager det i anden altså
    squares.append(square) #Det looper den for value af square, som der så samles fra listen "squares"

print(squares) #Her udskrives resultatet

#Nedenfor findes minimum, maksimum og summen af en liste med tal:
digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
0
max(digits)
9
sum(digits)
45

#OPGAVE 4-10:
# Opretter en liste over de første 10 kvadrattal
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

# Udskriver listen over kvadrattal
print(f"Alle kvadrattal: {squares}")

# Udskriver de første tre elementer i listen
print("The first three items in the list are:")
print(squares[:3])

# Udskriver tre elementer fra midten af listen
print("Three items from the middle of the list are:")
middle_index = len(squares) // 2
print(squares[middle_index-1:middle_index+2])

# Udskriver de sidste tre elementer i listen
print("The last three items in the list are:")
print(squares[-3:])
