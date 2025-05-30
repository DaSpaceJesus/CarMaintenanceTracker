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
    last_maintenance= {
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

def checkf(check, mileage, last_maintenance, change_interval206):
    match check:
        case 1:
            last = last_maintenance["last_engine_oil"]
            interval = change_interval206["engine_oil_interval206"]

        case 2:
            last = last_maintenance["last_airfilter"]
            interval = change_interval206["airfilter_interval206"]

        case 3:
            last = last_maintenance["last_cabin_airfilter"]
            interval = change_interval206["cabin_airfilter_interval206"]

        case 4:
            last = last_maintenance["last_gasfilter"]
            interval = change_interval206["gasfilter_interval206"]

        case 5:
            last = last_maintenance["last_engine_sparkplug"]
            interval = change_interval206["engine_sparkplug_interval206"]

        case 6:
            last = last_maintenance["last_brake_oil"]
            interval = change_interval206["brake_oil_interval206"]

        case 7:
            last = last_maintenance["last_timebelt"]
            interval = change_interval206["timebelt_interval206"]

        case 8:
            last = last_maintenance["last_manualgearbox_oil"]
            interval = change_interval206["manualgearbox_oil_interval206"]

    if mileage > (last + interval):
        print("You should Change it!")
    else:
        print("You're fine now!")


def updatef(update, mileage):
    match update:
        case 1:
            last_maintenance["last_engine_oil"] : mileage

        case 2:
            last_maintenance["last_airfilter"] : mileage

        case 3:
            last_maintenance["last_cabin_airfilter"] : mileage

        case 4:
            last_maintenance["last_gasfilter"]: mileage

        case 5:
            last_maintenance["last_engine_sparkplug"] : mileage

        case 6:
            last_maintenance["last_brake_oil"]: mileage

        case 7:
            last_maintenance["last_timebelt"]: mileage

        case 8:
            last_maintenance["last_manualgearbox_oil"]: mileage






def main():
    last_maintenance = variables()
    print("Welcome to Car Maintenance Tracker\n")
    print("supported car models:\n 1. Peugeot 206/207\n 2. Changan CS55+\n")
    choice = int(input("Enter your choice: "))
    model, modelname = car_model(choice)
    print(f'selected car model: {modelname}\n')
    if choice == 1:
        change_interval206 = change_intervals206()

    do =input("Do you want to\n 1. Check\n or\n 2. Update last maintenance?")
    if do == "1":
        mileage = int(input("Enter Car's mileage(In KM): "))

        print("which one do you want to check?\n 1. engine oil\n 2. air filter\n 3. cabin air filter\n 4. gas filter")
        print(" 5. engine_sparkplug\n 6. brake_oil\n 7. time belt\n 8. manual gearbox")
        check = int(input("Enter your choice: "))
        checkf(check, mileage, last_maintenance, change_interval206)
    elif do == "2":
        print("which one do you want to update?\n 1. engine oil\n 2. air filter\n 3. cabin air filter\n 4. gas filter")
        print(" 5. engine_sparkplug\n 6. brake_oil\n 7. time belt\n 8. manual gearbox")
        update = int(input("Enter your choice: "))
        mileage = int(input("Enter Car's update mileage(In KM): "))
        updatef(update, mileage)





if __name__ == '__main__':
    main()