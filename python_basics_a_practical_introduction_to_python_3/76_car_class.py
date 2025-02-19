class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."
    def drive(self, miles):
        self.mileage = self.mileage + miles
    
blue = Car("blue", 20_000)
red = Car("red", 30_000)

print(blue)
print(red)

blue.drive(100)
print(blue)
