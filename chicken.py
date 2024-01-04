#建立類別
class Chicken():
    #建立建構子
    def __init__(self ,chicken_type , part , price , serves_people , discount):
        self.chicken_type = chicken_type
        self.part = part
        self.price = price
        self.serves_people = serves_people
        self.discount = discount

    #使用property設定價格,來確保價錢不易更改
    @property 
    def Price(self):
        return self.price
    #使用setter , 設定一個機制來檢查輸入的價格是否合理
    @Price.setter
    def Price(self , new_price):
        if new_price < 0 :
            raise ValueError('Please enter the reasonable price!')
        self.price = new_price

    #使用property , 來計算折扣後價格,以免輸入到不合理金額
    @property
    def Price_afetr_discount(self):
        return self.discount * self.price
       
    #顯示所有的資訊
    def Display_all_info(self):
        print("Chicken Type : {} \nChicken Part : {} \nPrice : {} \nServes for several people : {} \nDiscount : {}".format(self.chicken_type , self.part , self.price , self.serves_people , self.discount))

    
    
#產生物件
Combo1 = Chicken('White chopped chicken' , 'Mix' , 500 , '6' , 0.9 )
Combo2 = Chicken('Imperial Rooster' , 'Leg' , 300 , '3' , 0.9 )
Combo3 = Chicken('black feather broiler' , 'Mix' , 500 , '6' , 0.9 )
Combo4 = Chicken('turkey' , 'Mix' , 1000 , '8' , 0.9 )


#執行副函式
Combo1.Display_all_info()

print('Price after dicount : {}'.format(Combo1.Price_afetr_discount))

Combo2.Display_all_info()
print('Price after dicount : {}'.format(Combo2.Price_afetr_discount))

Combo3.Display_all_info()
print('Price after dicount : {}'.format(Combo3.Price_afetr_discount))

Combo4.Display_all_info()
print('Price after dicount : {}'.format(Combo4.Price_afetr_discount))