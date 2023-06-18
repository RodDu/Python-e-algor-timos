x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(x) // 3):
    for j in range(len(x) // 3):
        print(x[i * j], end="")
    print()
