def animal(types,name='james'):
    print(f"i have a {types}.")
    print(f"my {types}'s name is {name.title()}")
animal('dog','horay')
#关键字实参
animal(name='nike',types='cat')
#默认值
animal(types='dog')