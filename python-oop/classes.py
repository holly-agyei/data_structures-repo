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
               
    
smeg: Microwave = Microwave("smeg", "B")



