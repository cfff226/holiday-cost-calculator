import math

# Program which calculates the total cost of a holiday for a user

list_of_cities = ["berlin", "amsterdam", "zurich", "paris", "budapest: "]

plane_cost = [89, 65, 110, 95, 87]

daily_car_rental = [39, 45, 86, 98, 72]

# Request the city choice from the user
while True:
    print("\n\t\t\tWelcome to Yourtrip!")
    city_flight = input(
        "\nPlease type either 'Berlin', 'Amsterdam', 'Zurich', 'Paris' or 'Budapest": 
    )
    if city_flight.lower() not in list_of_cities:
        print("You have entered incorrectly")
        continue
    else:
        city_flight = city_flight.capitalize()
        print(f"\nGreat, you have chosen to fly to {city_flight}")
        break

# Function which requests the number of nights that the user would like to book a hotel for
def number_of_nights():
    num_nights = input("\nPlease input the number of nights that you wish to stay: \n")
    try:
        num_nights = int(num_nights)
        if num_nights <= 0:
            num_nights = 0
            print("You have chosen not to book a hotel")
    except ValueError:
        print("You have entered incorrectly")
        number_of_nights()
    
    return num_nights

number_of_nights()

# Function which requests the number of says that the user would like to rent a car for
def car_rental_days():
    rental_days = input(
        "\nPlease input the number of days that you would like to hire a car for: \n"
    )
    try:
        rental_days = int(rental_days)
        if rental_days <= 0:
            rental_days = 0
            print("You have chosen not to rent a car")