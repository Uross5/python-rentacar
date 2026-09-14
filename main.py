from models.Car import Car
from models.User import User
from datetime import datetime


available_options = [1, 2, 3, 4, 5, 6]

while True:

    print("Choose one of the following options:")
    option = int(input(" 1. Add a user\n 2. Display users\n "
                       "3. Show available cars\n 4. Show occupied cars\n "
                       "5. Rent a car\n 6. Exit\n"))

    if option not in available_options:
        print("Invalid option. Please choose one of the following options:")
        continue

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
        car=Car()
        car.display_available_cars()


    elif option == 4:
        car=Car()
        car.display_occupied_cars()


    elif option == 5:
        car=Car()
        car.display_available_cars()
        car_id=int(input("Enter your car id: "))
        car.get_available_car_by_id(car_id)
        user_rent_until=input("Until when would you like to rent your car? Please use format YYYY-MM-DD HH:MM:SS\n" )
        rented_until_date=datetime.strptime(user_rent_until,"%Y-%m-%d %H:%M:%S")
        car.validate_rental_date(rented_until_date)
        car.rent_car(car_id,rented_until_date)

    elif option == 6:
        print("Thank you for your time, see you soon!")
        break





