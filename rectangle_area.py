Usr_inquiry = input("Do you want to calculate area ? (Y/N) : ").upper()
def area_calculation():
    rec_l = float(input("Input l (cm) : "))
    rec_w = float(input("Input w (cm) : "))
    return print(f"A (cm^2) : {rec_l * rec_w} ")
if Usr_inquiry == "Y":
    area_calculation()
else:
    print("Understandable , have a good day")