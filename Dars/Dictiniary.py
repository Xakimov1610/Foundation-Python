car1 = {
    "name": "AUDI",
    "speed": 250,
    "cost": 80000,
    "year": 2020,
    "new": True
}

for i in car1:
    if isinstance(car1[i], int) and not isinstance(car1[i], bool):
        print(i)
        