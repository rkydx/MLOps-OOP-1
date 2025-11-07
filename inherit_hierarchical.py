## Hierarchical Inheritance

# Base class
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Derived class 1
class Child1(Parent):

    def play(self):
        print(f"{self.name} is playing.")

# Derived class 2
class Child2(Parent):

    def study(self):
        print(f"{self.name} is studying.")

# Create instances of Child1 and Child2
child1 = Child1("Dave")
child2 = Child2("Eve")

child1.greet()  # Output: Hello, my name is Dave.
child1.play()   # Output: Dave is playing.

child2.greet()  # Output: Hello, my name is Eve.
child2.study()  # Output: Eve is studying.