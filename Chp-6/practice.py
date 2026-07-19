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
# "Make a lot of money", "buy now", "subscribe this", "click this". Wrtie a program to detect this spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comments: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This commment is a spam")
else:
    print("This comment is not a spam")

# Problem 4: Write a program to find whether a given username contains less than 10 characters or not.

userName = input("Enter userName:")

if(len(userName)) <= 10:
    print("Username contains less than or equal to 10 characters")
else:
    print("Username contains more than 10 characters")

# Problem 5: Write a program which finds oout whether a given name is present in a list or not.

l = ["Naman", "Tanmay", "Rohit", "Khush", "Raj", "Gulrez"]

name = input("Enter your name: ")

if(name in l):
    print("Your name is in the list")
else:
    print("Your name is not in the list")

# Problem 6: Write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100 => O, 80-90 => A, 70-80 => B, 60-70 => C, 50-60 => D, 40-50 => E, <50 => F

Marks = int(input("Enter you marks: "))

if(Marks <= 100 and Marks >= 90):
    grade = "O"
elif(Marks < 90 and Marks >= 80):
    grade = "A"
elif(Marks < 80 and Marks >= 70):
    grade = "B"
elif(Marks < 70 and Marks >= 60):
    grade = "C"
elif(Marks < 60 and Marks >= 50):
    grade = "D"
elif(Marks < 50 and Marks >= 40):
    grade = "E"
else:
    grade = "F"

print("Your grade is:", grade)

# Problem 7: Write a program to check whether an email mentions "meeting".

email = input("Enter email:")

if("meeting" in email.lower()):
    print("Meeting-related email.")
else:
    print("No meeting mentioned")