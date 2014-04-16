#Write a program to calculate the credit card balance after one year if a person 
#only pays the minimum monthly payment required by the credit card company each month.

monthlyInterestrate = annualInterestRate/12.0
month = 0
totalPaid = 0

while month < 12:
    month += 1
    payment = monthlyPaymentRate * balance
    monthlyUnpaidBal = balance - payment
    balance = monthlyUnpaidBal + (monthlyInterestrate * monthlyUnpaidBal)
    totalPaid += payment
    print "Month: "+ str(month)
    print "Minimum monthly payment: " + "%.2f" %payment
    print "Remaining balance: " + "%.2f" %balance

print "Total paid: " + "%.2f" %totalPaid
print "Remaining balance: " + "%.2f" %balance

# write a program that calculates the minimum fixed monthly payment needed in order 
# pay off a credit card balance within 12 months.

savedBal = balance

monthlyInterestrate = annualInterestRate/12.0
payment = 0
month = 0

while balance >= 0:
    for month in range(12):
        monthlyUnpaidBal = balance - payment
        balance = monthlyUnpaidBal + (monthlyInterestrate * monthlyUnpaidBal)
    payment += 10
    if balance >=0:
        balance = savedBal
    else:
        print "Lowest Payment: " + str(payment - 10)


#PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER

orgBal = balance
epsilon = 0.01
monthlyInterestrate = annualInterestRate/12.0

lowerBound = balance /12.0
upperBound = (balance*(1+monthlyInterestrate)**12)/12.0

minpayment = (lowerBound + upperBound) / 2.0

while abs(balance) > epsilon:
    minpayment = (lowerBound + upperBound) / 2.0
    balance = orgBal
    for month in range(12):
        monthlyUnpaidBal = balance - minpayment
        balance = monthlyUnpaidBal + (monthlyInterestrate * monthlyUnpaidBal)
    
    if balance > 0: # need to up the payment
        lowerBound = minpayment
    elif balance < 0:
        upperBound = minpayment
    elif balance == 0.00:
        print "Lowest Payment: " +  "%.2f" %minpayment
print "Lowest Payment: " +  "%.2f" %minpayment
