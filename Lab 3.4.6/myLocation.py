# Визначення класу Location
class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# Перший екземпляр класу Location
loc1 = Location("Tomas", "Portugal")
loc1.myLocation()

# Другий екземпляр класу Location
loc2 = Location("Ying", "China")
loc2.myLocation()

# Третій екземпляр класу Location
loc3 = Location("Amare", "Kenya")
loc3.myLocation()

# Четвертий екземпляр класу Location
your_loc = Location("John", "France")
your_loc.myLocation()
