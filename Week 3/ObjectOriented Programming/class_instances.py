class Calculator:
    def add(self, a,b):
        return a+b
    def test_pass(self):
        print("Hello")
        pass
        print("World")
    
calculator = Calculator()
print('1 + 1 = ', calculator.add(1,1))

calculator.test_pass()