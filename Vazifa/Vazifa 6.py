gap = input("Soz kititing: ")

if len(gap) % 4 == 0:
    gap1 = gap[:len(gap) // 2]
    gap2 = gap[len(gap) // 2:]
    gap = gap1 + gap2[::-1]
    print(gap)