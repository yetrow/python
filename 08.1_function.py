def animal(types,name='james'):#使用默认值：形参中先写无默认值，再列出有默认值
    print(f"i have a {types}.")
    print(f"my {types}'s name is {name.title()}")
animal('dog','horay')
#关键字实参
animal(name='nike',types='cat')
#默认值
animal(types='dog')
