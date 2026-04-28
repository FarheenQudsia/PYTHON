print('=== ATM ANALYZER ===')
print('1. Check Balance')
print('2. Deposit')
print('3. Withdraw')
print('4. Exist')
balance = 1000

print()
print()

num = int(input('Enter the option'))

while num != 4:
    
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    num = int(input('Enter the option'))

    
    if num==1:
        print(f'The total balance is : {balance}')

    elif num==2:
        deposit = int(input('Enter the deposited money'))
        balance = balance + deposit
        print(f"The total balance is {balance}")

    elif num == 3:
        withdraw = int(input('Enter the withdraw amount'))
        balance = balance - withdraw
        print(f'The remaining balance is {balance}')
    elif num == 4:
        print('exit')
    else:
        print('Number is not valid')
        

print('thanks ')