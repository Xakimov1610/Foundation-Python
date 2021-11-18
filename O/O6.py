input_ = "PyNaTive"
upper = []
lower = []
[upper.append(i) if i.isupper() else lower.append(i) for i in input_]

lower = "".join(lower)
upper = "".join(upper)
print(lower + upper)