#Python Calculator
import math
print("Welcome!!!")
user_query = input("A(+) , S(-) , D(/) , M(*) , Adv , Adv2 : ")
while (not user_query == "A"
       or user_query == "S"
       or user_query == "D"
       or user_query == "M"
       or user_query == "Adv"
       or user_query == "Adv2"):
    print("Error ! Type the required words exactly")
    user_query = input("A(+) , S(-) , D(/) , M(*) , Adv , Adv2 : ")
def add():
    a = float(input("Enter a : "))
    b = float(input("Enter b : "))
    return print(f"A(+) : {a + b}")
def sub():
    a = float(input("Enter a : "))
    b = float(input("Enter b : "))
    return print(f"S(-) : {a - b}")
def div():
    a = float(input("Enter a : "))
    b = float(input("Enter b : "))
    return print(f"D(/) : {round((a / b) , 3)}")
def mul():
    a = float(input("Enter a : "))
    b = float(input("Enter b : "))
    return print(f"M(*) : {a * b}")
def exp():
    a = float(input("Enter a : "))
    b = float(input("Enter b : "))
    return print(f"exp : {a ** b}")
def sqrt():
    a = float(input("Enter a : "))
    return print(f"sqrt : {round((math.sqrt(a)) , 3)}")
def sin():
    a = float(input("Enter a : "))
    return print(f"sin : {round((math.sin(a)) , 3)}")
def cos():
    a = float(input("Enter a : "))
    return print(f"cos : {round((math.cos(a)) , 3)}")
def tan():
    a = float(input("Enter a : "))
    return print(f"tan : {round((math.tan(a)) , 3)}")
def cot():
    a = float(input("Enter a : "))
    return print(f"cot q : {round((1/(math.tan(a))) , 3)}")
def sec():
    a = float(input("Enter a : "))
    return print(f"sec q : {round((1/(math.cos(a))) , 3)}")
def co_sec():
    a = float(input("Enter a : "))
    return print(f"cot` q : {round((1/(math.sin(a))) , 3)}")
def sin_h():
    a = float(input("Enter a : "))
    return print(f"sin : {round((math.sinh(a)) , 3)}")
def cos_h():
    a = float(input("Enter a : "))
    return print(f"cos : {round((math.cosh(a)) , 3)}")
def tan_h():
    a = float(input("Enter a : "))
    return print(f"tan : {round((math.tanh(a)) , 3)}")
def cot_h():
    a = float(input("Enter a : "))
    return print(f"cot q : {round((1/(math.tanh(a))) , 3)}")
def sec_h():
    a = float(input("Enter a : "))
    return print(f"sec q : {round((1/(math.cosh(a))) , 3)}")
def co_sec_h():
    a = float(input("Enter a : "))
    return print(f"cot` q : {round((1/(math.sinh(a))) , 3)}")
if user_query == "A":
    add()
if user_query == "S":
    sub()
if user_query == "D":
    div()
if user_query == "M":
    mul()
def adv():
    user_query2 = input("exp "
                        ", sqrt "
                        ", sin "
                        ", cos "
                        ", tan "
                        ", cot "
                        ", sec "
                        ", co_sec : ")
    if user_query2 == "exp":
        exp()
    if user_query2 == "sqrt":
        sqrt()
    if user_query2 == "sin":
        sin()
    if user_query2 == "cos":
        cos()
    if user_query2 == "tan":
        tan()
    if user_query2 == "cot":
        cot()
    if user_query2 == "sec":
        sec()
    if user_query2 == "co_sec":
        co_sec()
def adv2():
    user_query2 = input("sin_h "
                        ", cos_h "
                        ", tan_h "
                        ", cot_h "
                        ", sec_h "
                        ", co_sec_h : ")
    if user_query2 == "sin_h":
        sin_h()
    if user_query2 == "cos_h":
        cos_h()
    if user_query2 == "tan_h":
        tan_h()
    if user_query2 == "cot_h":
        cot_h()
    if user_query2 == "sec_h":
        sec_h()
    if user_query2 == "co_sec_h":
        co_sec_h()
if user_query == "Adv":
    adv()
if user_query == "Adv2":
    adv2()

