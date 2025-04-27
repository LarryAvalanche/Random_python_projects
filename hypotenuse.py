import math
usr_h = input("Calculate the hypotenuse (H) ? (Y/N) : ").upper()
def tri_h():
    a = float(input("First side (a) : "))
    b = float(input("Other side (b) : "))
    return print(f"Hypotenuse (h) : {round(math.sqrt(pow(a,2)+pow(b,2)) , 2)}")
if usr_h == "Y":
    tri_h()
else:
    print("Fine")
