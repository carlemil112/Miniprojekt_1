#Celsius til Fahrenheit omregner

def Celcius_Fahrenheit(celsius):

    return celsius * 9/5 + 32


user_input = float(input("Indtast en temperatur i celcius"))

fahrenheit = Celcius_Fahrenheit(user_input)

print(f"Temperaturen er {fahrenheit} fahrenheit")