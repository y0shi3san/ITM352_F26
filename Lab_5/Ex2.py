# define a list of taxi trip durations in miles
# Kaili Takara
# September 23, 2026

trip_duration = [1.1, 0.8, 2.5, 2.6]
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

trips = {
    "miles": trip_duration,
    "fares": trip_fares
}
print(trips)


print("The duration of the third trip is:", trips["miles"][2], " miles")
print("The fare of the third trip is:", trips["fares"][2])
