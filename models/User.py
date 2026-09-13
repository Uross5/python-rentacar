from models.Db import Db

class User(Db):

    all_users=[]

    def __init__(self):
        super().__init__()
        self.__name = None
        self.__age = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        split_name=newName.split()

        if len(split_name)<2:
            raise ValueError("Name must be in format firs last name")

        self.__name = newName

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Age must be at least 18 years old")
        self.__age = age

    def create_user(self):
        if self.__name is None or self.__age is None:
            raise ValueError("Name and age cannot be None")

        User.all_users.append([self.__name,self.__age])

