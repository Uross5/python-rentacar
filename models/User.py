from Db import Db


class User(Db):
    def __init__(self):
        super().__init__()
        self.__name = None
        self.__age = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Age must be at least 18 years old")
        self.__age = age
