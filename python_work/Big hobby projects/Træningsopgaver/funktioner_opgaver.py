#Summen af 2 tal:
def sum(x, y):
    return x + y

resultat_1 = sum(7,8)

print(resultat_1)

resultat_2 = sum(2,2)

print(resultat_2)



#Ulige eller lige tal:
def heltal(x):
    if x % 2 == 0:
        print("Tallet er lige")
    if x % 2 != 0:
        print("Tallet er ulige")

lige_tal = heltal(8)

print(lige_tal)

ulige_tal = heltal(7)

print(ulige_tal)

#Funktion med standard argumenter:
def produkt(x,y=10):
    
    return x*y

samlet = produkt(8)

print(samlet)

#Funktion med flere returneringer:
def sum_produkt_gennemsnit(x, y, z):
    return x+y+z, x*y*z, (x+y+z)/3

altialt = sum_produkt_gennemsnit(5, 7, 8)

print(altialt)


#Fakultet udregning
def fakultet(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * fakultet(n - 1)

# Test funktionen
print(fakultet(5))  # Output: 120
print(fakultet(3))  # Output: 6
