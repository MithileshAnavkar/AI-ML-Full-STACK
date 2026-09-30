class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


car1 = Car("BMW", "M4", 2024)

print("Brand:", car1.brand)
print("Model:", car1.model)
print("Year:", car1.year)