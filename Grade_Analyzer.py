total= 0
max = 0
min = 100
avg = 0
st_pass = 0
st_fail = 0
pass_per = 0
count = 0
count_2 = 0
print(f'=== Grade Analyze ===')

for i in range(1,6):
    current_st = int(input('Enter the students no'))
    print(f'Enter the Grade for student {i} :{current_st}')
    total+=current_st

    if current_st>max:
        max = current_st
    if current_st<min:
        min=current_st
    if current_st>=65:
        st_pass +=1
    if current_st>=60:
         count+=1
    else:
         count_2+=1
         
print('=== Grade Analyze ===')
avg =float (total/5)
print(f'AVERAGE GRADE: {avg}')
print(f'MAXIMUM GRADE: {max}')
print(f'LOWEST GRADE: {min}')
print(f'STUDENT PASSED: {count}')
print(f'STUDENT FAILED: {count_2}')
pass_per= st_pass/5*100
print(f'The pass percentage is :{pass_per}')