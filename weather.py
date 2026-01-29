import random

days = int(input("How many days would you like to see? "))

print("n\Weather Forecastn")

for day in range(1, days + 1):
    temp = random.randint(20, 100)

    if temp < 50:
        mood = "Cold, You should definitly wear a jacket"
    elif temp < 70:
        mood = "️Mild, sweater weather"
    else:
        mood = "Hot, a t-shirt is the way to go"
    
    print(f"Day {day}: {temp}°F — {mood}")
