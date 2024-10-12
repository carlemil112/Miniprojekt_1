#Myndighedstjek

alder = 30
if alder >= 18:
    print("Du er myndig")

else:
    print("Du er ikke myndig")



#Karakter udregner

score = 44

if score >=90:
    print(12)

elif 80 <= score <= 89:
    print(10)

elif 70 <= score <= 79:
    print(7)

elif 60 <= score <= 69:
    print(4)

else:
    print("02")


#Er dine 2 tal positive eller negative?
pass
input_1 = int(input("Indtast tal 1:"))
pass
input_2 = int(input("Indtast tal 2:"))

if input_1 < 0 and input_2 >0:
    print("Input 1 er negativt, input 2 er positivt")

elif input_1 > 0 and input_2 >0:
    print("Input 1 er positivt, input 2 er positivt")

elif input_1 > 0 and input_2 <0:
    print("Input 1 er positivt, input 2 er negativt")

else: print("input 1 er negativt, input 2 er negativt")
    


#Er dit tal positivt, negativt eller = 0?
pass
input_tal = int(input("Indtast et tal:"))

if input_tal == 0:
    print("Dit tal er 0")

elif input_tal <=0:
    print("Dit tal er negativt")

else: print("Dit tal er positivt")


#Rabatberegner

payment = 700

if payment >1000:
    new_price = payment*0.80
    print(f"Din pris er på 20% rabat, og er nu: {new_price}")

elif  500 <= payment <=1000:
    new_price = payment*0.90
    print(f"Din pris er på 10% rabat, og er nu {new_price}")

else: print(f"Du får ikke rabat, og din pris er derfor: {payment}")