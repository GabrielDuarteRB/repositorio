from math import ceil

s = 'tenha um bom dia'
s = s.replace(' ', '')
novaPalavra = ''
grid = ceil(float(len(s)) ** 0.5)
cont1 = 0
cont2 = 0
novoArray = [[0 for _ in range(grid)] for _ in range(grid)]

for i in range(grid):
    for j in range(grid):
        if (i*grid+j+1) <= len(s):
            novoArray[i][j] = s[i*grid+j]
        else:
            novoArray[i][j] = ''

for i in range(grid):
    for j in range(grid):
        novaPalavra = novaPalavra + novoArray[j][i]
    novaPalavra = novaPalavra + " "

print(novaPalavra)