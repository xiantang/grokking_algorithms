"""
# @File  : 9.2.py
# @Author: xiantang
# @Date  : 08/08/18
# @Email :zhujingdi1998@gmail.com
# blog : zhanshengpipidi.cn/blog
# Github : github.com/xiantang
"""
word_a = 'FISH'
word_b = 'FOSH'
cell = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
for i in range(len(word_a)):
    for j in range(len(word_b)):
        if word_a[i] == word_b[j]:
            cell[i][j]=cell[i-1][j-1]+1
        else:
            cell[i][j]=max(cell[i-1][j],cell[i][j-1])
print(cell)