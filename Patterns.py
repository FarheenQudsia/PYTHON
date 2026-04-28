for i in range(10, 0, -1):
    print(f"{" *"*i:<20}")

#2nd Pattern
for i in range(1,5):
    for s in range(1,i+1):
        print(' ',end=" ")
    for j in range(1,i+1):
        j*=j
        print(f'{j}',end=" ")
    print()
for k in range(5,0,-1):
    for m in range(1,k+1):
        print(' ',end=" ")
    for l in range(1,k+1):
        l*=l
        print(f'{l}',end=" ")
    print()

#3rd Pattern
for i in range(1,5):
    for s in range(5-i):
        print(' ',end=" ")
    for j in range(1,i+1):
        j*=j
        print(f'{j}',end=" ")
    print()
for k in range(5,0,-1):
    for m in range(5-k):
        print(' ',end=" ")
    for l in range(1,k+1):
        l*=l
        print(f'{l}',end=" ")
    print()

#4th Pattern
for i in range(1,5):
    for s in range(-5-i):
        print(end=" ")
    for j in range(1,i+1):
        j*=j
        print(f'{j}',end=" ")
    print()
for k in range(5,0,-1):
    for m in range(-5-k):
        print(end=" ")
    for l in range(1,k+1):
        l*=l
        print(f'{l}',end=" ")
    print()

#5th Pattern
for i in range(1,5):  
    for s in range(-1,i+1):
        print(' ',end=" ")
    for j in range(1,i+1):
        j*=j
        print(f'{j}',end=" ")
    print()
for k in range(5,0,-1):
    for m in range(-1,k+1):
        print(' ',end=" ")
    for l in range(1,k+1):
        l*=l
        print(f'{l}',end=" ")
    print()

#6th Pattern
for i in range(1,5):
    for s in range(5-i):
        print(end=" ")
    for j in range(1,i+1):
        j*=j
        print(f'{j}',end=" ")
    print()
for k in range(5,0,-1):
    for m in range(5-k):
        print(end=" ")
    for l in range(1,k+1):
        l*=l
        print(f'{l}',end=" ")
    print()

#7th Pattern
for i in range(1):
    print(f"{'* '*10}")
    for j in range(0,4):
        print(f"{'* '*2}")
for i in range(1):
    print(f"{'* '*10}")
    for j in range(0,4):
        print(f"{'* '*2}")