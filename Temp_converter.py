
#Python temp converter
def ctof():
    temp_unit = float(input("Input value: "))
    c_to_f = (temp_unit * 9/5) + 32
    return print(f"Converted temperature in F : {c_to_f} C")
def cto_k():
    temp_unit = float(input("Input value: "))
    c_to_k = temp_unit + 273.15
    return print(f"Converted temperature in K : {c_to_k} K")
def ftoc():
    temp_unit = float(input("Input value: "))
    f_to_c = (temp_unit - 32) * 5/9
    return print(f"Converted temperature in F : {round(f_to_c,4)} F")
def fto_k():
    temp_unit = float(input("Input value: "))
    f_to_k = ((temp_unit - 32) * 5/9) + 273.15
    return print(f"Converted temperature in K : {round(f_to_k,4)} K")
def kto_c():
    temp_unit = float(input("Input value: "))
    k_to_c = temp_unit - 273.15
    return print(f"Converted temperature in C : {k_to_c} C")
def kto_f():
    temp_unit = float(input("Input value: "))
    k_to_f = ((temp_unit - 273.15) * 9/5) + 32
    return print(f"Converted temperature in F : {round(k_to_f,4)} F")
print("Welcome to Python temperature converter !!!")
usr_choice = input("Choose temperature unit (C/F/K) : ").upper()
while usr_choice not in ("C", "F", "K"):
    print("Error ! Insert a valid unit")
    usr_choice = input("Choose temperature unit (C/F/K) : ").upper()
if usr_choice == "C":
    choice_2 = input("Choose the unit to convert to (K/F) : ").upper()
    while choice_2 not in ("K","F"):
        print("Error ! Insert a valid unit")
        choice_2 = input("Choose the unit to convert to (K/F) : ").upper()
    if choice_2 == "K":
        cto_k()
    elif choice_2 == "F":
        ctof()
if usr_choice == "F":
    choice_2 = input("Choose the unit to convert to (C/K) : ").upper()
    while choice_2 not in ("C","K"):
        print("Error ! Insert a valid unit")
        choice_2 = input("Choose the unit to convert to (C/K) : ").upper()
    if choice_2 == "C":
        ftoc()
    elif choice_2 == "K":
        fto_k()
if usr_choice == "K":
    choice_2 = input("Choose the unit to convert to (C/F) : ").upper()
    while choice_2 not in ("C","F"):
        print("Error ! Insert a valid unit")
        choice_2 = input("Choose the unit to convert to (C/F) : ").upper()
    if choice_2 == "C":
        kto_c()
    elif choice_2 == "F":
        kto_f()

