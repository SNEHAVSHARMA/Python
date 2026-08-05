print("Welcome to Tip Generator")
bill=float(input("What was the total bill?"))
tip=float(input("How much tip(%) would you like to give?"))
tip=(tip/100)*bill
bill+=tip
person=int(input("How many peaople to split the bill?"))
pay=bill/person
final=round(pay,2)
print(f"Each person should pay: {final}" )

