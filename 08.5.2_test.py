def make_car(manufacturer,model,**car_info):
    
    car_info['manufacturer']=manufacturer#如果使用car而不是car_info，则需要先定义car={}
    car_info['model']=model
    
    return car_info
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)