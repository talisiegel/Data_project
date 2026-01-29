
import requests


url = "https://api.citybik.es/v2/networks/citi-bike-nyc"
response = requests.get(url)

data = response.json()

stations = data["network"]["stations"]

total_bikes = 0
for station in stations:
    total_bikes += station["free_bikes"]

print("Total available Citi Bikes in NYC:", total_bikes)

print(f"There are {total_bikes} bikes available in NYC")





