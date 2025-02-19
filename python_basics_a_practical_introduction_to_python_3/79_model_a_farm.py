class Animal:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old. It is a {breed}."

    def walk(self):
        return f"{self.name} starts walking."

    def eat(self):
        return f"{self.name} is eating."

    def run(self):
        return f"{self.name} is running."

    def sleep(self):
        return f"{self.name} fell asleep."

    def speak(self, sound):
        return f"{self.name} says: '{sound}'"

    def jump(self):
        return f"{self.name} jumps!"


class Dog(Animal):

    def shepherd(self):
        return f"{self.name} is shepherding the other animals."

    def speak(self, sound="woof"):
        return super().speak(sound)

class Cow(Animal):

    def graze(self):
        return f"{self.name} is grazing some grass."

    def jump(self):
        return f"{self.name} can't really jump."

    def speak(self, sound="moo"):
        return super().speak(sound)

class Pig(Animal):

    def wallow(self):
        return f"{self.name} wallows in the mire."

    def jump(self):
        return f"{self.name} can't really jump."

    def speak(self, sound="Spare me some oats, brother!"):
        return super().speak(sound)

class Hen(Animal):

    def lay(self):
        return f"{self.name} is laying an egg."

    def speak(self, sound="coo"):
        return super().speak(sound)

class Rooster(Animal):

    def crow(self):
        return f"{self.name} is crowing loudly!"

    def speak(self, sound="caw"):
        return super().speak(sound)

class Horse(Animal):

    def speak(self, sound="neigh"):
        return super().speak(sound)

class Sheep(Animal):

    def speak(self, sound="baa"):
        return super().speak(sound)

bobby = Dog("Bobby", 4, "German Sheperd")
poppy = Cow("Poppy", 7, "Aberdeen Angus")
winston = Pig("Winston", 3, "Pinky Boy") 
lily = Hen("Lily", 1, "Whitey")
rocco = Rooster("Rocco", 3, "Welsh Red")
cooper = Horse("Cooper", 9, "Golden Arabian")
barney = Sheep("Barney", 2, "Wooly")
