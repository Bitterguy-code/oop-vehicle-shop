class CarManager:
    all_cars = {}
    total_cars = 0

    def __init__(self,id,make,model,year,mileage,services):
        self._id = id
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services

    def __repr__(self):
        return f"{str(self._id)}: {str(self._make)}, {str(self._model)}"

def main():
    running = True
    while running:
        running = menu()

def menu():
    selection = input('''
        ----  WELCOME  ----
        1. Add a car
        2. View all cars
        3. View total number of cars
        4. See a car's details
        5. Service a car
        6. Update mileage
        7. Quit
        ```
    ''')

    match int(selection):
        case 1: #add a car
            add_car()
            return True
        case 2:#view all cars
            view_all()
            return True
        case 3: #view total number of cars
            pass
        case 4: #see a car's details
            pass
        case 5: #service a car
            pass
        case 6: #update milage
            pass
        case 7: #quit
            return False
        case _:
            print("Please enter a valid selection")


def add_car():
    car_id = input("ID: ")
    car_make = input("Make: ")
    car_model = input("Model: ")
    car_year = input("Year: ")
    car_mileage = input("Mileage: ")
    car_services = input("Services seperated by commas: ").split(',')

    CarManager.all_cars[car_id] = CarManager(car_id, car_make, car_model, car_year, car_mileage,car_services)

def view_all():
    for key in CarManager.all_cars:
     print(CarManager.all_cars[key])

main()