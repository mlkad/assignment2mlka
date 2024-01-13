import math


#Conditionals
#1
x = int(input())
if x > 0:
    res = x + 1
elif x < 0:
    res = x - 2
else:
    res = 10
print(res)

#2
a, b, c = map(int, input().split())
count_pos = 0
count_neg = 0
if a > 0:
    count_pos += 1
elif a < 0:
    count_neg += 1

if b > 0:
    count_pos += 1
elif b < 0:
    count_neg += 1

if c > 0:
    count_pos += 1
elif c < 0:
    count_neg += 1

print(count_pos, count_neg)

#3
a, b, c = map(float, input("Enter three numbers: ").split())

numbers = [a, b, c]
numbers.sort(reverse=True)
sum_two = numbers[0] + numbers[1]
print(sum_two)

#4
x = int(input())
if x % 2 == 0:
    print('It is even')
else:
    print('It is odd')

#5
ox = float(input())
oy = float(input())
if ox > 0 and oy > 0:
    quadrant = 1
elif ox < 0 < oy:
    quadrant = 2
elif ox < 0 and oy < 0:
    quadrant = 3
elif ox > 0 > oy:
    quadrant = 4
else:
    quadrant = None

result = quadrant
if result is None:
    print("No answer")
else:
    print(quadrant)

#Loops
#1
print("Enter A < B")
A = int(input())
B = int(input())
if A < B:
    n = B - A + 1
    result = (n * (A + B)) // 2
    print(result)
else:
    print("enter values A < B")

#2
A = int(input())
B = int(input()
if A < B:
    prod = 1
    for n in range(A, B + 1):
        prod *= n
    print(prod)
else:
    print("enter values A < B")

#3
print("N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2")
N = int(input())
if N > 0:
    summ = 0
    for n in range(N, 2 * N + 1):  # N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2
        summ += n**2
    print(summ)
else:
    print("Enter a positive integer")

#4
A = float(input())
N = int(input())
if N > 0:
    powers = []
    for n in range(1, N+1):
        res = A ** n
        powers.append(res)
        print(res)
    print(powers)
else:
    print("Enter a positive integer")

#5
N = int(input("Enter a positive integer: "))

if N > 0:
    summ = 0
    for i in range(1, N + 1):
        summ += math.factorial(i)
    print(summ)
else:
    print("Please enter a positive integer.")
