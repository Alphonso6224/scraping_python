class Vehicule:
    def __init__ (self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    
    def start(self):
        self.started = True
        print("Car started, let's ride!")
        
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vroooom!')
        else:
            print("You need to start the car first")
            
    def stop(self):
        self.speed = 0
        print('Halting')
        
        
class Car(Vehicule):
    trunk_open = False
    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False

class Motorcycle(Vehicule):
    def __init__ (self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()
    def start (self):
        print("Désolé, plus de carburant!")