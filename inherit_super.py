# Simple inheritance

# # Base class (parent class)
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# # Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()                                      # Call the constructor of the base class (ie parent class) to initialize inherited attributes
        self.breed = breed

    def speak(self):
        super().speak()                                          # Call the speak method of the base class (ie parent class)
        print(f"{self.name} barks. It is a {self.breed}.")
        #print(f"{self.name} barks. It is a wonderful.")


# # # Create an instance of Dog
#dog = Dog('Buddy')
dog = Dog("Golden Retriever")
dog.speak()  # Output: Buddy barks. It is a Golden Retriever.    # it will override the speak method of base class if the derived class has the same method name
