from Airplane import airplane
from Car import car
from Train import train

Trans_info = {
    'aira_info': {'air1': airplane('Boeing 737-800', 828.0, 1997, 189, 'Jet A-1', 12500),
                  'air2': airplane('Airbus A320', 828.0, 1987, 180, 'Jet A-1', 11900),
                  'air3': airplane('Cessna 172', 226.0, 1955, 4, 'Avgas 100LL', 4115)},

    'car_info': {'car1': car('Toyota Corolla 1.6', 195.0, 2020, 1.6, 'petrol', 'CVT'),
                 'car2': car('BMW M3 Competition', 250.0, 2021, 3.0, 'petrol', 'automatic'),
                 'car3': car('Lada Vesta 1.6', 175.0, 2019, 1.6, 'petrol', 'manual')},
         
    'train_info': {'train1': train('BHP Iron Ore Train', 80.0, 2001, '82,000 t iron ore', 'Diesel-electric', 7353.00),
                   'train2': train('Rhaetian Railway Capricorn', 35.0, 2022, '4,000+ passengers', 'Electric', 1906.00),
                   'train3': train('CRH380BL Hexie', 487.3, 2011, '1,000+ seats', 'Electric', 400.00)}
    }