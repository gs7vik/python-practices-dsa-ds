class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name} from the Parent class.")

class Child(Parent):
    def __init__(self, name, age):
        # Use super to call the Parent class's __init__ method
        super().__init__(name)
        self.age = age

    def greet(self):
        # Use super to call the Parent class's greet method
        super().greet()
        print(f"I am {self.age} years old from the Child class.")

# Example usage
child = Child("Alice", 10)
child.greet()

class Parent2:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, I am {self.name} from the Parent2 class.")
        
class Child2(Parent2):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def greet(self):
        