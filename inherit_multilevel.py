## Multilevel Inheritance

# Base class (Grandparent class)
class Grandparent:
    def __init__(self, name):
        self.name = name

    def tell_story(self):
        print(f"{self.name} tells a story.")

# Intermediate class (Parent class)
class Parent(Grandparent):

    def work(self):
        print(f"{self.name} is working.")

# Derived class (Child class)
class Child(Parent):

    def play(self):
        print(f"{self.name} is playing.")

# Create an instance of Child
child = Child("Charlie")
child.tell_story()  # Output: Charlie tells a story.
child.work()        # Output: Charlie is working.
child.play()        # Output: Charlie is playing.