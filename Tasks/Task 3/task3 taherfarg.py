class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show_capacity(self, capacity):
        print("The capacity of the vehicle is: ", capacity)

vehicle = Vehicle("Car", 120, 20)
print(vehicle.name)
print(vehicle.max_speed)
print(vehicle.mileage)
vehicle.show_capacity(5)

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, bus_type):
        super().__init__(name, max_speed, mileage)
        self.bus_type = bus_type

bus = Bus("School Bus", 90, 15, "School")
print(bus.name)
print(bus.max_speed)
print(bus.mileage)
print(bus.bus_type)
bus.show_capacity(40)

class Driver:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience
        
    def driver_id(self, id):
        return f"Driver Name: {self.name}, Driver ID: {id}"

driver = Driver("John Doe", 40, 15)
print(driver.name)
print(driver.age)
print(driver.experience)
print(driver.driver_id(12345))

class BusDriver(Vehicle, Driver):
    def __init__(self, name, max_speed, mileage, bus_type, age, experience, bus_id):
        Vehicle.__init__(self, name, max_speed, mileage)
        Driver.__init__(self, name, age, experience)
        self.bus_id = bus_id

bus_driver = BusDriver("Jane Doe", 90, 15, "School", 35, 10, 101)
print(bus_driver.name)
print(bus_driver.age)
print(bus_driver.experience)
print(bus_driver.bus_id)
print(bus_driver.driver_id(67890))
