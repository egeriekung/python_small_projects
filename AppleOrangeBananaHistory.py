import random

answer = 'yes'
A =[]
O =[]
B =[]

while answer != 'no':
    a = random.randint(0,20)
    o = random.randint(0,20)
    b = random.randint(0,20)
    A.append(a)
    O.append(o)
    B.append(b)
    if (a > o) and (o > b):
        print("rank: 1. apple, 2. orange, 3. banana")
    elif (a > b) and (b > o):
        print("rank: 1. apple, 2. banana, 3. orange")
    elif (o > a) and (a > b):
        print("rank: 1. orange, 2. apple, 3. banana")
    elif (o > b) and (b > a):
        print("rank: 1. orange, 2. banana, 3. apple")
    elif (b > a) and (a > o):
        print("rank: 1. banana, 2. apple, 3. orange")
    elif (b > o) and (o > a):
        print("rank: 1. banana, 2. orange, 3. apple")
    else:
        print('There is a tie')
    
    print("apple",a)
    print("orange",o)
    print("banana",b)
    
    answer = input('continue? yes/no: ')

print('Apples',A)
print('Oranges',O)
print('Bananas',B)
print('total: ',sum(A)+sum(B)+sum(O),' Furits')