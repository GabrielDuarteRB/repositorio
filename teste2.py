n = [1, 5, 3, 4, 2]
x = 2
cont = 0

for item in range(len(n)):
    for i in range(len(n)):
        if (n[item] - n[i]) == x:
            cont += 1

print(cont)
