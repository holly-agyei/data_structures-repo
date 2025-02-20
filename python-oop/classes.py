class Microwave:
    def __init__(self, brand: str, power_rating: str):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False
        
        
    def turn_on(self)->None:
        if self.turned_on:
            print(f"Microwave {self.brand} is already turned on")
        else:
            self.turned_on = True
            print(f"Microwave {self.brand} is now turned on")
            
    def turn_off(self)->None:
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave {self.brand} is turned off")
        else:
            
            print(f"Microwave {self.brand} is already turned off")
    
    def run(self, seconds: int)->None:
        if self.turned_on:
            print(f'running {self.brand} for {seconds} seconds')
        else:
            print("turn on your microwave first!")

    def __str__(self):
        return f"{self.brand} and {self.power_rating}"
    
    def __repr__(self):
        return f"microwave( brand = {self.brand}, power = {self.power_rating})"
        
        
        
                
               
    
smeg = Microwave("smeg", "B")
hotplate: Microwave = Microwave("cooking_microwave", "D")
print(repr(hotplate))


"""
the repr and str dunder methods will always be called when you print the instance. 

the default is the memory of the class!
to call the repr representation, you have to use repr(objectname)
"""



