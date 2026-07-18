# Problem 1: Write a program to find the greatest of four numbers entered by the user.

a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:", a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:", a3)
elif(a4>a1 and a4>a2 and a4>a3):
    print("Greatest number is a4:", a4)

# Problem 2: Write a program to find out whether a student has passed or faled if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjecrs and take markss as an input from the user.

M1 = int(input("Enter Marks 1: "))
M2 = int(input("Enter Marks 2: "))
M3 = int(input("Enter Marks 3: "))

total_percentage = (100*(M1 + M2 + M3)) / 300

if(total_percentage >= 40 and M1 >= 33 and M2 >= 33 and M3 >= 33):
    print("Passed",total_percentage)
else:
    print("Failed, better luck next time",total_percentage)

# Problem 3: A spam comment is defined as a text containing following keywords:
# "Make a lot af money", "buy now", "subscribe this", "click this". Wrtie a program to detect this spams.