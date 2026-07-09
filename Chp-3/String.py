# String Functions

# 1.Len() function is use to find the kenght of the string.

name = "Alice"
print(len(name))

# 2. startswith()function is use to check the string start with a specific character or not.

print(name.startswith("A"))

# 3. endswith() function is use to check the string end with the specific character or not.

print(name.endswith("ce"))

# 4. lower() function is use to convert the string into lower case.
a = "HELLO"
b = a.lower()
print(b)

# 5. Upper() function is use to convert the string into upper case.

print(b.upper())

# 6. count() function is use to count the number of specific character in the string.

str = "abacas"
print(str.count("a"))

# 7. find() function is use to find the index of the specific character in the string.

print(name.find("i"))

# 8. replace()function is used to replace the specific word or character in the string with the new word or character.

s = "Hello world"
replaced_string = s.replace("world", "Python")
print(replaced_string)

# 9. title() function is  used to capatalize the  first character of each word in the strings.

print(s.title())

# 10. strip() function is used to remove the leading and the trailing spaces from the string.

x = "   Hello python    " 
print(x.strip())

# 11. Split() function is used to split a string into a list.

y = "Hello My Name is Rosemarry"
print(y.split())

#  12. join() function is used to join the elemnts of the list into a string.

list = ["Hello", "how", "are", "you"]
print(" ".join(list))

# 13. isalpha() function is used to check if all characters in a string are alphabet or not.

text = "python"
print(text.isalpha())

text2 = "python123"
print(text2.isalpha())

# 14. isdigit() function is used to check if all the  characters in a string is digit or not.

num = "123456789"
print(num.isdigit())

num2 = "123456789qwerty"
print(num2.isdigit())

# 15. isalnum() function is used to check if all the string contains only letters and numbers .

str = "Python123"
print(str.isalnum())

str1 = "python 123"
print(str1.isalnum())

# 16. islower() function is used to check if all the characters in a string are in lower case or not.

str2 = "python"
print(str2.islower())

# 17. isupper() function is used to check if all the characters in a string are in upper case or not.

str3 = "PYTHON"
print(str3.isupper())