def number(bus_stops):
    total_passengers = 0

    for stop in bus_stops:

        total_passengers += stop[0]
        total_passengers -= stop[1]

    return total_passengers

bus_stops = [(3, 0), (4, 1), (10, 5), (2, 1)]
remaining_passengers = number(bus_stops)
print("Remaining passengers: " + str(remaining_passengers))