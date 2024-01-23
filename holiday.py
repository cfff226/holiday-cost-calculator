# Program which calculates the total cost of a holiday for a user

list_of_cities = ["berlin", "amsterdam", "zurich", "paris", "budapest"]

plane_cost = ["89", "65", "110", "95", "87"]

daily_car_rental = ["39", "45", "86", "98", "72"]

# Request the city choice from the user
while True:
    print("\nWelcome to Yourtrip!")
    city_flight = input("\nPlease type either 'Berlin', 'Amsterdam', 'Zurich', 'Paris' or 'Budapest ")
    if city_flight.lower() not in list_of_cities:
        print("You have entered incorrectly")
        continue
    else:
        city_flight = city_flight.capitalize()
        print(f"\nGreat, you have chosen to fly to {city_flight}")
        break