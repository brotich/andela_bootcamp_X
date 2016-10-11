

class Car(object):
    """
        Car class that can be used to instantiate various vehicles.
        It takes in arguments that depict the type, model, and name of the vehicle 
    """

    def __init__(self,  name = "General", model = "GM", car_type = "saloon"):

        num_of_wheels = 4
        num_of_doors  = 4

        if car_type == "trailer":
            num_of_wheels = 8

        if name == "Porshe" or name == "Koenigsegg":
            num_of_doors = 2
    
        self.name = name
        self.model = model
        self.type = car_type
        self.num_of_doors  = num_of_doors
        self.num_of_wheels = num_of_wheels 
        self.speed = 0
   
    def drive(self, gear):
     
        if self.type == "trailer":
            self.speed = gear * 77 / 7
        elif self.type == "saloon":
            self.speed = gear * 1000 / 3

        return self

    def is_saloon(self):
        return self.type == 'saloon'
