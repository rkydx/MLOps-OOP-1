## Multiple Inheritance (Diamond Problem)

# Common base class
class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from A, {self.name}.")

# Intermediate class 1
class B(A):

    def greet(self):
        print(f"Hello from B, {self.name}.")
        super().greet()

# Intermediate class 2
class C(A):
    def greet(self):
        print(f"Hello from C, {self.name}.")
        super().greet()

# Derived class
class D(B, C):

    def greet(self):
        print(f"Hello from D, {self.name}.")
        super().greet()

# Create an instance of D
d = D("Frank")
d.greet()
# Output:
# Hello from D, Frank.
# Hello from B, Frank.
# Hello from C, Frank.
# Hello from A, Frank.