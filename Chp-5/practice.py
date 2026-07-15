# Problem1: Write a program to create a dictionary of Hindi Words with values as their English translation. Provide a userwith an option to look it up!

Words = {
    "Billi": "Cat",
    "Kutta": "Dog",
    "madad": "Help",
    "Kursi": "Chair",
    "Ghar": "House"
}

word = input("Enter a Hindi word:")

print("Meaning:", Words.get(word, "Word not found in dictionary")) 

# Problem2: Write a program to input 8 mumber from the user and display all the unique number once

s = set()

n1 = input("Enter no 1:")
s.add(int(n1))
n2 = input("Enter no 2:")
s.add(int(n2))
n3 = input("Enter no 3:")
s.add(int(n3))
n4 = input("Enter no 4:")
s.add(int(n4))
n5 = input("Enter no 5:")
s.add(int(n5))
n6 = input("Enter no 6:")
s.add(int(n6))
n7 = input("Enter no 7:")
s.add(int(n7))
n8 = input("Enter no 8:")
s.add(int(n8))

print(s)

# Problem3: can we have set with 18 (int) and '18' stras a value in it 

s1 = set()
s1.add(18)
s1.add("18")
print(s1)

# Problem4: what will be the length of the following set:

set1 = set()
set1.add(20)
set1.add(20.0)
set1.add('20')
print(len(set1))

#  Problem5: s = {} | What is the type of s?

ss = {}
print(type(ss))

# Problem6: Create an empty dictionary. Allow 4 freinds to enter their favorite language as value and use key as their name. Assumethat the names are unique.

d = {}

name = input("Enter friend name:")
lang = input("Enter language name:")
d.update({name : lang})
name = input("Enter friend name:")
lang = input("Enter language name:")
d.update({name : lang})
name = input("Enter friend name:")
lang = input("Enter language name:")
d.update({name : lang})
name = input("Enter friend name:")
lang = input("Enter language name:")
d.update({name : lang})
print(d)

# Problem7: If the names of 2 friends are same, What will happen to the program in problem 6.

# Answer: The second value will overwrite the first one because dictionary keys must be unique.

# Ash: Java,  Ash: Python  # the answer will be the Ash: Python

# Problem8: if languages of 2 friends are same; what will happento the program in problem 6.

# Answer: Nothing happens. The dictionary accepts duplicate values. Only keys must be unique.

# Sam: English,  Ron: English # the answer will be Sam: English, Ron: English


# Problem9: can you change the values inside a listwhich is contained in set S?  s = {8, 10, 18, "Jordan", [1, 3, 5]}

# s = {8, 10, 18, "Jordan", [1, 3, 5]}

# Answer: No, because a list cannot even be an element of a set. Python will raise a TypeError when creating the set.