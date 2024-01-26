import math

# Program which calculates the total cost of a holiday for a user

list_of_cities = ["berlin", "amsterdam", "zurich", "paris", "budapest"]

plane_cost = [89, 65, 110, 95, 87]

daily_car_rental = [39, 45, 86, 98, 72]

daily_hotel_cost = [78, 82, 125, 110, 90]

print("\n\n\t\t\tWelcome to Yourtrip!")

# Request the city choice from the user
while True:
    city_flight = input(
        "\nPlease type either 'Berlin', 'Amsterdam', 'Zurich', 'Paris' or 'Budapest': "
    )
    if city_flight.lower() not in list_of_cities:
        print("\n------------------------ You've entered incorrectly ------------------------\n")
        continue
    else:
        print(f"\n\n------------------- Great, you have chosen to fly to {city_flight.capitalize()} -------------------")
        break


# Function which requests the number of nights that the user would like to book a hotel for
def number_of_nights():
    num_nights = input("\nPlease input the number of nights that you wish to stay: ")

    try:
        num_nights = int(num_nights)
        if num_nights <= 0:
            num_nights = 0
            print("\n--------------------- You've chosen not to book a hotel ---------------------\n")
            return num_nights
        else:
            return num_nights
    except ValueError:
        print("\n------------------------ You've entered incorrectly ------------------------")
        return number_of_nights()


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
            print("\n--------------------- You've chosen not to rent a car ---------------------\n")
            return rental_days
        else:
            return rental_days
    except ValueError:
        print("\n------------------------ You've entered incorrectly ------------------------")
        return car_rental_days()


rental_days = car_rental_days()


# Function which calculates the cost of the hotel per night and outputs to the user
def hotel_cost(num_nights, daily_hotel_cost, list_of_cities, city_flight):
    index = list_of_cities.index(city_flight)
    daily_hotel_cost = daily_hotel_cost[index]
    hotel_total = daily_hotel_cost * num_nights
    print(
        f"\nThe total cost of the hotel in {list_of_cities[index].capitalize()} would be £{hotel_total}\n"
    )
    return hotel_total


# Function which calculates the cost of car rental and outputs to the user
def car_rental_cost(rental_days, list_of_cities, daily_car_rental, city_flight):
    index = list_of_cities.index(city_flight)
    daily_car_rental = daily_car_rental[index]
    car_total = daily_car_rental * rental_days
    print(
        f"\nThe total cost of the car rental in {list_of_cities[index].capitalize()} would be £{car_total}"
    )
    return car_total


# Function which calculates the cost of the flight and outputs to the user
def total_plane_cost(list_of_cities, city_flight, plane_cost):
    index = list_of_cities.index(city_flight)
    plane_total = plane_cost[index]
    print(
        f"\nThe total cost of your flight to {list_of_cities[index].capitalize()} would be £{plane_total}"
    )
    return plane_total


# Function which calculates the total cost of a holiday
def holiday_cost(city_flight):
    while city_flight in list_of_cities:
        total_plane = total_plane_cost(list_of_cities, city_flight, plane_cost)
        total_car = car_rental_cost(
            rental_days, list_of_cities, daily_car_rental, city_flight
        )
        total_hotel = hotel_cost(
            num_nights, daily_hotel_cost, list_of_cities, city_flight
        )
        total = total_plane + total_car + total_hotel
        print("\n---------------------------- Your price total: ----------------------------\n")
        print(f"Your total holiday cost: £{total}\n")
        break


holiday_cost(city_flight)
