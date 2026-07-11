a= (1, 23, 4.5, "Hello", False)
print(type(a))


# count of 1 in tuple
no = a.count(1)
print(no)

# Index of 4.5
i = a.index(4.5)
print(i)

# concatenation of tuples

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
concatenated = tup1 + tup2
print(concatenated)

# Repeatition of tuples

repeated = tup1 * 2
print(repeated)

# Membership is used to check if an element is present in the tuple or not.

print(2 in tup1)

# minimum and maximum function is used to get the smallest and the largest element in the tuple.
print(min(tup2))
print(max(tup2))

a, b, c = tup1
print(a, b, c)