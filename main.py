from models.Car import Car
from models.User import User

available_options = [1, 2, 3, 4]

print("Choose one of the following options:")
option = int(input(" 1. Add a user\n 2. Display users\n "
                   "3. Show available cars\n 4. Show occupied cars\n"))

if option not in available_options:
    raise ValueError("Invalid option")

if option == 1:
    user = User()
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    user.name = name
    user.age = age
    user.create_user()

elif option == 2:
    user = User()
    user.display_users()

elif option == 3:
    Car.display_available_cars()

elif option == 4:
    Car.display_occupied_cars()
