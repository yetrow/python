class Car:
    def __init__ (self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0#给属性指定默认值

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

my_car=Car('audi','a4',2025)
print(my_car.get_descri())
my_car.read_odometer()

my_car.odometer_reading=23#直接修改属性的值
my_car.read_odometer()
print('-------------------')

# 通过方法修改属性的值
my_car.update_odometer(4)
my_car.read_odometer()

my_car.increment_odometer(30)
my_car.read_odometer()