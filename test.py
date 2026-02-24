class Calculator:
    def __init__(self):
        
        self.formulas = [self.formula_1, self.formula_2, self.formula_3, self.formula_4, self.formula_5]
    

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

    #곱셈공식 (a+b)(a^2-ab+b^2)
    def formula_5(self):
        a = int(input("a: "))
        b = int(input("b: "))
        result = ((a**3 + b**3))
        return result


    #결정

    def run(self):
        
        try:
                decide = int(input("곱셈공식: "))
                print(self.formulas[(decide)-1]())
                
        except ValueError:
                print("null")
            
        except IndexError:
                print("null")
            

class Equations:


    def __init__(self):
        self.equations = [self.linear_equation,self.quadratic_equation]

    def quadratic_equation(self):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        d = (b**2 - 4*a*c)

        if d > 0:

            plus = ((-b + d**0.5)/(2*a))
            minus = ((-b - d**0.5)/(2*a))

            result = ("x1 = " + str(plus) + "x2 = " + str(minus))
            return result
                    
        elif d == 0:
            result = (0)
            return result

        elif d < 0:
            result = ("허근")
            return result
            

    def linear_equation(self):
        a = int(input("x의 계수: "))
        b = int(input("상수항: "))
        result = (-b/a)

        return result
    
    def run(self):
        try:
            self.decide = int(input("차수: "))
            target_formula = (self.equations[(self.decide)-1])
                
            print(target_formula())
            
        except IndexError:
                print("null")

        except ValueError:
                print("null")

                

equa = Equations()
calc = Calculator()

calculator_modes = [equa, calc]

while True:
    try:
        decide = int(input("방정식=1, 곱셈공식=2: "))
        selected = calculator_modes[(decide)-1]
        selected.run()
    
    except ValueError:
        print("null")
    except IndexError:
        print("null")