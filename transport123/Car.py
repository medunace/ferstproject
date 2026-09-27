from Transport import transport
class car(transport):
    def __init__(self, model, speed, year, capacity, fuel, fact):
        self.fact = fact    
        super().__init__(model, speed, year, capacity, fuel)
    def car_fact(self):
        print(f'"{self.fact}" number of vehicles leads the market.')
toyota = car('Toyota Corolla 1.6', 195, 2020, 1.6, 'petrol', 'Interesting fact')

