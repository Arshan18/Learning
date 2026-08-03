# Problem1: Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter a Number:"))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")

# Problem2: Write a program to greet all the person name stored in a list 'l' and which starts with letter 'S'.

l = ["John", "Sam", "Sally", "Mike", "Will", "Steve"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")

# Problem3: Write a program to print multiplication table of a given number using while loop.

num = int(input("Enter a number:"))

i = 1

while i<11:
    print(f"{num} X {i} = {num * i}")
    i += 1

# Problem4: Write a program to find whether the given number is prime or not.

p = int(input("Enter a number:"))

if p <= 1:
    print(f"{p} is not a prime number.")

else:
    for i in range(2, p):
        if p % i == 0:
            print(f"{p} is not a prime number.")
            break
    else:
        print(f"{p} is a prime number.")

# Problem5: Write a program to print all the prime numbers between 1 to 100.

for num in range (1, 100):
    if num > 1:
        for i in range (2, num):
            if num % i == 0:
                break
        else:
            print(num)

# Problem6: Write a program to find the sum of first n natural numbers using while loop.

s = int(input("Enter a number:"))

i = 1
sum = 0
while(i <= s):
    sum += i
    i += 1
print(sum)

# Problem7: Write a program to calculate the factorial of a given number using for loop.

f = int(input("Enter a number:"))

product = 1
for i in range(1, f  + 1):
    product = product * i
print(f"The factorial of {f} is: {product}")

# Problem8: Write a program to print the following star patterns.
# 1)

a = int(input("Enter a number:"))

for i in range(1, a + 1):
    print(" "* (a - i), end = "")
    print("*" * (2 * i - 1), end = "")
    print("")

# 2)

b = int(input("Enter a number:"))

for i in range(1, b + 1):
    print("*" * i, end = "")
    print("")

# 3)

c = int(input("Enter a number:"))

for i in range(1, c + 1):
    if(i == 1 or i == c):
        print("*"* c, end = "")
    else:
        print("*", end = "")
        print(" " * (c - 2), end = "")
        print("*", end = "")
    print("")

# Problem9: Write a program to print multiplication table of n using for loop in reversed order.

t = int(input("Enter a number:"))

for i in range(1, 11):
    print(f"{t} X {11 - i} = {t * (11 - i)}")