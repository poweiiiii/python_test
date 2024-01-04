
#建立類別
class Drinks():
    def __init__(self , name,sugar_index, price):
        self.price = price
        self.name = name
        self.sugar_index = sugar_index

    #顯示品項
    def dispaly_name(self):
        print('Drink :{} '.format(self.name))

    #顯示價錢
    def dispaly_price(self):
        print("Price : {}".format(self.price))

    #顯示甜度
    def dispaly_sugar(self):
        print("Sugar : {}".format(self.sugar_index))
    #使用property更改名字
    @property
    def correct_name(self):
        return self.name
    
    @correct_name.setter
    def correct_name(self , new_name):
        self.name = new_name

    #使用property更改甜度
    @property
    def correct_sugar(self):
        return self.sugar_index
    
    @correct_sugar.setter
    def correct_sugar(self , new_sugar):
        self.sugar_index = new_sugar

    #使用property更改價錢
    @property
    def correct_price(self):
        return self.price

    @correct_price.setter
    def correct_price(self , new_price):
        self.price = new_price
    
#建立子類別
class Cold_drinks(Drinks):
    #建立建構子
    def __init__(self, name, ice_index , sugar_index, price):
        self.name = name
        self.ice_index = ice_index
        self.sugar_index = sugar_index
        self.price = price
#建立子類別
class Hot_drinks(Drinks):
    #建立建構子
    def __init__(self,name , sugar_index , price):
        self.name = name
        self.price = price   
        self.sugar_index= sugar_index

#建立物件
Coffee = Hot_drinks('Coffee' ,'No Sugar', '120')
latté = Hot_drinks('latté' ,'No Sugar', '150')
green_tea = Hot_drinks('green_tea' ,'Half sugar', '50')
Red_Tea = Cold_drinks('Red_Tea' , 'Half ice' , 'Half sugar' , '30')
Milk_tea = Cold_drinks('Milk_tea ' , 'Half ice' , 'NO sugar' , '85')
Bubble_Milk_tea = Cold_drinks('Bubble Milk tea' , 'Half ice' , 'No sugar' , '130')

Coffee.dispaly_name()
Coffee.dispaly_price()
Coffee.dispaly_sugar()
#更改價錢
Coffee.correct_price = '150'
#更改甜度
Coffee.correct_sugar = 'Three-point sugar'
print('!Price correct to : {} !'.format(Coffee.price))
print('!Sugar correct to : {} !'.format(Coffee.sugar_index))


print('**-------------------------------------')
#建立類別
class Employee():
    #建立建構子
    def __init__(self , name , Seniority , work_time):
        self.name = name
        self.Seniority = Seniority
        self.work_time = work_time
    #查詢名字
    def Search_Employee_Name(self):
        print("Name : {}" .format(self.name))
    #顯示年資
    def Display_Seniority(self):
        print("{}'s Seniority : {}".format(self.name , self.Seniority))
    #顯示時數
    def Display_Work_Time(self):
        print("{}'s work time is : {}  ".format(self.name , self.work_time))
    #使用property , 來計算月薪
    @property
    def Calculate_salary(self):
        salary = 183 * self.work_time
        return salary

#建立員工物件
Employee1 = Employee('Aaron' , '3' , 250)
Employee2 = Employee('Zack' , '1' , 150)
Employee3 = Employee('Ash' , '10' , 280)

Employee1.Search_Employee_Name()
Employee1.Display_Seniority()
Employee1.Display_Work_Time()
print('Salary :')
print(Employee1.Calculate_salary)
print('-----')
Employee2.Search_Employee_Name()
Employee2.Display_Seniority()
Employee2.Display_Work_Time()
print('Salary :')
print(Employee2.Calculate_salary)
print('-----')
Employee3.Search_Employee_Name()
Employee3.Display_Seniority()
Employee3.Display_Work_Time()
print('Salary :')
print(Employee3.Calculate_salary)

