""" 
Problem: You are tasked with developing a Python program for a bank to help determine whether a customer is eligible for
a loan based on their salary and loan amount requested.

The customer is eligible for a loan if:

Their monthly salary is greater than or equal to 30,000.00.
The loan amount they request is less than or equal to 10 times their monthly salary.
If customer is eligible, ask how many months to pay and add a 10% interest increase

If the customer is not eligible, display a message explaining why they are not approved 
(either low salary or too high loan request)
"""

# Prompt the user to ask the customer his or her name:
input("Enter Customer Name: ")

# Prompt the user to entertain the customer's request for loan based on his/her salary and loan request:
Salary = float(input("Please Enter Customer's Monthly Salary: "))
Loan_Amount_Request = float(input("Please Enter the amount of Loan Request: "))

# Eligibility Verification
if (Salary > 30000):
    Loan_Amount = Salary * 10
    if (Loan_Amount_Request <= Loan_Amount):
        print("You are eligible to loan")
        input()
        Month_Request = int(input("How many months would you pay? (An 10% interest increase will be added to your loan): "))
        Loan_Requested = Loan_Amount_Request * 0.10 
        Final_Loan_Requested = Loan_Requested / Month_Request
        print("*initializing*")
        input()
        print("Here is the amount of loan that has been processed: ", Final_Loan_Requested)
        print("Loan Request Accepted")
        
        input()
        print("Have a nice day, dear customer!")
        
    
else:
    print("We apologize Dear Customer, for Loan Request is not eligible enough due to the customer's low salary and/or high loan request that exceeded the salary of the customer does not meet the interdependence requirement of a salary of greater than or equal to 30,000.00 and the loan amount request is less than or equal to 10 times to their monthly salary.")
    print("Loan Request Denied")
 
input()
input("Enter Customer Name: ")
    
input()
