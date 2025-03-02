#range 创建数值列表
numlist=list(range(1, 6))
print(numlist)

squares=[]
for i in range(1,6):
    square=i**2
    squares.append(square)
print(squares)

#切片
players=['charles','martina','micheal','florence','eli']
print(players[1:3])
print(players[:3])
print(players[1:])
print(players[-3:])

#复制列表：省略起始索引和终止索引
friends=players[:]
print(friends)


