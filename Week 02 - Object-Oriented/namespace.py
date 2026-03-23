class Employee:
    # Class attribute (shard across all objects)
    company_name = "Tech Corp"

    def __init__(self, name, role):
        # Instance attributes (unique to each object)
        self.name = name
        self.role = role

    def display_info(self):
        # Instance method to display employee details.
        print(f"Name: {self.name}, Role: {self.role}, Company: {self.company_name}")

    @classmethod
    def set_company_name(cls, name):
        # Class method to modify the class attribute.
        cls.company_name = name
    
    @staticmethod
    def company_policy():
        # Static method (not dependent on instance or  class).
        return "All employee must adhere to company policies."
    
# Accessing class namespace
print("Initial Company Name:", Employee.company_name)

# Creating objects (instance namespace)
employee1 = Employee("Alice", "Engineer")
employee2 = Employee("Bob", "Manager")

# Displaying individual employee details
employee1.display_info()
employee2.display_info()

# Modifying the class attribute using a class method
Employee.set_company_name("Tech Solutions")
employee1.display_info()
employee2.display_info()

# Accessing static method
print("Company Policy:", Employee.company_policy())

# Adding a dynamic attribute to an object (instance namespace)
employee1.salary = 80000
print(f"{employee1.name}'s Salary: {employee1.salary}")