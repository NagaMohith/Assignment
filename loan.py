income = 5000
credit_score = 500
in_rate = 6.0
loan_status = ""

number_couster = int(input("Enter number of customer"))
for i in range(number_couster):
    input_income = int(input("Enter the your income \n"))
    input_credit = int(input("Enter the credit score \n"))
    input_rate = float(input("Enter the rate \n"))

    if input_income>income and input_credit > credit_score and input_rate>in_rate:
        loan_status = "Loan Approved"
    else:
        loan_status = "Loan not Approved"


    with open("Bank_details.txt" , "a+") as file_object:
        file_object.write(f"Customer : {i+1} , Name : xxxx , income : {input_income} , credit_score : {input_credit} , rate : {input_rate} , loan_staus : {loan_status} \n")