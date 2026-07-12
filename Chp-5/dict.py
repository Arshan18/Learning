Marks = {
    "Andrew": 96 ,
    "Senorita": 69,
    "Sam": 56,
    "list": [1, 2, 3, 4]
}

# print(Marks)
# print(type(Marks))

# print(Marks.items())
# print(Marks.keys())
# print(Marks.values())

Marks.update({"Sam": 59, "Alisia": 50, "Ro": 45})
print(Marks)

print(Marks.get("Ro"))
print(Marks["Ro"])

Marks.pop("list")
print(Marks)