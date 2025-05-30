import math

def car_model(choice):
    if choice == 1:
        model = 206
        modelname = "206 and 207"
    elif choice == 2:
        model = 55
        modelname = "Changan CS55+ Ba Esalat"

    return model, modelname

def variables():
    last_maintenance: {
    "last_engine_oil" : 0,
    "last_airfilter" : 0,
    "last_cabin_airfilter" : 0,
    "last_gasfilter" : 0,
    "last_engine_sparkplug" : 0,
    "last_brake_oil" : 0,
    "last_timebelt" : 0,
    "last_manualgearbox_oil" : 0
    }
    return last_maintenance

def change_intervals206():
    change_interval206 = {
    "engine_oil_interval206" : 10000,
    "airfilter_interval206" : 10000,
    "cabin_airfilter_interval206" : 10000,
    "gasfilter_interval206" : 10000,
    "engine_sparkplug_interval206" : 20000,
    "brake_oil_interval206" : 40000,
    "timebelt_interval206" : 80000,
    "manualgearbox_oil_interval206" : 40000
    }
    return change_interval206

def checkf(check):
    match check:
        case 1:
            if mileage > (last_engine_oil + engine_oil_interval206):
                print("You should Change it!")

def main():
    variables()
    print("Welcome to Car Maintenance Tracker\n")
    print("supported car models:\n 1. Peugeot 206\n 2. Changan CS55+\n")
    choice = int(input("Enter your choice: "))
    model, modelname = car_model(choice)
    print(f'selected car model: {modelname}\n')
    if choice == 1:
        change_intervals206()

    mileage = int(input("Enter Car's mileage(In KM): "))

    print("which one do you want to check?\n 1. engine oil\n 2. air filter\n 3. cabin air filter\n 4. gas filter")
    print(" 5. engine_sparkplug\n 6. brake_oil\n 7. time belt\n 8. manual gearbox")
    check = int(input("Enter your choice: "))
    checkf(check, mileage, last_maintenance, change_interval206)



if __name__ == '__main__':
    main()