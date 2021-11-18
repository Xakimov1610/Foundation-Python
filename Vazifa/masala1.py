#input -->  human
#output --> HumaNa

soz = input("SOZ: ")

soz = soz.replace(soz[-1], soz[-1].capitalize(), -1)
print(soz.capitalize())