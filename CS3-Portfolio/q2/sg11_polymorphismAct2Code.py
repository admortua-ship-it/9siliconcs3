## Created Class Definitions for Car, Boat, and Drone

class Car:
    def move(self):
        print("The car drives on the road.")

    def start_trip(self, vehicle):
        vehicle = self
        vehicle.move()

class Boat:
    def move(self):
        print("The boat sails on water.")

    def start_trip(self, vehicle):
        vehicle = self
        vehicle.move()

class Drone:
    def move(self):
        print("The drone flies in the sky.")

    def start_trip(self, vehicle):
        vehicle = self
        vehicle.move()

# Create instances of Car, Boat, and Drone and demonstrate polymorphism
car = Car()
boat = Boat()
drone = Drone()

# Demonstrate polymorphism by calling the start_trip method for each vehicle
car.start_trip(car)
boat.start_trip(boat)
drone.start_trip(drone)