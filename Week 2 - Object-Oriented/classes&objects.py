# Defining a Class
class Car:
    # Constructor (__init__ method)
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    # Method to start the car
    def start(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model} is now running.")

    # Method to stop the car
    def stop(self):
        self.is_running = False
        print(f"The {self.year} {self.make} {self.model} has stopped.")

    # Method to display car details
    def display_info(self):
        status = "running" if self.is_running else "not running"
        print(f"{self.year} {self.make} {self.model} is currently {status}.")

# Creating Objects
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2020)

# Using Methods
car1.display_info()
car1.start()
car1.display_info()
car1.stop()

car2.display_info()
