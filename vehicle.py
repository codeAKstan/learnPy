class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def details(self):
        return f'the vehicles make is {self.make} with model {self.model}'
    
    