
alien1={'x_position':0,'y_position':25,'speed':'medium'}
alien1['speed']='fast'
if alien1['speed']=='slow':
    x_increment=1
elif alien1['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien1['x_position']=alien1['x_position']+x_increment
print(f"新的坐标是{alien1['x_position']}")
del  alien1['y_position']
print(alien1)