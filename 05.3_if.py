favorite_fruits=['apple','banana','orange']
for i in favorite_fruits:
    if i=='apple':
        print("对不起，我们没有apple\n")
    else:
        print(f"你喜欢的是{i}\n")

num1=['1','2','3','4',5]
num2=['1','2',5]
for i in num1:
    if i in num2:
        print(f"共有{i}\n")
    else:
        print(f"没有{i}\n")