class Calculator:
    def input_ecpr(self):
        ecpr= input('수식을 입력하세요 >>')
        self.ecpr = ecpr

    def calculate(self):
        return eval (self.ecpr)

calc = Calculator()
calc.input_ecpr()
print('수식 결과는 {}입니다'.format(calc.calculate()))