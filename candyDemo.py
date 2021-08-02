#class Candy:
#    def set_info(self, shape, color):
#        self.shape = shape
#        self.color = color

class Candy:
    def __init__(self, shape, color):  #메소드. 생성자로 자동으로..   
        self.shape = shape
        self.color = color


# 객체를 만들고 그 안에 메소드를 더 설정해서 했음 

# 생성자를 이용하면 (__init__) 더 매끄럽고 짧게 가능 

satang = Candy('circle','brawn')

#satang = Candy()  #값이 없는 빈 객체 생성
#satang.set_info('circle','brown') # 일단 붕어빵 찍고 -> 이름 던져줌 

print(satang.shape)
print(satang.color)
