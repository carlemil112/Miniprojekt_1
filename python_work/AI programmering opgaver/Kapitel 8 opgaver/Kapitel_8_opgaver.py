#8-1 Definer en besked, uden parameter
def display_message():
    """Viser hvad jeg har lært indtil nu"""
    print("Jeg har lært at man kan definere funktioner, og så ud fra det anvende dem senere i koden, med nye værdier, så mange gange som man vil.")

display_message()

#8-2 Definer med parameter
def favorite_book(bog):
    """Skriv alle mine yndlingsbøger"""
    print(f"En af mine yndlingsbøger er {bog}!")

favorite_book('usårlig')
favorite_book('never finished')


#8-3 Call function med positional arguments OG keyword arguments
def make_shirt(size="L", text="I love Python!"):
    """Skriv trøje str. samt tekst"""
    print(f"Størrelsen er: {size}")
    print(f"Print på trøjen: {text}")

make_shirt('M', 'God mand')

make_shirt(text="Hvaså der mand", size= "L")

#8-4 Default message (Ændret call function ovenfor til at have =L og =I love python som standard:)

make_shirt()


#8-6 City Names function

# Define the function city_country
def city_country(city, country):
    return f"{city}, {country}"

# Call the function with three city-country pairs and print the results
print(city_country('Santiago', 'Chile'))
print(city_country('Tokyo', 'Japan'))
print(city_country('Berlin', 'Germany'))


#8-7 Album function
def make_album(artist, title, num=None): #Hvis der ikke indtastes antal sange "num" ignoreres dette parameter
    album = {'artist': artist, 'title': title}
    if num:
        album['num'] = num
    return album

while True: #While loop der lader brugeren selv indtaste 
    print("\nEnter artist and album title:")
    print("(enter 'q' to quit at any time")

    user_album = input("Album") #definerer input til album
    if user_album == 'q': #skriver man q lukker programmet
        break

    user_artist = input("Artist") #definerer input til artist
    if user_artist == 'q':
        break

    bruger_album_artist = make_album(user_album, user_artist)
    print(f"\nDin artist er {user_artist}, med albummet {user_album}")

print(make_album('Kanye West', 'The College Dropout'))
print(make_album('Lil Uzi Vert', 'Pink Tape', 17))