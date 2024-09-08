from vehicle import Vehicle

class Car(Vehicle):
    
    def __init__(self, make, model, doornum):
        super().__init__(make, model)
        self.doornum = doornum

    def details(self):
        return f'the vehicles make is {self.make} with model {self.model} it has {self.doornum} doors'
    

mycar = Car('camry', '417', 67)

print(mycar.details())