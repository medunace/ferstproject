from Transport import transport
class airplane(transport):
    def __init__(self, model, speed, year, capacity, fuel, height):
        self.height = height
        super().__init__(model, speed, year, capacity, fuel)
    def height_air(self):
        print(f'The aircraft can climb to an altitude: {self.height}')
air = airplane('Boeing 737-800', 828, 1997, 189, 'Jet A-1', 12500)
