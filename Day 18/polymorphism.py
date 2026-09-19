class Vehicle:
    def move(self):
        print("Vehicle is driven")

class Car:
    def move(self):
        print("Car is driving")

class Bike:
    def move(self):
        print("Bike is driving")

car = Car()
bike = Bike()

car.move()
bike.move()