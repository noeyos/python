class Vehicle:
    def __init__(self):
        self.wheelCount = 2
    
    def flex(self):
        self.wheelCount = 4
        
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.autopilot_level = 1
    
    def hit(self):
        self.autopilot_level += 1
        
if __name__ == '__main__':
    c = Car()
    print(c.wheelCount)
    print(c.autopilot_level)
    c.flex()
    c.hit()
    print(c.wheelCount)
    print(c.autopilot_level)
    
