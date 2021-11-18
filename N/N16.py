sentc = input("Etner: ")

x = sentc.split()[0]

for i in range(1, len(sentc.split())):
    if len(x) > len(sentc.split()[1]):
        x = sentc.split()[i]

print(x)

