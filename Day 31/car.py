from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str
    year: int
    fuel: str = "Petrol"


car = Car("BMW", "M3", 2024)

print(car)