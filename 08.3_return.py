def get_name(firstname,lastname,middlename=''):
    full_name=f"{firstname} {middlename} {lastname}"
    return full_name
musician=get_name('tom','james')
print(musician)
musician=get_name('tom','james','mark')
print(musician)

#返回字典
def persion(first,last):
    persion={'first':first,'last':last}
    return persion
musician=persion('jim','cool')
print(musician)
