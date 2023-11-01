class Vehical:
    def __init__(self,name,colour,prize):
        self.name = name
        self.colour = colour
        self.prize = prize
    
    def get_details(self):
        print(f"the name is {self.name}")
        print(f"the colour is {self.colour}")
        print(f"the prize is {self.prize}")
        
    def max_speed(self):
        print("max speed is 110")
        
    def gear(self):
        print("the gear is 6")
        
class car(Vehical):
    def max_speed(self):
        print("max speed is 150")
        
    def gear(self):
        print("the gear is 7") 
        
v1 = Vehical('truck','red',70000)
    
v1.max_speed()

c1 = car('audi','white',4000000)
c1.max_speed()
