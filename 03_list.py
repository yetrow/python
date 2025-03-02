bicycles=['red','yellow','green','black','white']
#print(bicycles[-1].title()) 
#color=f"自行车的颜色是{bicycles[3]}色。"
#print(color)


bicycles.insert(1,'pink')
#    del bicycles[0]删除列表中任意元素
#popedbicycles=bicycles.pop(0) 删除元素，仍可使用
#bicycles.remove('red')根据值删除元素

#print(bicycles)
#print(popedbicycles)
#print(f"我的第一个自行车的颜色是{popedbicycles}色。")

not_like='red'
bicycles.remove(not_like)
print(f"我不喜欢{not_like}色。")

