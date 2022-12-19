class Vehicle:
    def __init__(self, brand, model, color, maxSpeed):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxSpeed = maxSpeed

    def start(self):
        msg = f"Vehicle has started its engine."
        return msg
    
    def stop(self):
        msg = f"Vehicle has stopped."
        return msg
    
    def turnLeft(self):
        msg = f"Vehicle is turning left."
        return msg

    def turnRight(self):
        msg = f"Vehicle is turning right."

class Truck(Vehicle):
    def __init__(self, brand, model, color, maxSpeed, loadCapacity):
        super().__init__(brand, model, color, maxSpeed,)
        self.loadCapacity = loadCapacity
    
    def load(self):
        msg = f"Loading cargo... Maximum capacity is {self.loadCapacity}"

truck = Truck('Scania', 'Cargo Truck', 'Red', 100, '100 Tonnes')
print(truck.load())
