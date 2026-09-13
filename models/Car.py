class Car:
    allowed_cars = {
        "Audi": [
            {"model": "A4", "production_year": 2004, "rented":True,"rented_until":None},
            {"model": "A5", "production_year": 2003, "rented":False,"rented_until":None},
            {"model": "A6", "production_year": 2002, "rented":False,"rented_until":None}
        ],
        "BMW": [
            {"model": "M3", "production_year": 2008, "rented":False,"rented_until":None},
            {"model": "M5", "production_year": 2010, "rented":False,"rented_until":None},
            {"model": "M8", "production_year": 2019, "rented":True,"rented_until":None}
        ],
        "Mercedes": [
            {"model": "GLK", "production_year": 2015, "rented":False,"rented_until":None},
            {"model": "GLE", "production_year": 2017, "rented":False,"rented_until":None},
            {"model": "GLC", "production_year": 2016, "rented":False,"rented_until":None}
        ]
    }

    def __init__(self):
        self.__brand = None
        self.__model = None
        self.__production_year = None

    # Getter
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__brand is None:
            raise ValueError("set the brand first")
        valid_models = Car.allowed_cars[self.__brand]
        for car in valid_models:
            if model == car["model"]:
                self.__model = model
                self.__production_year = car["production_year"]
                return

        raise ValueError("model not allowed")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if brand not in Car.allowed_cars:
            raise ValueError("Invalid brand")
        self.__brand = brand

    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self, year):
        if self.__production_year is None:
            raise ValueError("Invalid production year")
        if self.__model is not None and self.__brand is not None:
            raise ValueError("Production year cannot be set")
        self.__production_year = year

    @classmethod
    def display_available_cars(cls):
        for brand in Car.allowed_cars:
            cars = Car.allowed_cars[brand]
            for car in cars:
                if car["rented"] == False:
                    print(f"{brand} {car['model']} ({car['production_year']})")

    @classmethod
    def display_occupied_cars(cls):
        for brand in Car.allowed_cars:
            cars = Car.allowed_cars[brand]
            for car in cars:
                if car["rented"] == True:
                    print(f"{brand} {car['model']} ({car['production_year']})")




