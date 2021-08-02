class Korean:
    country = "korea"

    def __init__ (self, name, age, address):
        self.name = name
        self.age = age
        self.address = address 

#객체생성
man = Korean('Hong',35,'seoul')
weman = Korean('Julice', 47, 'seoul')
# korean.name
#korean.age
#korean.address
#이렇게는 답이 안나옴 

print(man.name) 
print(man.country) 
print(Korean.country) #클래스의 변수 ->korea

print(weman.country)