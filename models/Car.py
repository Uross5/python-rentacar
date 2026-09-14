from models.Db import Db
from datetime import datetime


class Car(Db):
    allowed_cars = {
        "Audi": [
            {"model": "A4", "production_year": 2004, "rented": True, "rented_until": None},
            {"model": "A5", "production_year": 2003, "rented": False, "rented_until": None},
            {"model": "A6", "production_year": 2002, "rented": False, "rented_until": None}
        ],
        "BMW": [
            {"model": "M3", "production_year": 2008, "rented": False, "rented_until": None},
            {"model": "M5", "production_year": 2010, "rented": False, "rented_until": None},
            {"model": "M8", "production_year": 2019, "rented": True, "rented_until": None}
        ],
        "Mercedes": [
            {"model": "GLK", "production_year": 2015, "rented": False, "rented_until": None},
            {"model": "GLE", "production_year": 2017, "rented": False, "rented_until": None},
            {"model": "GLC", "production_year": 2016, "rented": False, "rented_until": None}
        ]
    }

    def __init__(self):
        super().__init__()
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


    def display_available_cars(self):
        connection=self._get_connection()
        cursor=connection.cursor()
        query="SELECT * FROM cars WHERE rented=FALSE"
        cursor.execute(query)
        cars=cursor.fetchall()
        cursor.close()
        for car in cars:
            print(car)


    def display_occupied_cars(self):
        connection=self._get_connection()
        cursor=connection.cursor()
        query="SELECT * FROM cars WHERE rented= TRUE"
        cursor.execute(query)
        cars=cursor.fetchall()
        cursor.close()
        for car in cars:
            print(car)


    def insert_cars_into_db(self):
        connection=self._get_connection()
        cursor=connection.cursor()
        query="INSERT INTO cars (brand,model,production_year,rented,rented_until)VALUES(%s,%s,%s,%s,%s)"
        for brand in Car.allowed_cars:
            for car in Car.allowed_cars[brand]:
                cursor.execute(query,(brand,car["model"],car["production_year"],car["rented"],car["rented_until"]))
        connection.commit()
        cursor.close()

    def get_available_car_by_id(self,car_id):
        connection=self._get_connection()
        cursor=connection.cursor()
        query="SELECT * FROM cars WHERE id=%s and rented=FALSE"
        cursor.execute(query,(car_id,))
        car=cursor.fetchone()
        cursor.close()
        if car is None:
            raise ValueError("Car does not exist or is not available")
        return car

    @staticmethod
    def validate_rental_date(rented_until_date):
        if rented_until_date <= datetime.now():
            raise ValueError("Rental end date must be in the future")

    def rent_car(self,car_id,rented_until_date):
        connection=self._get_connection()
        cursor=connection.cursor()
        query="UPDATE cars SET rented=TRUE, rented_until=%s WHERE id=%s"
        cursor.execute(query,(rented_until_date,car_id))
        connection.commit()
        cursor.close()


    # def rent_car(self):
    #     connection=self._get_connection()
    #     cursor=connection.cursor()
    #     query
