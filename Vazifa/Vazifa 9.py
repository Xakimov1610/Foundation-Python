height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))

index = weight ** 2 / height

print(index)

if index < 18.5:
    print("ozg'in")
elif 18.5 <= index <= 25:
    print("Normal")
elif 26 <= index <= 30:
    print("Ortiqcha")
elif index >31:
    print("Semiz")