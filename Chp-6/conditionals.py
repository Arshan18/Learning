# If-else example

a = int(input("Enter your age: "))

if(a>=18):
    print("Person is eligible for voting")

else:
    print("Person is not eligible for voting")  


# If-elif-else example

role = input("Enter your role:")

if role == "Admin":
    print("Access to all features")

elif role == "Manager":
    print("Access to reports and employees")

elif role == "Employee":
    print("Access to your dashboard")

else:
    print("Access Denied")