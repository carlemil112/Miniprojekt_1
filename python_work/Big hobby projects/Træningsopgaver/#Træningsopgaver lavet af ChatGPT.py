#Træningsopgaver lavet af ChatGPT

#TÆL VOKALER I EN STRING

def vowel_counter(string):
    vowels=["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    

    count = 0

    for char in string:
        if char in vowels:
            count += 1 

    return count
    
user_input = input("Indtast en sætning")

vowel_count=vowel_counter(user_input)

#f-string så en kode kan være i sætningen:
print(f"Antallet af vokaler i sætningen er {vowel_count}")
    