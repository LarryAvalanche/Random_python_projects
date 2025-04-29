init_balance = float(input("Enter the initial principal balance: $ "))
while init_balance <= 0:
    print("Principle can't be less than or equal to zero")
    init_balance = float(input("Please enter the principal balance"
                               " again: $ "))
int_r = float(input("Enter the interest rate: % "))
while int_r <= 0:
    print("Interest rate can't be less than or equal to zero")
    init_balance = float(input("Please enter the interest rate"
                               " again: % "))
num_t = int(input("Enter the time period in years:  "))
while num_t <= 0:
    print("Time period can't be less than or equal to zero")
    init_balance = float(input("Please enter the time period"
                               " again: "))
final_amount = init_balance * pow((1 + int_r / 100),num_t)
print(f"Final amount after {num_t} year(s) with {int_r}% interest"
      f": $ {final_amount:.2f}")