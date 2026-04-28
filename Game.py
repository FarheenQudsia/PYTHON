import random
random_choice = random.randint(0,200)
attempt =1
num = int(input( 'enter a number'))

while num != random_choice:
    attempt+=1
    if num < random_choice: #30<200
        print (f"take a num little higher attempt: {attempt}")
    else: #NUM>200
        print(f'take a num little smaller attempt:{attempt}')
    num=int(input('enter a number: '))
print(f'congrats you found the number in {attempt} attempts')
if attempt<=10:
    print('the minimum access is 10')
else:
    print("u exceed the limit")