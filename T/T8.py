import Vars

lst = Vars.T8_2
str1 = Vars.T8

x = map(lambda a, b: b + str(a), lst, str1)

print(list(x))