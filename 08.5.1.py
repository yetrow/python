#传递任意数量的实参
def making(*toppings):
    print(toppings)
making('tobacco')
making('banana','apple')


def makes(size,*toppings):#如果届户搜不同类型的实参，那么接受任意数量的形参需要放在最后
    print(f"{size}寸，需要：")
    for i in toppings:
        print(i)
makes(10,'cheese')
makes(15,'noodles','vegtables')

print("-----")

def builds(first,last,**user_info):#其中**这两个星号让python创建了一个名为user_info的字典，该字典包含函数收到的其他所有名值对
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
users=builds('tom','james',location='west',phone='apple')
print(users)