# activity1_class_design.py
# Assignment 1: Design Your Own Class

class Device:
    """Base class representing a generic device."""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is powering on...")

    def power_off(self):
        print(f"{self.brand} {self.model} is shutting down...")


class Smartphone(Device):  # Inherits from Device
    """Child class representing a smartphone."""
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)   # Call the parent constructor
        self.os = os
        self.storage = storage

    def install_app(self, app_name):
        print(f"📱 Installing {app_name} on {self.brand} {self.model}...")

    def specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, OS: {self.os}, Storage: {self.storage}GB")


# --- Example Usage ---
if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 15", "iOS", 256)
    phone2 = Smartphone("Samsung", "Galaxy S24", "Android", 512)

    phone1.power_on()
    phone1.specs()
    phone1.install_app("Spotify")

    print()
    phone2.power_on()
    phone2.specs()
    phone2.install_app("Google Maps")
    phone2.power_off()
