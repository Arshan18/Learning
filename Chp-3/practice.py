# Problem1: Write a python program to display a user entered name followed by Good morning using input() function.

name = input("Enter your name: ")
print(f"Good morning {name}")

# Problem2: wrtie a python program to fill in a letter template given below with name and date .

letter = '''Dear <Name>,
    You are selected!
    <Date>
            ''' 

print(letter.replace("<Name>", name).replace("<Date>",  "21 March 2026"))

# Problem3: Write a python program to detect double spaces in a string.
str = "Time to learn  python"
print(str.find("  "))

# Problem4: Replace the  double spaces from the problem 3 with single space.

print(str.replace("  ", " "))

# Problem5: Write a program to format the following letter using the escape sequence characters.

# letter1 = '''Dear XYZ, This course is nice. Thanks!'''
letter1 = '''Dear XYZ,\n\tThis course is nice.\nThanks!'''
print(letter1)

# Problem6: 

letter2 = "Hii,/n My name is Goblin,/n and i am currently playing for team Soul"
print(letter2)