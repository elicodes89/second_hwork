stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

stops.append("Edinburgh Waverley")

new_stop = "Glasgow Q St"
stops = [new_stop, *stops]

stops.insert(4, "Polmont")

index = stops.index('Linlithgow')
# print(index)

stops.remove("Livingston")

if "Cumbernauld" in stops: stops.remove("Cumbernauld")

number_of_stops = len(stops)
print(number_of_stops)

stops.sort()
print(stops)

for i in reversed(stops):
    print(i)

for stop in stops:
    print(stop)

