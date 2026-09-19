class Laptop:
    category = "Electronics"

    def __init__(self , brand , price ,ram):
        self.brand = brand
        self.price = price
        self.ram = ram

laptop1 = Laptop("Lenovo" , 800000 , "8GB")
laptop2 = Laptop("Dell" ,  90000 , "16GB")

print(laptop1.brand , laptop1.price , laptop1.ram , laptop1.category)
print(laptop2.brand , laptop2.price , laptop2.ram)