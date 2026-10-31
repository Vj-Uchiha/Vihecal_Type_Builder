
# Vehicle Inheritance Program

# PART 1: Create the Parent Class
class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    # PART 2: Display vehicle details
    def show_details(self):
        print("Brand:", self.brand)
        print("Maximum Speed:", self.max_speed, "km/h")


# PART 3: Create the Child Class
class Car(Vehicle):

    # PART 4: Add car-specific details
    def __init__(self, brand, max_speed, model, seats):
        super().__init__(brand, max_speed)
        self.model = model
        self.seats = seats

    # PART 5: Override the parent method
    def show_details(self):
        print("Car Model:", self.model)
        print("Number of Seats:", self.seats)
        super().show_details()

    # PART 6: Add a child-only method
    def fuel_type(self):
        print("Fuel Type: Petrol")


# PART 7: Create and test the object
my_car = Car("Toyota", 180, "Fortuner", 7)

print("===== CAR DETAILS =====")
my_car.show_details()

print("\n===== FUEL INFORMATION =====")
my_car.fuel_type()


# PART 8: Check inheritance
print("\nIs Car a subclass of Vehicle?")
print(issubclass(Car, Vehicle))
