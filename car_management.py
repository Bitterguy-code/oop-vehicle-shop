class CarManager:
    all_cars = {}
    total_cars = 0

    def __init__(self):
        _id = 0
        _make = ""
        _model = ""
        _year = 0
        _mileage = 0
        _services = []