word_a = 'DISH'
word_b = 'DISTA'
cell = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
for i in range(len(word_a)):
    for j in range(len(word_b)):
        if word_a[i] == word_b[j]:

            cell[i][j] = cell[i-1][j-1]+1
        else:
            cell[i][j] = 0
print(cell)