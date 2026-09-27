from Transport import transport
class train(transport):
    def __init__(self, model, speed, year, capacity, fuel, train_length):
        self.train_length = train_length
        super().__init__(model, speed, year, capacity, fuel)
    def train_leng(self):
        print(f'maximum train length: {self.train_length}')
trai = train('BHP Iron Ore Train', 80.0, 2001, '82,000 t iron ore', 'Diesel-electric', 7353.00)   


