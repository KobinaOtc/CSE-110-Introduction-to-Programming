# Ask users for their rating from 1 - 10
print('\nRate the following from 1 - 10')

loan_size = int(input('How large is the loan? '))
credit_score = int(input('How good is your credit history? '))
income_score = int(input('How high is your income? '))
down_payment_size = int(input('How large is your down payment? '))
loan_approval = False
# Check if the loan size is at least 5
if loan_size >= 5:
    if credit_score >= 7 and income_score >= 7:
        loan_approval = True
    elif (credit_score >= 7 or income_score >= 7) and down_payment_size >= 5:
        loan_approval = True
    else:
        loan_approval = False
# if the loan is not 5 or greater
else:
# If the credit is less than 4, then the decision is "no"
    if credit_score < 4:
        loan_approval = False
    else:
        if income_score >= 7 or down_payment_size >= 7:
            loan_approval = True
        elif  income_score >= 4 and down_payment_size >= 4:
            loan_approval = True
        else:
            loan_approval = False

# Print qualification.
if loan_approval:
    print('\nYour Loan has been approved.\n')
else:
    print('\nYou do not qualify for a loan at this time.\n')
