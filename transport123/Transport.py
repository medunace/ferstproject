class transport:
    def __init__(self, model, speed, year, capacity, fuel):
        self.model = model
        self.speed = speed
        self.year = year
        self.capacity = capacity
        self.fuel = fuel
        
    def model_transport(self):
        print(f'model of this transport: """{self.model}"""')

    def speed_transport(self):
        print(f'Acceleration rate: "{self.speed}"')

    def year_transport(self):
        print(f'year of manufacture: "{self.year}"')

    def capacity_transport(self):
        print(f' capacity: "{self.capacity}"')

    def fuel_transport(self):
        print(f'fuel used: "{self.fuel}"')
    