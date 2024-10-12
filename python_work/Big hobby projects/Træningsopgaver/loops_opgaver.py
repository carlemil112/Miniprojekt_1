# Print 5 tal, hvor hvert tal fordobles
for i in range(5):
    double = i * 2
    print(double)

# While loop - tæl ned fra 10, og skriv færdig efter
tal = 10
while tal > 0:
    print(tal)
    tal -= 1  # Tæller ned

print("Færdig!")  # Når while-loopet er færdigt, udskriv "Færdig!"

#Optælling med continue og break
for i in range(10):
 
    if i == 5:
         continue
    elif i ==8:
        break
    print(i)