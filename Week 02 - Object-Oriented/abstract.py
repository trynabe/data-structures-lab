# Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def details(self):
        return f"Vehicle: {self.brand} {self.model}"
    
# Intermediate Class
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def details(self):
        return f"Car: {self.brand} {self.model}, Doors: {self.doors}"
    
# Child Class
class ElectricCar(Car):
    def __init__(self, brand, model, doors, battery_capacity):
        super().__init__(brand, model, doors)
        self.battery_capacity = battery_capacity

    def details(self):
        return f"Electric Car: {self.brand} {self.model}, Doors: {self.doors}, Battery: {self.battery_capacity} kWh"
    
# Using the Classes
vehicle = Vehicle("Generic", "ModelX")
car = Car("Toyota", "Camry", 4)
electric_car = ElectricCar("Tesla", "Model S", 4, 100)

print(vehicle.details())
print(car.details())
print(electric_car.details())