class Car:
    def __init__(self, brand,model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand + " ! "

    def full_name(self):
        return f"{self.__brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"
#we can make things private by simply putting __ in front of the attribute so now we will not able to access it outside class
#for accessing we need to use getter function this is encapsulation

class ElectricCar(Car): # this is inheritance
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
# __init__ this is the constructor
# self is the this method
    def fuel_type(self):
        return "Charge"
    
my_tesla = ElectricCar("Tesla","Model S","85KWh")

# print(my_tesla.model)

# print(my_tesla.get_brand())

print(my_tesla.fuel_type())
safari = Car("Tata","Safari")
print(safari.fuel_type())
# my_car = Car("Toyata","Fortuner")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

