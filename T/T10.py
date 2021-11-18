import Vars

txt = "Hello, welcome to my world."
txt = txt[::-1]

result = len(txt) - txt.find("d")
print(result - 1)
