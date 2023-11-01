class Computer(object):
    def __init__(self):
        self.ram = '8gb'
        self.storage = '225gb'
        print("im in computer class:")
        
class Mobile(Computer):
    def __init__(self):
        super().__init__()
        self.model = 'iphone X' 
        print("im in mobile constructor:")
        
        
c1 = Mobile()
print(c1. __dict__)               
        