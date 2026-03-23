# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        # Generic method to be overridden by child classes.
        return "I make a sound"
    
# Child Class 1
class Dog(Animal):
    def speak(self):
        # Override the speak method for Dog.
        return f"{self.name} says Woof!"
    
# Child Class 2
class Cat(Animal):
    def speak(self):
        # Override the speak method for Cat.
        return f"{self.name} says Meow!"
    
# Using the Classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())