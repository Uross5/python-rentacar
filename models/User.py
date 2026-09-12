from Db import Db

class User(Db):
    def __init__(self):
        super().__init__()

    def get_name(self):
        return self.__name

    def set_name(self,name):
        if len(name)<3:
            raise ValueError("Name must be at least 3 characters")
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age<18:
            raise ValueError("Age must be at least 18 years old")
        self.__age=age

