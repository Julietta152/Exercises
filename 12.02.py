class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def description(self):
        return f"The {self.color} car has {self.mileage} miles"

blue = Car("Blue", 20000)
blue.description()
print(blue.description())

red = Car("Red", 30000)
red.description()
print(red.description())
