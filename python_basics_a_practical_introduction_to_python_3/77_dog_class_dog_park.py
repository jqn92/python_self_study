class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    def speak(self, sound="Yap"):
        return super().speak(sound)

class Bulldog(Dog):
    def speak(self, sound="Woof"):
        return super().speak(sound)

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)    

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
bobby = GoldenRetriever("Bobby", 2)
