# Simple inheritance

# # Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# # Derived class
class Dog(Animal):

    def speak(self):
        print(f"{self.name} barks.")

# # Create an instance of Animal
animal = Animal("Generic Animal")
animal.speak()  # Output: Generic Animal makes a sound.

# # # Create an instance of Dog
dog = Dog('Buddy')
dog.speak()  # Output: Buddy barks. He is very Friendly.         # it will override the speak method of base class if the derived class has the same method name
