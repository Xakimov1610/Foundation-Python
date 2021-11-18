a = "*23"
b = "1*7"
c = "2*0"
d = "35*"

# print(d.index("*"))



# a.replace("*", "/")
# print(a.replace("*", "/"))

def first(a_, b_):
    a_inx = a_.index("*")
    b_inx = b_.index("*")
    result_i = []
    result_j = []

    for i in range(1, 10):
        x = a_.replace(a_[a_inx], str(i))
        for j in range(1, 10):
            y = b_.replace(b_[b_inx], str(j))
            n = int(x) + int(y)
            if n % 9 == 0:
                result_i.append(int(i))
                result_j.append(int(j))
    return result_i, result_j


print(first(a, b))
# print(type(result[0][0]))
# exit()

# def second(c_, d_, result_):
#     result_i = result_[0]
#     result_j = result_[1]
#     c_inx = c_.index("*")
#     d_inx = d.index("*")
#     result = []
#
#     print(result_i)
#     for i in result_i:
#         x = c_.replace(c_[c_inx], str(i))
#         for j in result_j:
#             y = d_.replace(d_[d_inx], str(j))
#             n = int(x) + int(y)
#             if n % 9 == 0:
#                 result_i.append(i)
#
#     print(result_i)
#
#     # result.append(result_i)
#     # result.append(result_j)
#     # result.append(result_i)
#     # result.append(result_i)


second(c, d, result)
