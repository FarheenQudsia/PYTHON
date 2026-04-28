salary =int(input('enter the salary $'))
tax = None

if salary<=10000:

   print(f'total net salary is{salary}')

elif salary<= 30000:
   tax = 0.10
   tax_amount = salary * tax
   net_salary = salary - tax_amount
   print(f"net salary{net_salary}")
   print(f'total tax amount is{ tax_amount}')
elif salary<=60000 :
   tax = 0.20
   tax_amount = salary * tax
   net_salary = salary - tax_amount
   print(f"net salary{net_salary}")
   print(f'total tax amount is{ tax_amount}')
else:
   tax = 0.30
   tax_amount = salary * tax
   net_salary = salary - tax_amount
   print(f"net salary{net_salary}")
   print(f'total tax amount is{ tax_amount}')