
#Klasse med bil information
class Bil:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def beskrivelse(self):
        return f"Dette er en {self.brand}, moddel {self.model}, årgang {self.year}"
    
    def start_bilen(self):
        
        return "Bilen er startet"

bil_1 = Bil("Ford", "Mustang", "2020")

print(bil_1.beskrivelse())
print(bil_1.start_bilen())