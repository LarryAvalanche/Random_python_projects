print("Make sure to leave a blank space after every 4 numbers")
usr_input = input("Enter credit number : ")
while len(usr_input) > 19:
    print("Error! No more than 16 characters")
    usr_input = input("Enter credit number : ")
while usr_input.count(" ") != 3:
    print("Error! please leave only 3 spaces between")
usr_input.replace(" ","-")
last4digits = usr_input[-4:]
print(f"XXXX-XXXX-XXXX-{last4digits}")