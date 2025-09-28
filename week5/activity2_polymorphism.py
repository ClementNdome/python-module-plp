# activity2_polymorphism.py
# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        print("This vehicle is moving in a general way.")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing across the water.")


# --- Example Usage ---
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        v.move()   # Each class defines move() differently
