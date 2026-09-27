
from Info import Trans_info

i = True
air_character = ['speed', 'year', 'capacity', 'fuel', 'height']
train_character = ['speed', 'year', 'capacity', 'fuel', 'train_length']
car__character = ['speed', 'year', 'capacity', 'fuel', 'fact']

while i:
    print('the mode of transport you want to find out about')
    print('1 = train')
    print('2 = car')
    print('3 = airplane')
    print('0 = exit')
    a = int(input(''))
    if a == 0:
        i = False
        
    elif a == 1:
        print('Select a model:')
        print('1.', Trans_info['train_info']['train1'].model)
        print('2.', Trans_info['train_info']['train2'].model)
        print('3.', Trans_info['train_info']['train3'].model)
        print('4. "exit"')
        a1 = int(input(''))
        if a1 == 4:
            continue
        elif a1 == 1:
            obj = Trans_info['train_info']['train1']
            print('Enter 1 to view specifications.')
            print('Enter 2 to exit')
            r = int(input(''))
            if r == 1:
                print('Select a characteristic:')
                for ai, key in enumerate(train_character, 1):
                    print(f'{ai}: "{key}"')
                print('0: "exit"')
                
                while True:
                    rr = int(input('Enter the number:')) 
                    if rr == 1:
                        obj.speed_transport()
                    elif rr == 2:
                        obj.year_transport()
                    elif rr == 3:
                        obj.capacity_transport()
                    elif rr == 4:
                        obj.fuel_transport()
                    elif rr == 5:
                        obj.train_leng()
                    elif rr == 0:
                        break
                    else:
                        print('Make a choice.')

            else:
                continue
        elif a1 == 2:
            obj = Trans_info['train_info']['train2']
            print('Enter 1 to view specifications.')
            print('Enter 2 to exit')
            r = int(input(''))
            if r == 1:
                print('Select a characteristic:')
                for ai, key in enumerate(train_character, 1):
                    print(f'{ai}: "{key}"')
                print('0: "exit"')
                
                while True:
                    rr = int(input('Enter the number:')) 
                    if rr == 1:
                        obj.speed_transport()
                    elif rr == 2:
                        obj.year_transport()
                    elif rr == 3:
                        obj.capacity_transport()
                    elif rr == 4:
                        obj.fuel_transport()
                    elif rr == 5:
                        obj.train_leng()
                    elif rr == 0:
                        break
                    else:
                        print('Make a choice.')

            else:
                continue
        elif a1 == 3:
            obj = Trans_info['train_info']['train3']
            print('Enter 1 to view specifications.')
            print('Enter 2 to exit')
            r = int(input(''))
            if r == 1:
                print('Select a characteristic:')
                for ai, key in enumerate(train_character, 1):
                    print(f'{ai}: "{key}"')
                print('0: "exit"')
                
                while True:
                    rr = int(input('Enter the number:')) 
                    if rr == 1:
                        obj.speed_transport()
                    elif rr == 2:
                        obj.year_transport()
                    elif rr == 3:
                        obj.capacity_transport()
                    elif rr == 4:
                        obj.fuel_transport()
                    elif rr == 5:
                        obj.train_leng()
                    elif rr == 0:
                        break
                    else:
                        print('Make a choice.')

            else:
                continue

    elif a == 2:
        print('Select a model:')
        print('1.', Trans_info['car_info']['car1'].model)
        print('2.', Trans_info['car_info']['car2'].model)
        print('3.', Trans_info['car_info']['car3'].model)
        print('4. "exit"')
        a2 = int(input(''))
        if a2 == 4:
            continue
        elif a2 == 1:
            obj = Trans_info['car_info']['car1']
            print('Enter 1 to view specifications.')
            print('Enter 2 to exit')
            r = int(input(''))
            if r == 1:
                print('Select a characteristic:')
                for ai, key in enumerate(car__character, 1):
                    print(f'{ai}: "{key}"')
                print('0: "exit"')
                
                while True:
                    rr = int(input('Enter the number:')) 
                    if rr == 1:
                        obj.speed_transport()
                    elif rr == 2:
                        obj.year_transport()
                    elif rr == 3:
                        obj.capacity_transport()
                    elif rr == 4:
                        obj.fuel_transport()
                    elif rr == 5:
                        obj.car_fact()
                        
                    elif rr == 0:
                        break
                    else:
                        print('Make a choice.')

            else:
                continue
        elif a2 == 2:
            obj = Trans_info['car_info']['car2']
            print('Enter 1 to view specifications.')
            print('Enter 2 to exit')
            r = int(input(''))
            if r == 1:
                print('Select a characteristic:')
                for ai, key in enumerate(car__character, 1):
                    print(f'{ai}: "{key}"')
                print('0: "exit"')
                
                while True:
                    rr = int(input('Enter the number:')) 
                    if rr == 1:
                        obj.speed_transport()
                    elif rr == 2:
                        obj.year_transport()
                    elif rr == 3:
                        obj.capacity_transport()
                    elif rr == 4:
                        obj.fuel_transport()
                    elif rr == 5:
                        obj.car_fact()
                    elif rr == 0:
                        break
                    else:
                        print('Make a choice.')

            else:
                continue
        elif a2 == 3:
            obj = Trans_info['car_info']['car3']
            print('Enter 1 to view specifications.')
            print('Enter 2 to exit')
            r = int(input(''))
            if r == 1:
                print('Select a characteristic:')
                for ai, key in enumerate(car__character, 1):
                    print(f'{ai}: "{key}"')
                print('0: "exit"')
                
                while True:
                    rr = int(input('Enter the number:')) 
                    if rr == 1:
                        obj.speed_transport()
                    elif rr == 2:
                        obj.year_transport()
                    elif rr == 3:
                        obj.capacity_transport()
                    elif rr == 4:
                        obj.fuel_transport()
                    elif rr == 5:
                       obj.car_fact()
                    elif rr == 0:
                        break
                    else:
                        print('Make a choice.')

            else:
                continue

    elif a == 3:
        print('Select a model:')
        print('1.', Trans_info['aira_info']['air1'].model)
        print('2.', Trans_info['aira_info']['air2'].model)
        print('3.', Trans_info['aira_info']['air3'].model)
        print('4. "exit"')
        a3 = int(input(''))
        if a3 == 4:
            continue
        elif a3 == 1:
            obj = Trans_info['aira_info']['air1']
            print('Enter 1 to view specifications.')
            print('Enter 2 to exit')
            r = int(input(''))
            if r == 1:
                print('Select a characteristic:')
                for ai, key in enumerate(air_character, 1):
                    print(f'{ai}: "{key}"')
                print('0: "exit"')
                
                while True:
                    rr = int(input('Enter the number:')) 
                    if rr == 1:
                        obj.speed_transport()
                    elif rr == 2:
                        obj.year_transport()
                    elif rr == 3:
                        obj.capacity_transport()
                    elif rr == 4:
                        obj.fuel_transport()
                    elif rr == 5:
                        obj.height_air()
                        
                    elif rr == 0:
                        break
                    else:
                        print('Make a choice.')

            else:
                continue
        elif a3 == 2:
            obj = Trans_info['aira_info']['air2']
            print('Enter 1 to view specifications.')
            print('Enter 2 to exit')
            r = int(input(''))
            if r == 1:
                print('Select a characteristic:')
                for ai, key in enumerate(air_character, 1):
                    print(f'{ai}: "{key}"')
                print('0: "exit"')
                
                while True:
                    rr = int(input('Enter the number:')) 
                    if rr == 1:
                        obj.speed_transport()
                    elif rr == 2:
                        obj.year_transport()
                    elif rr == 3:
                        obj.capacity_transport()
                    elif rr == 4:
                        obj.fuel_transport()
                    elif rr == 5:
                        obj.height_air()
                    elif rr == 0:
                        break
                    else:
                        print('Make a choice.')

            else:
                continue
        elif a3 == 3:
            obj = Trans_info['aira_info']['air3']
            print('Enter 1 to view specifications.')
            print('Enter 2 to exit')
            r = int(input(''))
            if r == 1:
                print('Select a characteristic:')
                for ai, key in enumerate(air_character, 1):
                    print(f'{ai}: "{key}"')
                print('0: "exit"')
                
                while True:
                    rr = int(input('Enter the number:')) 
                    if rr == 1:
                        obj.speed_transport()
                    elif rr == 2:
                        obj.year_transport()
                    elif rr == 3:
                        obj.capacity_transport()
                    elif rr == 4:
                        obj.fuel_transport()
                    elif rr == 5:
                       obj.height_air()
                    elif rr == 0:
                        break
                    else:
                        print('Make a choice.')

            else:
                continue

        
        

