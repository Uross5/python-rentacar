from models.Db import Db


class User(Db):
    all_users = []

    def __init__(self):
        super().__init__()
        self.__name = None
        self.__age = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        split_name = new_name.split()

        if len(split_name) < 2:
            raise ValueError("Name must be in format firs last name")

        self.__name = new_name

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
        connection = self._get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO users(name,age) VALUES(%s,%s)"
        cursor.execute(query, (self.__name, self.__age))
        connection.commit()
        cursor.close()

    def display_users(self):
        connection = self._get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        for user in result:
            print(user)
