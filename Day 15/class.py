class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("BMW", "M3")
car2 = Car("Audi", "A4")

print(car1.brand, car1.model)
print(car2.brand, car2.model)