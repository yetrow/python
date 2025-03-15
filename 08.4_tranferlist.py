def greet(names):
    for i in names:
        msg=f"hello,{i.title()}"
        print(msg)
usernames=['jamne','mark','tom']
greet(usernames)                     

#在函数中修改列表
def prints(desigin,complete):
    while desigin:
        current_desigin=desigin.pop()
        print(f"{current_desigin}")
        complete.append(current_desigin)
def shows(complete):
    for i in complete:
        print(i)
undesigin=['iphone','mac','ipad','ipod']
complete=[]
prints(undesigin,complete)
print("--")
shows(complete)