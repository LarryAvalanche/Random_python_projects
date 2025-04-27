import math
usr_area = input("Calculate the area of the circle ? (Y/N): ").upper()
def circ_area():
    r = float(input("Radius (r) : "))
    return print(f"Area (A) : {round(math.pi * r * r , 2)}")
if usr_area == "Y":
    circ_area()
else:
    print("Ok , have a good day")
usr_c = input("Calculate the circumference too ? (Y/N): ").upper()
def circ_c():
    r = float(input("Radius (r) : "))
    return print(f"Circumference (C) : {round(math.pi * r * 2 , 2)}")
if usr_c == "Y":
    circ_c()
else:
    print("Understandable")