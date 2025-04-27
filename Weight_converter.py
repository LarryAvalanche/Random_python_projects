#Python weight converter
weight = float(input("Enter weight : "))
unit = input("Kilogram or Pound ? (kg/lb) : ")
if unit == "kg":
    weight *= 2.2046
    print(f"weight in pound : {round(weight,4)} lb")
elif unit == "lb":
    weight /= 2.2046
    print(f"weight in kilogram : {round(weight,4)} kg")
else:
    print("Error, invalid unit ! choose kg or lb")
    unit = input("Kilogram or Pound ? (kg/lb) : ")


