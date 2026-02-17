def formula_1():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    x = int(input("x: "))
    result = (x**3 + (a + b + c) * x**2 + (a*b + b*c + a*c) * x + (a*b*c))
    return result

def formula_2():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    result = ((a**2 + b**2 + c**2) + 2*(a*b + b*c + a*c))
    return result

formulas = [formula_1, formula_2]

while True:
    decide = int(input("곱셈공식: "))
    if decide <=2:
        print(formulas[int(decide)-1]())
    else:
        print("null")
          