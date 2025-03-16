class Car:
    def __init__ (self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0  #给属性指定默认值

    def get_descri(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it.")

    # 通过方法修改属性的值
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer!")
    # 通过方法对属性的值进行递增
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

# 继承
class ElectricCar(Car):
    #初始化父类的属性
    def __init__ (self,make,model,year):
        #super()是一个特殊函数，帮助Python将父类和子类关联起来去调用Car中的__init__()方法,父类也叫超类
        super().__init__(make,model,year)
        self.battery_size=Battery()
    #给子类定义属性和方法
    def describe_battery(self):
        print(f"this car has a {self.battery_size}-kWh battery.")
    #重写父类的方法：定义一个与父类同名的方法
    def get_descri(self):
        long_name=f"{self.year} {self.make} {self.model} -electric"
        return long_name.title()
    
#创建实例
class Battery:
    def __init__ (self,battery_size=50):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"this car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size<=70:
            range=200
        else:
            range=300
        print(f"this car can go about {range} miles on a full charge.")
    
my_leaf=ElectricCar('nissan','leaf',2025)
print(my_leaf.get_descri())
my_leaf.describe_battery()
my_leaf.battery_size=100
my_leaf.get_range()