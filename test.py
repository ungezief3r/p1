class calculator:
    def __init__(self):
        self.formulas = [self.formula_1, self.formula_2, self.formula_3, self.formula_4]
    


    #곱셈공식 (x+a)(x+b)(x+c)
    def formula_1(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        x = int(input("x: "))
        result = (x**3 + (a + b + c) * x**2 + (a*b + b*c + a*c) * x + (a*b*c))
        return result


    #곱셈공식 (a+b+c)^2
    def formula_2(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        result = ((a**2 + b**2 + c**2) + 2*(a*b + b*c + a*c))
        return result


    #곱셈공식 (a+b)^3
    def formula_3(self):
        a = int(input("a: "))
        b = int(input("b: "))
        result = ((a**3 + 3*a**2*b + 3*a*b**2 + b**3))
        return result


    #곱셈공식 (a+b+c)(a^2+b^2+c^2-ab-bc-ca)
    def formula_4(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        result = ((a**3 + b**3 + c**3) - 3*a*b*c)
        return result


#결정

    def run(self):
        while True:
            try:
                decide = int(input("곱셈공식: "))
                print(self.formulas[int(decide)-1]())
                
            except:
                print("null")
                
calc = calculator()
calc.run()
