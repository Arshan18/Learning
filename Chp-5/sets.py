s = {1, 2, 3, 56, 2, "Sammy"}
# print(s, type(s))

# Methods

# 1.add method

s.add("Ash")
print(s)

# 2.remove 

s.remove("Sammy")
print(s)

# Union

s1 = {1, 12, 34, 54, 69}
s2 = {1, 13, 34, 45, 96}

print(s1.union(s2))
print(s1.intersection(s2)) #print the common elements from both the sets.

print(s1.issubset(s2))
print(s1.issuperset(s2))