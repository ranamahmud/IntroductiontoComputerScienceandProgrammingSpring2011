#Rana
principal = float(
    raw_input('Enter the outstanding balance on your credit card: '))
print(principal)
interest_rate = float(
    raw_input('Enter the annual credit card interest rate as decimal: '))
print(interest_rate)
min_monthly_payment_rate = float(
    raw_input('Enter the minimal monthly payment rate as decimal: '))
print(min_monthly_payment_rate)

x = 1
total_paid = 0
for num in range(1, 13):
    print('Month: '+str(x))
    x = x + 1

    minimum_payment = min_monthly_payment_rate * principal
    total_paid+=minimum_payment
    print('Minimum monthly payment: $' + str(round(minimum_payment,2)))

    interest_paid = interest_rate / 12.0 * principal
    principal_paid = minimum_payment - interest_paid
    print('Principal paid: $' + str(round(principal_paid,2)))
    remaining_balance = principal - principal_paid
    print('Remaining balance: $' + str(round(remaining_balance,2)))
    principal = remaining_balance

print('RESULT')
print('Total amount paid: $'+str(round(total_paid,2)))
print('Remaining balance: $'+str(round(remaining_balance,2)))
