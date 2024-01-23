import math

# Program which calculates the total cost of a holiday for a user

list_of_cities = ["berlin", "amsterdam", "zurich", "paris", "budapest: "]

plane_cost = [89, 65, 110, 95, 87]

daily_car_rental = [39, 45, 86, 98, 72]

daily_hotel_cost = [78, 82, 125, 110, 90]

# Request the city choice from the user
while True:
    print("\n\t\t\tWelcome to Yourtrip!")
    city_flight = input(
        "\nPlease type either 'Berlin', 'Amsterdam', 'Zurich', 'Paris' or 'Budapest: "
    )
    if city_flight.lower() not in list_of_cities:
        print("You have entered incorrectly")
        continue
    else:
        print(f"\nGreat, you have chosen to fly to {city_flight.capitalize()}")
        break


# Function which requests the number of nights that the user would like to book a hotel for
def number_of_nights():
    num_nights = input("\nPlease input the number of nights that you wish to stay: ")
    try:
        num_nights = int(num_nights)
        if num_nights <= 0:
            num_nights = 0
            print("You have chosen not to book a hotel")
            return num_nights
        else:
            return num_nights
    except ValueError:
        print("You have entered incorrectly")
        number_of_nights()


num_nights = number_of_nights()


# Function which requests the number of says that the user would like to rent a car for
def car_rental_days():
    rental_days = input(
        "\nPlease input the number of days that you would like to hire a car for: "
    )
    try:
        rental_days = int(rental_days)
        if rental_days <= 0:
            rental_days = 0
            print("You have chosen not to rent a car")
            return rental_days
        else:
            return rental_days
    except ValueError:
        print("You have entered incorrectly")
        car_rental_days()


rental_days = car_rental_days()


# Function which calculates the cost of the hotel per night and outputs to the user
def hotel_cost(num_nights, daily_hotel_cost, list_of_cities, city_flight):
    index = list_of_cities.index(city_flight)
    daily_hotel_cost = daily_hotel_cost[index]
    hotel_total = daily_hotel_cost * num_nights
    print(
        f"\nThe total cost of the hotel in {list_of_cities[index].capitalize()} would be £{hotel_total}"
    )


hotel_cost(num_nights, daily_hotel_cost, list_of_cities, city_flight)


# Function which calculates the cost of car rental and outputs to the user
def car_rental_cost(rental_days, list_of_cities, daily_car_rental, city_flight):
    index = list_of_cities.index(city_flight)
    daily_car_rental = daily_car_rental[index]
    print(rental_days)
    print(daily_car_rental)
    car_total = daily_car_rental * rental_days
    print(
        f"\nThe total cost of the car rental in {list_of_cities[index].capitalize()} would be £{car_total}"
    )


car_rental_cost(rental_days, list_of_cities, daily_car_rental, city_flight)


def plane_cost(list_of_citites, city_flight, plane_cost):