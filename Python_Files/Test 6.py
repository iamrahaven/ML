Salary=int(input("Monthly Salary:"))
Age=int(input("Age:"))
if(Salary>=20000 or Age<=25):
    print("You are elegible for loan")
    loan=int(input("Enter the Loan Amount:"))
    if(loan<=50000):
        print("Loan is available for",loan)
    else:
        print("Your maximum limit is 50000")
else:
    print("You are not elegible for loan")