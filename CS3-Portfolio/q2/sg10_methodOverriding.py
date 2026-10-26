# Creating superclass Animal and subclasses Lion, Elephant, and Monkey

class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def get_name(self):
        return self._name

    def eat(self):
        return f"{self.get_name} is eating."

    def make_sound(self):
        return f"{self.get_name} makes a sound."

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.get_name} roars loudly!"

    def eat(self):
        return f"{self.get_name} eats fresh meat."

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.get_name} trumpets!"

    def eat(self):
        return f"{self.get_name} eats grass and fruits."

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.get_name} chatters!"

    def eat(self):
        return f"{self.get_name} eats bananas."

# Creating example objects

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

# Demonstrating method overriding

print(lion.make_sound())  # Output: Simba roars loudly!
print(lion.eat())  # Output: Simba eats fresh meat. 
print("-----")

print(elephant.make_sound())  # Output: Dumbo trumpets!
print(elephant.eat())  # Output: Dumbo eats grass and fruits.
print("-----")

print(monkey.make_sound())  # Output: George chatters!
print(monkey.eat())  # Output: George eats bananas.
print("-----")

# Test Results

"""
Simba roars loudly!
Simba eats fresh meat.
-----
Dumbo trumpets!
Dumbo eats grass and fruits.
-----
George chatters!
George eats bananas.
-----
"""