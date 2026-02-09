class Dog:
    animal = "canine"
    
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    def display_details(self):
        print(f"Details: {self.colour} {self.breed}, a {Dog.animal}")

dog1 = Dog("Labrador", "Yellow")
dog2 = Dog("German Shepherd", "Brown and Black")

dog1.display_details()
dog2.display_details()